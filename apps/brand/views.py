from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from core.django.views import CommonContextMixin
from .models import Brand
from . import forms


class BrandListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Brand """
    model = Brand
    template_name_suffix = '_list'  # brand/brand_list.html

    def get_context_data(self, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        context['table_titles'] = ['中文名称', '英文名称', u'别名', u'普通产品', u'优选产品''']
        context['table_fields'] = ['name_cn', 'name_en', 'alias', 'product_count', 'premium_product_count', 'id']
        return context


class BrandAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for Brand """
    model = Brand
    form_class = forms.BrandAddForm
    template_name = 'brand/brand_form.html'


class BrandUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for Brand """
    model = Brand
    form_class = forms.BrandUpdateForm
    template_name = 'brand/brand_form.html'


class BrandDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for Brand """
    model = Brand
    form_class = forms.BrandDetailForm
    template_name = 'adminlte/common_detail.html'
