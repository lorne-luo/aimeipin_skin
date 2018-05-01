# coding=utf-8
from django import forms
from django.contrib import admin
from django.forms.models import modelformset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

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
