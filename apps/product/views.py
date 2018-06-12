from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.edit import ProcessFormView

from apps.product.forms import ProductAnalysisFormSet  # ,ProductIngredientFormSet
from core.django.views import CommonContextMixin
from .models import Product, Brand
from . import forms


class ProductListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    model = Product
    template_name_suffix = '_list'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand']
        context['table_fields'] = ['pic', 'link', 'brand']
        context['brands'] = Brand.objects.all()
        return context


class ProductAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    model = Product
    form_class = forms.ProductAddForm
    template_name = 'product/product_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductAddView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'id']

        if self.request.POST:
            context['productanalysis_formset'] = ProductAnalysisFormSet(self.request.POST, self.request.FILES,
                                                                        prefix='productanalysis_formset',
                                                                        instance=self.object)
        else:
            context['productanalysis_formset'] = ProductAnalysisFormSet(prefix='productanalysis_formset',
                                                                        instance=self.object)

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        context = self.get_context_data()

        productanalysis_formset = context['productanalysis_formset']
        productanalysis_formset.instance = form.instance
        if productanalysis_formset.is_valid():
            productanalysis_formset.save()
        else:
            messages.error(self.request, str(productanalysis_formset.errors))

        return super(ProductAddView, self).form_valid(form)


class ProductUpdateView(ProductAddView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return ProcessFormView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return ProcessFormView.post(self, request, *args, **kwargs)


class ProductDetailView(CommonContextMixin, UpdateView):
    model = Product
    # template_name_suffix = '_form'
    fields = ['name_en', 'name_cn', 'pic', 'brand', 'avg_sell_price']
