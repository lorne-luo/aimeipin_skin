from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.edit import ProcessFormView

from apps.premium_product.forms import PremiumProductFitFormSet
from core.django.views import CommonContextMixin
from .models import PremiumProduct
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
