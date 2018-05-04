# coding=utf-8
import logging
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypinyin import Style
from stdimage import StdImageField
from taggit.managers import TaggableManager

from django_countries.fields import CountryField
from core.django.models import PinYinFieldModelMixin, ResizeUploadedImageModelMixin
from config.settings import BRAND_LOGO_PHOTO_FOLDER, MEDIA_URL, MEDIA_ROOT

log = logging.getLogger(__name__)


def get_brand_logo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = instance.brand.name_en + '_' if instance.brand.name_en else ''
    filename = '%s%s' % (filename, instance.name_en)
    filename = filename.replace(' ', '-')
    filename = '%s.%s' % (filename, ext)
    file_path = os.path.join(BRAND_LOGO_PHOTO_FOLDER, filename)

    from apps.celery.tasks import guetzli_compress_image
    full_path = os.path.join(MEDIA_ROOT, file_path)
    guetzli_compress_image.apply_async(args=[full_path], countdown=30)
    return file_path


class Brand(ResizeUploadedImageModelMixin, PinYinFieldModelMixin, models.Model):
    """品牌，skin_brand"""
    country = CountryField(verbose_name=_('country'))
    name_en = models.CharField(_('name_en'), max_length=128, blank=True)
    name_cn = models.CharField(_('name_cn'), max_length=128, blank=True)
    name_py = models.CharField(_('name_py'), max_length=128, blank=True)
    first_letter_en = models.CharField(_('first_letter_en'), max_length=128, blank=True)
    first_letter_cn = models.CharField(_('first_letter_cn'), max_length=128, blank=True)
    pinyin = models.TextField(_('pinyin'), max_length=512, blank=True)
    logo = StdImageField(upload_to=get_brand_logo_path, blank=True, null=True, verbose_name=_('logo'),
                         variations={
                             'medium': (800, 800, True),
                             'thumbnail': (400, 400, True)
                         })
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)
    aliases = TaggableManager(verbose_name='aliases')

    pinyin_fields_conf = [
        ('name_cn', Style.NORMAL, False),
        ('name_cn', Style.FIRST_LETTER, False),
    ]

    class Meta:
        verbose_name_plural = _('Brand')
        verbose_name = _('Brand')
        unique_together = ("name_en", "name_cn")
        index_together = ("name_en", "name_cn")

    def __str__(self):
        return self.name_cn or self.name_en

    def save(self, *args, **kwargs):
        self.resize_image('logo')  # resize images when first uploaded

        super(Brand, self).save(*args, **kwargs)

