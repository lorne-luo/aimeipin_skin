from django import forms
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import PremiumProduct, Brand


class PremiumProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("picture"), required=False,
                           widget=ThumbnailImageInput({'width': '280px', 'size': 'thumbnail'}))

    class Meta:
        model = PremiumProduct
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand']

    def __init__(self, *args, **kwargs):
        super(PremiumProductAddForm, self).__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all().order_by('name_en')


class PremiumProductAdminForm(PremiumProductAddForm):
    class Meta:
        model = PremiumProduct
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand', ]


class PremiumProductDetailForm(forms.ModelForm):
    class Meta:
        model = PremiumProduct
        fields = ['name_en', 'name_cn', 'alias', 'pic']
