# coding=utf-8
from django import forms
from django.contrib import admin
from django.forms.models import modelformset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from apps.survey.models import Answer
from .models import Customer


class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'sex', 'age', 'height', 'weight', 'job', 'monthly_income', 'address', 'weixin_id', 'remark',
                  'email', 'mobile']


class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'sex', 'age', 'height', 'weight', 'job', 'monthly_income', 'address', 'weixin_id', 'remark',
                  'email', 'mobile']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'sex', 'age', 'height', 'weight', 'job', 'monthly_income', 'address', 'weixin_id', 'remark',
                  'email', 'mobile']



class AnswerInlineForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AnswerInlineForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['class'] = 'form-control'

        self.fields['customer'].widget = forms.HiddenInput()


AnswerFormSet = modelformset_factory(Answer, form=AnswerInlineForm, can_order=False, can_delete=False, extra=1)