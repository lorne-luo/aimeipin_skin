from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from core.django.views import CommonContextMixin
from .models import Word
from . import forms


class WordListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Word """
    model = Word
    template_name = 'analysis/word_list.html'

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context['table_titles'] = [u'目标', u'油性or干性', u'敏感or耐受', u'色素or非色素', u'易皱or紧致', '']
        context['table_fields'] = ['purpose', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type', 'id']
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
    template_name = 'adminlte/common_detail_new.html'
