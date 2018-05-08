from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Product, Brand, ProductIngredient


class ProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("Picture"), required=False,
                           widget=ThumbnailImageInput({'width': '280px', 'size': 'thumbnail'}))

    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand', 'brand', 'category', 'description']

    def __init__(self, *args, **kwargs):
        super(ProductAddForm, self).__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all().order_by('name_en')


class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand', 'category', 'description']


class ProductIngredientInlineForm(forms.ModelForm):
    class Meta:
        model = ProductIngredient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductIngredientInlineForm, self).__init__(*args, **kwargs)
        # for field_name in self.fields:
        #     field = self.fields.get(field_name)
            # field.widget.attrs['class'] = 'form-control'

        self.fields['product'].widget = forms.HiddenInput()


ProductIngredientFormSet = inlineformset_factory(Product, ProductIngredient, form=ProductIngredientInlineForm,
                                                 can_order=False, can_delete=True, extra=1)
