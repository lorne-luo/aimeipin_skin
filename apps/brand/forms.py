from django import forms
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Brand


class BrandAddForm(forms.ModelForm):
    logo = forms.ImageField(label=_("Logo"), required=False,
                            widget=ThumbnailImageInput({'width': '280px', 'size': 'thumbnail'}))

    class Meta:
        model = Brand
        fields = ['name_en', 'name_cn', 'aliases', 'logo']


class BrandUpdateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name_en', 'first_letter_en', 'name_cn', 'first_letter_cn', 'aliases', 'logo']


class BrandDetailForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name_en', 'first_letter_en','name_cn','first_letter_cn', 'aliases', 'logo']
