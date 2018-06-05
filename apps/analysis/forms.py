from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Word, SkinType


class WordAddForm(forms.ModelForm):
    class Meta:
        model = Word
        exclude = ['pinyin']

    def __init__(self, *args, **kwargs):
        super(WordAddForm, self).__init__(*args, **kwargs)
        self.fields['oily_type'].queryset = SkinType.objects.filter(dimension='油性or干性')
        self.fields['sensitive_type'].queryset = SkinType.objects.filter(dimension='敏感or耐受')
        self.fields['pigment_type'].queryset = SkinType.objects.filter(dimension='色素or非色素')
        self.fields['loose_type'].queryset = SkinType.objects.filter(dimension='易皱纹or紧致')


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
        fields = '__all__'


class SkinTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = SkinType
        fields = '__all__'


class SkinTypeDetailForm(forms.ModelForm):
    class Meta:
        model = SkinType
        fields = '__all__'
