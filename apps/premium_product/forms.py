from django import forms
from django.forms import inlineformset_factory, formset_factory
from django.utils.translation import ugettext_lazy as _

from core.django.autocomplete import FormsetModelSelect2
from core.django.widgets import ThumbnailImageInput
from .models import PremiumProduct, Brand, PremiumProductFit


class PremiumProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("picture"), required=False,
                           widget=ThumbnailImageInput({'width': '280px', 'size': 'thumbnail'}))

    class Meta:
        model = PremiumProduct
        fields = ['name_en', 'name_cn', 'alias', 'pic', 'brand']

    def __init__(self, *args, **kwargs):
        super(PremiumProductAddForm, self).__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all().order_by('name_en')


class PremiumProductDetailForm(forms.ModelForm):
    class Meta:
        model = PremiumProduct
        fields = ['name_en', 'name_cn', 'alias', 'pic']


class PremiumProductFitInlineForm(forms.ModelForm):
    class Meta:
        model = PremiumProductFit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PremiumProductFitInlineForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['class'] = 'form-control'

        self.fields['product'].widget = forms.HiddenInput()


PremiumProductFitFormSet = inlineformset_factory(PremiumProduct, PremiumProductFit, form=PremiumProductFitInlineForm,
                                                 can_order=False, can_delete=True, extra=1)


class PremiumProductInlineForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    product = forms.ModelChoiceField(label=u'优选产品', queryset=PremiumProduct.objects.all(), required=True,
                                     widget=FormsetModelSelect2(url='api:premiumproduct-autocomplete',
                                                                attrs={'data-placeholder': u'任意中英文名称...',
                                                                       'class': 'form-control'})
                                     )
    class Meta:
        fields = ['id', 'product']


PremiumProductFormSet = formset_factory(PremiumProductInlineForm, extra=1, can_delete=True)
