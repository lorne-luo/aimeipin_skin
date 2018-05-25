from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
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
    template_name = 'report/report_form.html'


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
