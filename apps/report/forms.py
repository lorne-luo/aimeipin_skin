from django import forms

from .models import Report


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
        exclude = ['answer', 'purpose', 'level', 'day_products', 'night_products', 'mask_products']


class ReportDetailForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
