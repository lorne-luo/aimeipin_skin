from django.views.generic import ListView, CreateView, UpdateView
from braces.views import MultiplePermissionsRequiredMixin

from core.django.permission import SellerOwnerOrSuperuserRequiredMixin
from core.django.views import CommonContextMixin
from .models import PremiumProduct
from ..brand.models import Brand
from . import forms


class PremiumProductListView(CommonContextMixin, ListView):
    model = PremiumProduct
    template_name_suffix = '_list'

    def get_context_data(self, **kwargs):
        context = super(PremiumProductListView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'id']
        context['brands'] = Brand.objects.all()
        return context


class PremiumProductAddView(MultiplePermissionsRequiredMixin, CommonContextMixin, CreateView):
    model = PremiumProduct
    form_class = forms.PremiumProductAddForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("premium_product.add_premium_product",)
    }

    def get_context_data(self, **kwargs):
        context = super(PremiumProductAddView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'id']
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if not self.request.user.is_superuser:
            self.object.seller = self.request.profile
        return super(PremiumProductAddView, self).form_valid(form)


class PremiumProductUpdateView(SellerOwnerOrSuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = PremiumProduct
    form_class = forms.PremiumProductAddForm
    template_name = 'adminlte/common_form.html'


class PremiumProductDetailView(CommonContextMixin, UpdateView):
    model = PremiumProduct
    # template_name_suffix = '_form'
    fields = ['name_en', 'name_cn', 'pic', 'brand']
