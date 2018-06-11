from django import forms
from django.forms import inlineformset_factory

from apps.premium_product.models import PremiumProduct
from core.django.autocomplete import FormsetModelSelect2
from .models import Report, ReportPremiumProduct


class ReportAddForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['answer', 'purpose', 'level']

    def __init__(self, *args, **kwargs):
        super(ReportAddForm, self).__init__(*args, **kwargs)
        self.fields['answer'].widget = forms.HiddenInput()
        self.fields['purpose'].required = True
        self.fields['level'].required = True


class ReportUpdateForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ['answer', 'level', 'day_products', 'night_products', 'mask_products']


class ReportDetailForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


class PremiumProductInlineForm(forms.ModelForm):
    # id = forms.IntegerField(widget=forms.HiddenInput)
    type = forms.CharField(widget=forms.HiddenInput, required=False)
    product = forms.ModelChoiceField(label=u'优选产品', queryset=PremiumProduct.objects.all(), required=True,
                                     widget=FormsetModelSelect2(url='api:premiumproduct-autocomplete',
                                                                attrs={'data-placeholder': u'任意中英文名称...',
                                                                       'class': 'form-control'})
                                     )

    class Meta:
        model = ReportPremiumProduct
        fields = ['id', 'type', 'report', 'product']

    def clean(self):
        product = self.cleaned_data.get('product', None)
        if product:
            if self.prefix.startswith('day_products_formset'):
                self.cleaned_data['type'] = '日间'
            elif self.prefix.startswith('night_products_formset'):
                self.cleaned_data['type'] = '夜间'
            elif self.prefix.startswith('mask_products_formset'):
                self.cleaned_data['type'] = '面膜'
        return self.cleaned_data


PremiumProductFormSet = inlineformset_factory(Report, ReportPremiumProduct, form=PremiumProductInlineForm,
                                              can_order=False, can_delete=True, extra=1)
