# coding=utf-8
from django import forms
from django.contrib import admin
from django.forms.models import modelformset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from core.django.forms import NoManytoManyHintModelForm
from .models import Customer


class CustomerAddForm(NoManytoManyHintModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'remark', 'email', 'mobile']


class CustomerDetailForm(NoManytoManyHintModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'remark', 'email', 'mobile', 'primary_address']


class CustomerUpdateForm(NoManytoManyHintModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'remark', 'email', 'mobile', 'primary_address']
