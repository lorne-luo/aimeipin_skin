from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

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
    template_name = 'adminlte/common_form.html'

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


class PremiumProductUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = PremiumProduct
    form_class = forms.PremiumProductAddForm
    template_name = 'adminlte/common_form.html'


class PremiumProductDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = PremiumProduct
    # template_name_suffix = '_form'
    fields = ['name_en', 'name_cn', 'pic', 'brand']
