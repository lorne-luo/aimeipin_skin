from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Word, SkinType


class WordAddForm(forms.ModelForm):
    class Meta:
        model = Word
        exclude = ['pinyin']


class WordUpdateForm(WordAddForm):
    class Meta:
        model = Word
        exclude = ['pinyin']


class WordDetailForm(WordAddForm):
    class Meta:
        model = Word
        exclude = ['pinyin']



class SkinTypeAddForm(forms.ModelForm):
    class Meta:
        model = SkinType
        fields='__all__'

class SkinTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = SkinType
        fields='__all__'


class SkinTypeDetailForm(forms.ModelForm):
    class Meta:
        model = SkinType
        fields='__all__'