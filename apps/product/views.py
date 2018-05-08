from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.edit import ProcessFormView

from apps.product.forms import ProductIngredientFormSet
from core.django.views import CommonContextMixin
from .models import Product, Brand
from . import forms


class ProductListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    model = Product
    template_name_suffix = '_list'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['table_titles'] = ['Pic', 'Name', 'Brand', 'Last Price', 'Avg Price', '']
            context['table_fields'] = ['pic', 'link', 'brand', 'last_sell_price', 'avg_sell_price', 'id']
        else:
            context['table_titles'] = ['Pic', 'Name', 'Brand', 'Avg Price']
            context['table_fields'] = ['pic', 'link', 'brand', 'avg_sell_price']
        context['brands'] = Brand.objects.all()
        return context


class ProductAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    model = Product
    form_class = forms.ProductAddForm
    template_name = 'product/product_form.html'
    component_edit_querystring = 'component_edit'

    def get_context_data(self, **kwargs):

        context = super(ProductAddView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'id']
        params = self.request.GET or self.request.POST
        context['component_edit'] = self.component_edit_querystring in params
        if self.request.POST:
            context['productingredient_formset'] = ProductIngredientFormSet(self.request.POST,
                                                                            self.request.FILES,
                                                                            instance=self.object)
        else:
            context['productingredient_formset'] = ProductIngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        context = self.get_context_data()
        productingredient_formset = context['productingredient_formset']
        productingredient_formset.instance = form.instance
        if productingredient_formset.is_valid():
            productingredient_formset.save()
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
