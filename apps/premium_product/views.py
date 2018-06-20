from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.edit import ProcessFormView, FormView
from pyexcel_xls import get_data

from apps.premium_product.forms import PremiumProductFitFormSet, PremiumProductImportForm
from core.django.views import CommonContextMixin
from .models import PremiumProduct, PremiumProductFit
from ..brand.models import Brand
from . import forms


class PremiumProductListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    model = PremiumProduct
    template_name_suffix = '_list'

    def get_context_data(self, **kwargs):
        context = super(PremiumProductListView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'id']
        context['brands'] = Brand.objects.all()
        return context


class PremiumProductAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    model = PremiumProduct
    form_class = forms.PremiumProductAddForm
    template_name = 'premium_product/premiumproduct_form.html'

    def get_context_data(self, **kwargs):
        context = super(PremiumProductAddView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'id']

        if self.request.POST:
            context['premiumproductfit_formset'] = PremiumProductFitFormSet(self.request.POST, self.request.FILES,
                                                                            prefix='premiumproductfit_formset',
                                                                            instance=self.object)
        else:
            context['premiumproductfit_formset'] = PremiumProductFitFormSet(prefix='premiumproductfit_formset',
                                                                            instance=self.object)

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        context = self.get_context_data()

        premiumproductfit_formset = context['premiumproductfit_formset']
        premiumproductfit_formset.instance = form.instance
        if premiumproductfit_formset.is_valid():
            premiumproductfit_formset.save()

        return super(PremiumProductAddView, self).form_valid(form)


class PremiumProductUpdateView(PremiumProductAddView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return ProcessFormView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return ProcessFormView.post(self, request, *args, **kwargs)


class PremiumProductDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = PremiumProduct
    # template_name_suffix = '_form'
    fields = ['name_en', 'name_cn', 'pic', 'brand']


class PremiumProductImportView(FormView):
    form_class = PremiumProductImportForm
    template_name = 'premium_product/premiumproduct_import.html'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('premium_product:premiumproduct-list')

    def form_valid(self, form):
        file = form.cleaned_data.get('file')
        file_ext = file.name.split('.')[-1]
        data = get_data(file, file_ext)

        current_row = None
        try:
            for table_name, table in data.items():
                for row in table[1:]:
                    current_row = row
                    self.process_row(row)

        except Exception as e:
            messages.error(self.request, '导入失败: %s, %s' % (current_row, e))
            return super(PremiumProductImportView, self).form_invalid(form)

        messages.info(self.request, '导入成功')
        return super(PremiumProductImportView, self).form_valid(form)

    def process_row(self, row):
        if not row or all([not row[0], not row[1], not row[3], not row[4]]):
            return

        if row[0] == '油性':
            skintype = '油性肌肤'
        elif row[0] == '干性':
            skintype = '干性肌肤'
        else:
            skintype = None
        purpose = row[1]
        category = row[2]
        name_cn = row[3]
        pic = 'premiumproduct/%s.jpg' % row[4] if '.' not in row[4] else row[4]

        product, created = PremiumProduct.objects.get_or_create(name_cn=name_cn)
        product.pic = pic
        product.save()

        if all([not skintype, not purpose, not category]):
            return
        if not product.has_combine(skintype, purpose, category):
            PremiumProductFit.objects.get_or_create(product=product, skin_type=skintype, purpose=purpose,
                                                    category=category)
