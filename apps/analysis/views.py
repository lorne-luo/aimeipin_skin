from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from core.django.views import CommonContextMixin
from .models import Word, SkinType
from . import forms


class WordListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Word """
    model = Word
    template_name = 'analysis/word_list.html'

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context['table_titles'] = [u'目标', u'油性or干性', u'敏感or耐受', u'色素or非色素', u'易皱or紧致', '']
        context['table_fields'] = ['purpose', 'oily_type_display', 'sensitive_type_display', 'pigment_type_display',
                                   'loose_type_display', 'id']
        return context


class WordAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for Word """
    model = Word
    form_class = forms.WordAddForm
    template_name = 'analysis/word_form.html'


class WordUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for Word """
    model = Word
    form_class = forms.WordUpdateForm
    template_name = 'analysis/word_form.html'


class WordDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for Word """
    model = Word
    form_class = forms.WordDetailForm
    template_name = 'adminlte/common_detail.html'


class SkinTypeListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for SkinType """
    model = SkinType
    template_name = 'analysis/skintype_list.html'

    def get_context_data(self, **kwargs):
        context = super(SkinTypeListView, self).get_context_data(**kwargs)
        context['table_titles'] = [u'维度', u'名称', u'简称', u'备注', '']
        context['table_fields'] = ['dimension', 'name', 'short_name', 'description', 'id']
        return context


class SkinTypeAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for SkinType """
    model = SkinType
    form_class = forms.SkinTypeAddForm
    template_name = 'analysis/skintype_form.html'


class SkinTypeUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for SkinType """
    model = SkinType
    form_class = forms.SkinTypeUpdateForm
    template_name = 'analysis/skintype_form.html'


class SkinTypeDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for SkinType """
    model = SkinType
    form_class = forms.SkinTypeDetailForm
    template_name = 'adminlte/common_detail.html'
