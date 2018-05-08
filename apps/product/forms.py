from django import forms
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Product, Brand


class ProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("Picture"), required=False,
                           widget=ThumbnailImageInput({'width': '280px', 'size': 'thumbnail'}))

    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand']

    def __init__(self, *args, **kwargs):
        super(ProductAddForm, self).__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all().order_by('name_en')


class ProductAdminForm(ProductAddForm):
    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand', ]


class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic']
