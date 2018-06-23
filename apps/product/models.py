# coding=utf-8
import logging
import os
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from pypinyin import Style, pinyin
from stdimage import StdImageField
from stdimage.utils import UploadToClassNameDir
from taggit.managers import TaggableManager

from config.constants import PRODUCT_CATEGORY_CHOICES, SKIN_OILY_TYPE_CHOICES, SKIN_SENSITIVE_TYPE_CHOICES, \
    SKIN_PIGMENT_TYPE_CHOICES, SKIN_LOOSE_TYPE_CHOICES
from core.django.models import PinYinFieldModelMixin, ResizeUploadedImageModelMixin
from config.settings import PRODUCT_PHOTO_FOLDER, MEDIA_ROOT
from ..brand.models import Brand

log = logging.getLogger(__name__)


class Product(ResizeUploadedImageModelMixin, PinYinFieldModelMixin, models.Model):
    """普通产品库，由爬虫导入，客户输入现用产品时使用，不会推荐给客人, skin_product"""
    # sku = models.CharField(max_length=36, unique=True, blank=True)
    brand = models.ForeignKey(Brand, blank=True, null=True)
    name_en = models.CharField(_(u'name_en'), max_length=512, blank=True)
    name_cn = models.CharField(_(u'name_cn'), max_length=512, blank=True)
    pinyin = models.CharField(_(u'pinyin'), max_length=1024, blank=True)
    pic = StdImageField(upload_to=UploadToClassNameDir(), blank=True, null=True, verbose_name=_('picture'),
                        variations={
                            'thumbnail': (64, 64, True),
                        })
    alias = models.CharField(_(u'alias'), max_length=512, blank=True)
    category = models.CharField(max_length=64, choices=PRODUCT_CATEGORY_CHOICES, blank=True)
    description = models.TextField(_(u'description'), blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)
    ingredients = models.ManyToManyField('product.ProductIngredient', blank=True, verbose_name=u'成分组成')

    pinyin_fields_conf = [
        ('name_cn', Style.NORMAL, False),
        ('alias', Style.NORMAL, False),
    ]

    def __str__(self):
        if self.brand and self.name_cn:
            if (self.brand.name_cn and self.brand.name_cn in self.name_cn) or (self.brand.name_en and self.brand.name_en in self.name_cn):
                return self.name_cn
        if self.brand:
            return '%s %s' % (self.brand, self.name_cn)
        return self.name_cn

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        field_names = ['name_en', 'name_cn', 'brand_id', 'brand_en', 'brand_cn']
        for field_name in set(field_names):
            current_value = self.get_attr_by_str(field_name)
            self._original_fields_value.update({field_name: current_value})

    def save(self, *args, **kwargs):
        self.resize_image('pic')  # resize images when first uploaded
        super(Product, self).save(*args, **kwargs)

    def get_analysis(self, oily_type, sensitive_type, pigment_type, loose_type):
        analysis = self.productanalysis_set.filter(oily_type=oily_type, sensitive_type=sensitive_type,
                                                   pigment_type=pigment_type, loose_type=loose_type)
        return '\n'.join([x.analysis for x in analysis])

    def have_duplicated(self):
        count = 0
        total = self.productanalysis_set.all().count()
        for i in range(total):
            for j in range(i + 1, total):
                if self.productanalysis_set.all()[i].oily_type == self.productanalysis_set.all()[j].oily_type and \
                                self.productanalysis_set.all()[i].sensitive_type == self.productanalysis_set.all()[
                            j].sensitive_type and \
                                self.productanalysis_set.all()[i].pigment_type == self.productanalysis_set.all()[
                            j].pigment_type and \
                                self.productanalysis_set.all()[i].loose_type == self.productanalysis_set.all()[
                            j].loose_type:
                    count += 1
                    print(self.productanalysis_set.all()[i].oily_type, self.productanalysis_set.all()[i].sensitive_type,
                          self.productanalysis_set.all()[i].pigment_type, self.productanalysis_set.all()[i].loose_type)

        if count > 0:
            return True
        return False


class ProductIngredient(models.Model):
    """产品成分, skin_component"""
    name = models.CharField(_(u'name'), max_length=512, blank=True)
    is_safe = models.BooleanField(_(u'安全风险'), default=False, blank=True)  # 是否安全
    safe = models.CharField(_(u'safe'), max_length=255, blank=True)
    is_live = models.BooleanField(_(u'活性成分'), default=False, blank=True)  # 活性因子
    is_pox = models.BooleanField(_(u'致痘风险'), default=False, blank=True)  # 导致起痘
    effect = models.TextField(_(u'使用目的'), blank=True)
    description = models.TextField(_(u'描述'), blank=True)

    def __str__(self):
        return self.name


class ProductAnalysis(models.Model):
    """产品的肤质阐述 skin_p_t"""
    product = models.ForeignKey('product.Product', blank=True, null=True)

    oily_type = models.ForeignKey('analysis.SkinType', verbose_name=_('油性or干性'), blank=True, null=True,
                                  related_name='product_analysis_oily_type')
    sensitive_type = models.ForeignKey('analysis.SkinType', verbose_name=_('敏感or耐受'), blank=True, null=True,
                                       related_name='product_analysis_sensitive_type')
    pigment_type = models.ForeignKey('analysis.SkinType', verbose_name=_('色素or非色素'), blank=True, null=True,
                                     related_name='product_analysis_pigment_type')
    loose_type = models.ForeignKey('analysis.SkinType', verbose_name=_('易皱纹or紧致'), blank=True, null=True,
                                   related_name='product_analysis_loose_type')

    analysis = models.TextField(_(u'对应阐述'), blank=True)

    class Meta:
        unique_together = ('product', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type')
