from django.http import Http404
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from apps.survey.models import Answer
from core.django.views import CommonContextMixin
from .models import Report
from . import forms


class ReportListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Report """
    model = Report
    template_name_suffix = '_list'  # report/report_list.html

    def get_context_data(self, **kwargs):
        context = super(ReportListView, self).get_context_data(**kwargs)
        context['table_titles'] = [u'目标', u'类别', '']
        context['table_fields'] = ['purpose', 'level', 'id']
        return context


class ReportAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for Report """
    model = Report
    form_class = forms.ReportAddForm
    template_name = 'report/report_add.html'

    def get_initial(self):
        answer_id = self.kwargs.get('answer_id')
        self.answer = Answer.objects.filter(id=answer_id).first()
        if not self.answer:
            raise Http404
        initial = super(ReportAddView, self).get_initial()
        initial.update({
            'answer': self.answer,
        })
        return initial

    def get_context_data(self, **kwargs):
        context = super(ReportAddView, self).get_context_data(**kwargs)
        context.update({
            'answer': self.answer,
        })
        return context

    def form_valid(self, form):
        report = form.save()
        report.generate()
        self.object = report
        return super(ReportAddView, self).form_valid(form)


class ReportUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for Report """
    model = Report
    form_class = forms.ReportUpdateForm
    template_name = 'report/report_form.html'


class ReportDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for Report """
    model = Report
    form_class = forms.ReportDetailForm
    template_name = 'adminlte/common_detail.html'
