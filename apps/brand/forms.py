from django import forms
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Brand


class BrandAddForm(forms.ModelForm):
    logo = forms.ImageField(label=_("Logo"), required=False,
                            widget=ThumbnailImageInput({'width': '210px', 'size': 'thumbnail'}))

    class Meta:
        model = Brand
        fields = ['name_en', 'name_cn', 'logo']


class BrandUpdateForm(BrandAddForm):
    class Meta:
        model = Brand
        fields = ['logo', 'name_en', 'first_letter_en', 'name_cn', 'first_letter_cn', 'alias']


class BrandDetailForm(BrandAddForm):
    class Meta:
        model = Brand
        fields = ['name_en', 'name_cn', 'logo']
