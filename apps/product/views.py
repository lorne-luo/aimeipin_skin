from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.edit import ProcessFormView, FormView
from pyexcel_xls import get_data

from apps.product.forms import ProductAnalysisFormSet, ProductImportForm  # ,ProductIngredientFormSet
from core.django.views import CommonContextMixin
from .models import Product, Brand, ProductIngredient
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
            if self.object:
                context['productanalysis_formset'] = ProductAnalysisFormSet(
                    self.request.POST, self.request.FILES,
                    prefix='productanalysis_formset', instance=self.object,
                    queryset=self.object.productanalysis_set.order_by('oily_type', 'sensitive_type', 'pigment_type',
                                                                      'loose_type'))
            else:
                context['productanalysis_formset'] = ProductAnalysisFormSet(
                    self.request.POST, self.request.FILES,
                    prefix='productanalysis_formset', instance=self.object)
        else:
            if self.object:
                context['productanalysis_formset'] = ProductAnalysisFormSet(
                    prefix='productanalysis_formset', instance=self.object,
                    queryset=self.object.productanalysis_set.order_by('oily_type', 'sensitive_type', 'pigment_type',
                                                                      'loose_type'))
            else:
                context['productanalysis_formset'] = ProductAnalysisFormSet(
                    prefix='productanalysis_formset', instance=self.object)

        return context

    def form_valid(self, form):
        self.object = form.save()

        productanalysis_formset = ProductAnalysisFormSet(self.request.POST, self.request.FILES,
                                                         prefix='productanalysis_formset', instance=self.object)
        productanalysis_formset.instance = self.object

        if productanalysis_formset.is_valid():
            productanalysis_formset.save()
        else:
            messages.error(self.request, str(productanalysis_formset.errors))

        return HttpResponseRedirect(self.get_success_url())


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


class ProductImportView(FormView):
    form_class = ProductImportForm
    template_name = 'product/product_import.html'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('product:product-list')

    def form_valid(self, form):
        product_file = form.cleaned_data.get('product_file')
        current_row = None
        if product_file:
            file_ext = product_file.name.split('.')[-1]
            product_data = get_data(product_file, file_ext.lower())

            try:
                for table_name, table in product_data.items():
                    current_row = None
                    if len(table[0]) != 7 or table[0][0] != '产品拼音首字母':
                        raise ValidationError('Excel文件格式不正确，需包含"产品拼音首字母, 产品名称, 品牌, 英文名, 图片, 别名, 所属分类" 7列.')
                    for row in table[1:]:
                        current_row = row
                        self.process_product(row)
            except Exception as e:
                messages.error(self.request, '导入失败: %s, %s' % (current_row or '', e))
                return super(ProductImportView, self).form_invalid(form)

        component_file = form.cleaned_data.get('component_file')
        if component_file:
            file_ext = component_file.name.split('.')[-1]
            component_data = get_data(component_file, file_ext.lower())
            try:
                for table_name, table in component_data.items():
                    current_row = None
                    if len(table[0]) != 7 or table[0][0] != '产品':
                        raise ValidationError(
                            'Excel文件格式不正确，需包含"产品, 产品成分, 成分是否安全,（1安全、2不安全）, 活性因子（1是、2不是）, 是否导致起痘（1会、2不会）, 成分简介, 成分在产品中的作用" 7列.')
                    for row in table[1:]:
                        current_row = row
                        self.process_component(row)
            except Exception as e:
                messages.error(self.request, '导入失败: %s, %s' % (current_row or '', e))
                return super(ProductImportView, self).form_invalid(form)

        messages.success(self.request, '导入成功.')
        return super(ProductImportView, self).form_valid(form)

    def process_component(self, row):
        # 产品, 产品成分, 成分是否安全,（1安全、2不安全）, 活性因子（1是、2不是）, 是否导致起痘（1会、2不会）, 成分简介, 成分在产品中的作用
        if not row or len(row) < 2 or (not row[0] and not row[1]):
            return

        name_cn = row[0]
        component_name = row[1]
        safe = row[2] or '' if len(row) > 2 else ''
        is_live = row[3] or '' if len(row) > 3 else ''
        is_pox = row[4] or '' if len(row) > 4 else ''
        description = row[5] or '' if len(row) > 5 else ''
        effect = row[6] or '' if len(row) > 6 else ''
        is_live = True if is_live == '1' else False
        is_pox = True if is_pox == '1' else False

        component = ProductIngredient.objects.filter(name=component_name).first()
        if not component:
            component = ProductIngredient(name=component_name)
        component.safe = safe
        component.is_live = is_live
        component.is_pox = is_pox
        component.description = description
        component.effect = effect
        component.save()

        product = Product.objects.filter(name_cn=name_cn).first()
        if product:
            if not product.ingredients.filter(name=component_name).count():
                product.ingredients.add(component)

    def process_product(self, row):
        # 产品拼音首字母, 产品名称, 品牌, 英文名, 图片, 别名, 所属分类
        if not row or len(row) < 2 or not row[1]:
            return

        name_cn = row[1]
        brand_name = row[2] or '' if len(row) > 2 else ''
        name_en = row[3] or '' if len(row) > 3 else ''
        alias = row[5] or '' if len(row) > 5 else ''
        category = row[6] or '' if len(row) > 6 else ''
        if len(row) > 4 and row[4]:
            pic = 'product/%s.jpg' % row[4] if '.' not in row[4] else 'product/%s' % row[4]
        else:
            pic = None

        brand = Brand.objects.filter(Q(name_cn=brand_name) | Q(name_en=brand_name)).first() if brand_name else None
        product, created = Product.objects.get_or_create(name_cn=name_cn)
        product.brand = brand
        product.alias = alias
        product.name_en = name_en
        product.category = category
        product.pic = pic
        product.save()
