# coding=utf-8
import logging
import os
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from pypinyin import Style
from stdimage import StdImageField
from taggit.managers import TaggableManager

from config.constants import PRODUCT_CATEGORY_CHOICES, PURPOSE_CHOICES, SKIN_TYPE_CHOICES
from core.auth_user.models import AuthUser
from core.django.models import PinYinFieldModelMixin, ResizeUploadedImageModelMixin
from config.settings import PREMIUM_PRODUCT_PHOTO_FOLDER, MEDIA_ROOT
from ..brand.models import Brand

log = logging.getLogger(__name__)


def get_premium_product_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = instance.brand.name_en + '_' if instance.brand.name_en else ''
    filename = '%s%s' % (filename, instance.name_en)
    filename = filename.replace(' ', '-')
    filename = '%s.%s' % (filename, ext)
    file_path = os.path.join(PREMIUM_PRODUCT_PHOTO_FOLDER, filename)

    from apps.celery.tasks import guetzli_compress_image
    full_path = os.path.join(MEDIA_ROOT, file_path)
    guetzli_compress_image.apply_async(args=[full_path], countdown=30)
    return file_path


class PremiumProductManager(models.Manager):
    DEFAULT_CACHE_KEY = 'QUERYSET_CACHE_DEFAULT_PREMIUMPRODUCT'

    def clean_cache(self):
        log.info('[QUERYSET_CACHE] clean carriers.')
        cache.delete(self.DEFAULT_CACHE_KEY)


'''
| fuzhi        |
+--------------+
| 油性肌肤     |
| 干性肌肤

+-----------+
| mubiao    |
+-----------+
| 急镇定    |
| 抗轻衰    |
| 收毛孔    |
| 清痘痘    |
| 祛暗沉    |
| 调水油    |
+-----------+
+---------------+
| leibie        |
+---------------+
| 乳液/面霜     |
| 卸妆          |
| 去角质        |
| 化妆水        |
| 洁面          |
| 精华          |
| 防晒          |
| 面膜          |
+---------------+
'''


class PremiumProduct(ResizeUploadedImageModelMixin, PinYinFieldModelMixin, models.Model):
    sku = models.CharField(max_length=36, unique=True, null=True, blank=True)
    brand = models.ForeignKey(Brand, blank=True, null=True, verbose_name=_('brand'))
    name_en = models.CharField(_(u'name_en'), max_length=128, blank=True)
    name_cn = models.CharField(_(u'name_cn'), max_length=128, blank=True)
    pinyin = models.TextField(_('pinyin'), max_length=512, blank=True)
    pic = StdImageField(upload_to=get_premium_product_pic_path, blank=True, null=True, verbose_name=_('picture'),
                        variations={
                            'medium': (800, 800, True),
                            'thumbnail': (400, 400, True)
                        })
    skin_type = models.CharField(max_length=64, choices=SKIN_TYPE_CHOICES, null=True, blank=True)
    sold_count = models.IntegerField(_(u'Sold Count'), default=0, null=False, blank=False)
    description = models.TextField(_(u'description'), null=True, blank=True)
    category = models.CharField(max_length=64, choices=PRODUCT_CATEGORY_CHOICES, null=True, blank=True)
    purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES, null=True, blank=True)
    aliases = TaggableManager(verbose_name='aliases')

    pinyin_fields_conf = [
        ('name_cn', Style.NORMAL, False),
        ('name_cn', Style.FIRST_LETTER, False),
        ('brand.name_cn', Style.NORMAL, False),
        ('brand.name_cn', Style.FIRST_LETTER, False),
    ]
    objects = PremiumProductManager()

    class Meta:
        verbose_name_plural = _('Product')
        verbose_name = _('Product')

    def __str__(self):
        if self.brand and self.brand.name_en.lower() != 'none':
            return '%s %s' % (self.brand.name_en, self.name_cn)
        else:
            return self.name_cn

    def __init__(self, *args, **kwargs):
        super(PremiumProduct, self).__init__(*args, **kwargs)
        field_names = ['name_en', 'name_cn', 'brand_id', 'brand_en', 'brand_cn']
        for field_name in set(field_names):
            current_value = self.get_attr_by_str(field_name)
            self._original_fields_value.update({field_name: current_value})

    def save(self, *args, **kwargs):
        self.resize_image('pic')  # resize images when first uploaded

        update_cache = kwargs.pop('update_cache', True)  # default to update cache
        super(PremiumProduct, self).save(*args, **kwargs)
        if update_cache:
            PremiumProduct.objects.clean_cache()


@receiver(post_delete, sender=PremiumProduct)
def product_deleted(sender, **kwargs):
    instance = kwargs['instance']
    PremiumProduct.objects.clean_cache()
