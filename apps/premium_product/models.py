# coding=utf-8
import logging
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypinyin import Style
from stdimage.utils import UploadToClassNameDir

from config.constants import PRODUCT_CATEGORY_CHOICES, PURPOSE_CHOICES, SKIN_TYPE_CHOICES
from core.django.fields import PNGThumbnailStdImageField
from core.django.models import PinYinFieldModelMixin, ResizeUploadedImageModelMixin
from ..brand.models import Brand

log = logging.getLogger(__name__)


class PremiumProduct(ResizeUploadedImageModelMixin, PinYinFieldModelMixin, models.Model):
    """优选产品, 会推荐销售给客户, skin_you_product"""
    brand = models.ForeignKey(Brand, blank=True, null=True, verbose_name=_('brand'))
    name_en = models.CharField(_(u'name_en'), max_length=512, blank=True)
    name_cn = models.CharField(_(u'name_cn'), max_length=512, blank=True)
    pinyin = models.TextField(_('pinyin'), max_length=1024, blank=True)
    pic = PNGThumbnailStdImageField(upload_to=UploadToClassNameDir(), blank=True, null=True, verbose_name=_('picture'),
                                    variations={
                                        'thumbnail': (150, 150, True)
                                    })
    description = models.TextField(_(u'description'), blank=True)
    alias = models.CharField(_(u'alias'), max_length=512, blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    pinyin_fields_conf = [
        ('name_cn', Style.NORMAL, True),
        ('alias', Style.NORMAL, True),
    ]

    class Meta:
        verbose_name_plural = _('PremiumProducts')
        verbose_name = _('PremiumProduct')

    def __str__(self):
        if self.brand and self.name_cn:
            if (self.brand.name_cn and self.brand.name_cn in self.name_cn) or (self.brand.name_en and self.brand.name_en in self.name_cn):
                return self.name_cn
        if self.brand:
            return '%s %s' % (self.brand, self.name_cn)
        return self.name_cn

    def match_brand(self):
        if not self.name_cn:
            return None
        brand1 = None
        brand2 = None
        for b in Brand.objects.all():
            if (b.name_cn and self.name_cn.startswith(b.name_cn)) or (b.name_en and self.name_cn.startswith(b.name_en)):
                brand1 = b
            if (b.name_cn and b.name_cn in self.name_cn) or (b.name_en and b.name_en in self.name_cn):
                brand2 = b
        return brand1 or brand2

    def __init__(self, *args, **kwargs):
        super(PremiumProduct, self).__init__(*args, **kwargs)
        field_names = ['name_en', 'name_cn', 'brand_id', 'brand_en', 'brand_cn']
        for field_name in set(field_names):
            current_value = self.get_attr_by_str(field_name)
            self._original_fields_value.update({field_name: current_value})

    def save(self, *args, **kwargs):
        if not self.id and not self.brand:
            self.brand = self.match_brand()

        self.resize_image('pic')  # resize images when first uploaded
        super(PremiumProduct, self).save(*args, **kwargs)

    @staticmethod
    def search_fit(**kwargs):
        if kwargs:
            product_ids = [x.product_id for x in PremiumProductFit.objects.filter(**kwargs)]
            return PremiumProduct.objects.filter(id__in=product_ids)
        else:
            return PremiumProduct.objects.all()

    def has_combine(self, skin_type, purpose, category):
        for fit in self.premiumproductfit_set.all():
            if [skin_type, purpose, category] == [fit.skin_type, fit.purpose, fit.category]:
                return True
        return False


class PremiumProductFit(models.Model):
    """优选产品适合的肤质组合"""
    product = models.ForeignKey('premium_product.PremiumProduct', blank=True, null=True)
    purpose = models.CharField(_(u'目标'), max_length=64, choices=PURPOSE_CHOICES, blank=True)
    skin_type = models.CharField(_(u'肤质'), max_length=64, choices=SKIN_TYPE_CHOICES, blank=True)
    category = models.CharField(_(u'分类'), max_length=64, choices=PRODUCT_CATEGORY_CHOICES, blank=True)
