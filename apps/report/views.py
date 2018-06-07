from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin
from weasyprint import HTML, CSS

from apps.survey.forms import AnswerProductAnalysisFormSet
from core.django.utils.pdf import PdfGenerateBaseView
from .forms import PremiumProductFormSet
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
            'level': self.answer.level,
            'purpose': self.answer.purpose,
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
        return HttpResponseRedirect(self.get_success_url())


class ReportUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for Report """
    model = Report
    form_class = forms.ReportUpdateForm
    template_name = 'report/report_form_%s.html'

    def get_template_names(self):
        if self.object.level in ['9.9', '98']:
            return self.template_name % self.object.level
        return 'report/report_form_9.9.html'

    def get_productanalysis_initial(self):
        initial = []
        if not self.object.answer:
            return initial

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products1.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products2.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products3.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products4.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products5.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products6.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products7.all()]

        initial += [{'id': cosmetic.id, 'product': cosmetic.product_id,
                     'name': cosmetic.name or str(cosmetic.product),
                     'analysis': cosmetic.analysis}
                    for cosmetic in self.object.answer.cosmetic_products8.all()]

        return initial

    def get_context_data(self, **kwargs):
        context = super(ReportUpdateView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            if self.object:
                day_products_formset = PremiumProductFormSet(
                    queryset=self.object.reportpremiumproduct_set.all().filter(type='日间'),
                    instance=self.object,
                    prefix='day_products_formset')
                night_products_formset = PremiumProductFormSet(
                    queryset=self.object.reportpremiumproduct_set.all().filter(type='夜间'),
                    instance=self.object,
                    prefix='night_products_formset')
                mask_products_formset = PremiumProductFormSet(
                    queryset=self.object.reportpremiumproduct_set.all().filter(type='面膜'),
                    instance=self.object,
                    prefix='mask_products_formset')
            else:
                day_products_formset = PremiumProductFormSet(instance=self.object, prefix='day_products_formset')
                night_products_formset = PremiumProductFormSet(instance=self.object, prefix='night_products_formset')
                mask_products_formset = PremiumProductFormSet(instance=self.object, prefix='mask_products_formset')

            answerproductanalysis_formset = AnswerProductAnalysisFormSet(prefix='answerproductanalysis_formset',
                                                                         initial=self.get_productanalysis_initial())
        else:
            day_products_formset = PremiumProductFormSet(self.request.POST, self.request.FILES,
                                                         instance=self.object, prefix='day_products_formset')
            night_products_formset = PremiumProductFormSet(self.request.POST, self.request.FILES,
                                                           instance=self.object, prefix='night_products_formset')
            mask_products_formset = PremiumProductFormSet(self.request.POST, self.request.FILES,
                                                          instance=self.object, prefix='mask_products_formset')
            answerproductanalysis_formset = AnswerProductAnalysisFormSet(self.request.POST, self.request.FILES,
                                                                         instance=self.object.answer,
                                                                         prefix='answerproductanalysis_formset')
        context.update({
            'day_products_formset': day_products_formset,
            'night_products_formset': night_products_formset,
            'mask_products_formset': mask_products_formset,
            'answerproductanalysis_formset': answerproductanalysis_formset,
        })
        return context

    def process_formset(self, prefix):
        products_formset = PremiumProductFormSet(self.request.POST, self.request.FILES,
                                                 prefix=prefix, instance=self.object)
        products_formset.instance = self.object
        if products_formset.is_valid():
            products_formset.save()
            return True
        else:
            messages.error(self.request, str(products_formset.errors))
            return False

    def form_valid(self, form):
        result = super(ReportUpdateView, self).form_valid(form)

        if not all([self.process_formset('day_products_formset'),
                    self.process_formset('night_products_formset'),
                    self.process_formset('mask_products_formset')]):
            return self.form_invalid(form)
        return result


class ReportDetailView(CommonContextMixin, UpdateView):
    """ Detail views for Report """
    model = Report
    form_class = forms.ReportDetailForm
    template_name = 'report/report_detail_%s.html'
    http_method_names = ['get']

    def get_template_names(self):
        if self.object.level in ['9.9', '98']:
            return self.template_name % self.object.level
        return 'report/report_form_9.9.html'

    def get_context_data(self, **kwargs):
        return SingleObjectMixin.get_context_data(self, **kwargs)


class ReportDisplayView(ReportDetailView):
    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        obj = Report.objects.filter(answer__uuid=uuid).first()
        if obj:
            return obj
        else:
            raise Http404


class ReportDownloadView(PdfGenerateBaseView, ReportDetailView):  # PdfGenerateBaseView
    """ PDF Download views for Report """
    model = Report
    form_class = forms.ReportDetailForm
    template_name = 'report/report_download_%s.html'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # return super(ReportDownloadView, self).get(request, *args, **kwargs)
        context = self.get_context_data(**kwargs)
        pdf = self.render_to_pdf(self.get_template_names(), context)
        response = HttpResponse(pdf, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=Action28_NO.%s.pdf' % self.object.answer.uuid
        response['Content-Length'] = len(pdf.content)
        return response


class ReportDownloadView2(ReportDetailView):
    model = Report
    form_class = forms.ReportDetailForm
    template_name = 'report/report_download2_%s.html'
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # return super(ReportDownloadView, self).get(request, *args, **kwargs)
        context = self.get_context_data(**kwargs)
        template_name = self.get_template_names()
        template = get_template(template_name)
        html = template.render(context)
        return HttpResponse(html)
        pdf = HTML(string=html).write_pdf(stylesheets=[CSS(string='@page { size: A4; margin: 2cm };'
                                                                  '* { float: none !important };'
                                                                  '@media print { nav { display: none } }')])
        response = HttpResponse(pdf, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=Action28_NO.%s.pdf' % self.object.answer.uuid
        response['Content-Length'] = len(pdf)
        return response
