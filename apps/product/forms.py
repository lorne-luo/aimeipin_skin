import os

from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from apps.analysis.models import SkinType
from core.django.widgets import ThumbnailImageInput
from .models import Product, Brand, ProductIngredient, ProductAnalysis


class ProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("Picture"), required=False,
                           widget=ThumbnailImageInput({'width': '210px'}))

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


class ProductImportForm(forms.Form):
    product_file = forms.FileField(label='产品excel', required=False)
    component_file = forms.FileField(label='产品成分excel', required=False)

    def validate_filefield(self, file):
        if file:
            file_name, file_ext = os.path.splitext(file.name)
            if file_ext.lower() not in ['.xls', '.xlsx']:
                raise forms.ValidationError("请提交扩展名为xls/xlsx的Excel文件.")

    def clean_product_file(self):
        product_file = self.cleaned_data.get('product_file', None)
        self.validate_filefield(product_file)
        return product_file

    def clean_component_file(self):
        component_file = self.cleaned_data.get('component_file', None)
        self.validate_filefield(component_file)
        return component_file

    def clean(self):
        product_file = self.cleaned_data.get('product_file', None)
        component_file = self.cleaned_data.get('component_file', None)
        if not product_file and not component_file:
            raise forms.ValidationError("至少提供一组Excel文件.")


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
        self.fields['analysis'].widget.attrs['rows'] = 4
        self.fields['analysis'].widget.attrs['cols'] = 40
        self.fields['oily_type'].queryset = SkinType.objects.filter(dimension='油性or干性')
        self.fields['sensitive_type'].queryset = SkinType.objects.filter(dimension='敏感or耐受')
        self.fields['pigment_type'].queryset = SkinType.objects.filter(dimension='色素or非色素')
        self.fields['loose_type'].queryset = SkinType.objects.filter(dimension='易皱纹or紧致')


ProductAnalysisFormSet = inlineformset_factory(Product, ProductAnalysis, form=ProductAnalysisInlineForm,
                                               can_order=False, can_delete=True, extra=1)
