from django import forms
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Report


class ReportAddForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


class ReportUpdateForm(ReportAddForm):
    class Meta:
        model = Report
        fields = '__all__'


class ReportDetailForm(ReportAddForm):
    class Meta:
        model = Report
        fields = '__all__'
