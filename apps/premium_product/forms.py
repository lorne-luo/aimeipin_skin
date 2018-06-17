from django import forms
from django.forms import inlineformset_factory, formset_factory
from django.utils.translation import ugettext_lazy as _

from config.constants import PURPOSE_CHOICES, SKIN_TYPE_CHOICES, PRODUCT_CATEGORY_CHOICES
from core.django.autocomplete import FormsetModelSelect2
from core.django.widgets import ThumbnailImageInput
from .models import PremiumProduct, Brand, PremiumProductFit


class PremiumProductAddForm(forms.ModelForm):
    pic = forms.ImageField(label=_("picture"), required=False,
                           widget=ThumbnailImageInput({'width': '280px'}))

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


class PremiumProductSelectForm(forms.Form):
    skin_type = forms.ChoiceField(label='肤质', choices=(('------', ''),) + SKIN_TYPE_CHOICES, required=False)
    purpose = forms.ChoiceField(label='目标', choices=(('------', ''),) + PURPOSE_CHOICES, required=False)
    category = forms.ChoiceField(label='类别', choices=(('------', ''),) + PRODUCT_CATEGORY_CHOICES, required=False)
    name = forms.CharField(label='名称', required=False)
