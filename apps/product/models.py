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
from taggit.managers import TaggableManager

from config.constants import PRODUCT_CATEGORY_CHOICES, SKIN_OILY_TYPE_CHOICES, SKIN_SENSITIVE_TYPE_CHOICES, \
    SKIN_PIGMENT_TYPE_CHOICES, SKIN_LOOSE_TYPE_CHOICES
from core.django.models import PinYinFieldModelMixin, ResizeUploadedImageModelMixin
from config.settings import PRODUCT_PHOTO_FOLDER, MEDIA_ROOT
from ..brand.models import Brand

log = logging.getLogger(__name__)


def get_product_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = instance.brand.name_en + '_' if instance.brand.name_en else ''
    filename = '%s%s' % (filename, instance.name_en)
    filename = filename.replace(' ', '-')
    filename = '%s.%s' % (filename, ext)
    file_path = os.path.join(PRODUCT_PHOTO_FOLDER, filename)

    # from apps.celery.tasks import guetzli_compress_image
    # full_path = os.path.join(MEDIA_ROOT, file_path)
    # guetzli_compress_image.apply_async(args=[full_path], countdown=30)
    return file_path


class ProductManager(models.Manager):
    DEFAULT_CACHE_KEY = 'QUERYSET_CACHE_DEFAULT_PRODUCT'

    def clean_cache(self):
        log.info('[QUERYSET_CACHE] clean carriers.')
        # cache.delete(self.DEFAULT_CACHE_KEY)


class Product(ResizeUploadedImageModelMixin, PinYinFieldModelMixin, models.Model):
    """普通产品库，由爬虫导入，客户输入现用产品时使用，不会推荐给客人, skin_product"""
    # sku = models.CharField(max_length=36, unique=True, blank=True)
    brand = models.ForeignKey(Brand, blank=True, null=True)
    name_en = models.CharField(_(u'name_en'), max_length=255, blank=True)
    name_cn = models.CharField(_(u'name_cn'), max_length=255, blank=True)
    pinyin = models.CharField(_(u'pinyin'), max_length=512, blank=True)
    pic = StdImageField(upload_to=get_product_pic_path, blank=True, null=True, verbose_name=_('picture'),
                        variations={
                            'medium': (800, 800, True),
                            'thumbnail': (400, 400, True)
                        })
    alias = models.CharField(_(u'alias'), max_length=255, blank=True)
    category = models.CharField(max_length=64, choices=PRODUCT_CATEGORY_CHOICES, blank=True)
    description = models.TextField(_(u'description'), blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)
    ingredients = models.ManyToManyField('product.ProductIngredient', blank=True, verbose_name=u'成分组成')

    pinyin_fields_conf = [
        ('name_cn', Style.NORMAL, False),
        ('alias', Style.NORMAL, False),
    ]
    objects = ProductManager()

    def __str__(self):
        if self.brand and self.brand.name_cn:
            return '%s %s' % (self.brand.name_cn, self.name_cn)
        else:
            return self.name_cn

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        field_names = ['name_en', 'name_cn', 'brand_id', 'brand_en', 'brand_cn']
        for field_name in set(field_names):
            current_value = self.get_attr_by_str(field_name)
            self._original_fields_value.update({field_name: current_value})

    def save(self, *args, **kwargs):
        self.resize_image('pic')  # resize images when first uploaded
        update_cache = kwargs.pop('update_cache', True) or not self.id  # default to update cache
        super(Product, self).save(*args, **kwargs)
        if update_cache:
            Product.objects.clean_cache()


@receiver(post_delete, sender=Product)
def product_deleted(sender, **kwargs):
    instance = kwargs['instance']
    Product.objects.clean_cache()


class ProductIngredient(models.Model):
    """产品成分, skin_component"""
    name = models.CharField(_(u'name'), max_length=255, blank=True)
    is_safe = models.BooleanField(_(u'安全风险'), default=False, blank=True)  # 是否安全
    safe = models.CharField(_(u'safe'), max_length=255, blank=True)
    is_live = models.BooleanField(_(u'活性成分'), default=False, blank=True)  # 活性因子
    is_pox = models.BooleanField(_(u'致痘风险'), default=False, blank=True)  # 导致起痘
    effect = models.CharField(_(u'使用目的'), max_length=255, blank=True)
    description = models.TextField(_(u'描述'), max_length=512, blank=True)

    def __str__(self):
        return self.name

class ProductAnalysis(models.Model):
    """产品的肤质阐述 skin_p_t"""
    product = models.ForeignKey('product.Product', blank=True, null=True)
    oily_type = models.CharField(_(u'油性or干性'), max_length=64, choices=SKIN_OILY_TYPE_CHOICES, blank=True)
    sensitive_type = models.CharField(_(u'敏感or耐受'), max_length=64, choices=SKIN_SENSITIVE_TYPE_CHOICES, blank=True)
    pigment_type = models.CharField(_(u'色素or非色素'), max_length=64, choices=SKIN_PIGMENT_TYPE_CHOICES, blank=True)
    loose_type = models.CharField(_(u'易皱or紧致'), max_length=64, choices=SKIN_LOOSE_TYPE_CHOICES, blank=True)
    analysis = models.TextField(_(u'对应阐述'), max_length=64, blank=True)
