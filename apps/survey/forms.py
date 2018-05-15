from django import forms
from django.utils.translation import ugettext_lazy as _

from core.django.widgets import ThumbnailImageInput
from .models import Answer


class AnswerAddForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerUpdateForm(AnswerAddForm):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerDetailForm(AnswerAddForm):
    class Meta:
        model = Answer
        fields = '__all__'
