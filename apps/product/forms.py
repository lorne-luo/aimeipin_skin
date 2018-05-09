from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Product, Brand, ProductIngredient, ProductAnalysis


class ProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("Picture"), required=False,
                           widget=ThumbnailImageInput({'width': '210px', 'size': 'thumbnail'}))

    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand', 'brand', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductAddForm, self).__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all().order_by('name_en')


class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand', 'category']


class ProductIngredientInlineForm(forms.ModelForm):
    class Meta:
        model = ProductIngredient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductIngredientInlineForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['class'] = 'form-control'

        self.fields['product'].widget = forms.HiddenInput()


ProductIngredientFormSet = inlineformset_factory(Product, ProductIngredient, form=ProductIngredientInlineForm,
                                                 can_order=False, can_delete=True, extra=0)


class ProductAnalysisInlineForm(forms.ModelForm):
    class Meta:
        model = ProductAnalysis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAnalysisInlineForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['class'] = 'form-control'

        self.fields['product'].widget = forms.HiddenInput()

        self.fields['analysis'].widget.attrs['rows'] = 2
        self.fields['analysis'].widget.attrs['cols'] = 40


ProductAnalysisFormSet = inlineformset_factory(Product, ProductAnalysis, form=ProductAnalysisInlineForm,
                                               can_order=False, can_delete=True, extra=1)
