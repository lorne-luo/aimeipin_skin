from django.http import Http404
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from apps.premium_product.forms import PremiumProductFormSet
from apps.premium_product.models import PremiumProduct
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
        context['table_titles'] = ['问卷', u'目标', u'类别', '']
        context['table_fields'] = ['answer', 'purpose', 'level', 'id']
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
        answer = form.instance.answer
        purpose = form.instance.purpose
        level = form.instance.level
        report = answer.generate_report(purpose, level)

        self.object = report
        return super(ReportAddView, self).form_valid(form)


class ReportUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for Report """
    model = Report
    form_class = forms.ReportUpdateForm
    template_name = 'report/report_form.html'

    def get_context_data(self, **kwargs):
        context = super(ReportUpdateView, self).get_context_data(**kwargs)
        if self.object:
            day_products_formset = PremiumProductFormSet(initial=self.object.day_products.all(),
                                                         prefix='day_products_formset')
            night_products_formset = PremiumProductFormSet(initial=self.object.night_products.all(),
                                                           prefix='night_products_formset')
            mask_products_formset = PremiumProductFormSet(initial=self.object.mask_products.all(),
                                                          prefix='mask_products_formset')
        else:
            day_products_formset = PremiumProductFormSet(prefix='day_products_formset')
            night_products_formset = PremiumProductFormSet(prefix='night_products_formset')
            mask_products_formset = PremiumProductFormSet(prefix='mask_products_formset')

        context.update({
            'day_products_formset': day_products_formset,
            'night_products_formset': night_products_formset,
            'mask_products_formset': mask_products_formset,
        })
        return context

    def process_formset(self, product_set, prefix):
        products_formset = PremiumProductFormSet(data=self.request.POST, prefix=prefix)
        ids = []
        for p in products_formset:
            if p.is_valid():
                p.save()
                product_set.add(p)
                ids.append(p.id)
        deletes = product_set.all().exclude(id__in=ids)
        deletes.delete()

    def form_valid(self, form):
        self.object = form.save()
        self.process_formset(self.object.day_products, 'day_products_formset')
        self.process_formset(self.object.night_products, 'night_products_formset')
        self.process_formset(self.object.mask_products, 'mask_products_formset')
        return super(ReportUpdateView, self).form_valid(form)


class ReportDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for Report """
    model = Report
    form_class = forms.ReportDetailForm
    template_name = 'adminlte/common_detail.html'
