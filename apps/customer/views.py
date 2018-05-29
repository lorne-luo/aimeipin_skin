# coding=utf-8
from braces.views import MultiplePermissionsRequiredMixin, SuperuserRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView

from core.django.views import CommonContextMixin
from . import forms
from .models import Customer


# views for Customer

class CustomerListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    model = Customer
    template_name_suffix = '_list'  # customer/customer_list.html


class CustomerAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    model = Customer
    form_class = forms.CustomerAddForm
    template_name = 'customer/customer_add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(CustomerAddView, self).form_valid(form)


class CustomerUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = Customer
    form_class = forms.CustomerUpdateForm
    template_name = 'customer/customer_edit.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)

        context['new_address_forms'] = forms.AnswerInlineForm(prefix='address_set')
        address_forms = forms.AnswerFormSet(queryset=self.object.answer_set.all(), prefix='address_set')
        context['address_forms'] = address_forms

        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # customer address
        address_formset = forms.AnswerFormSet(request.POST, request.FILES, prefix='address_set')
        for form in address_formset:
            form.is_valid()
            if form.instance.address or form.instance.name:
                form.fields['customer'].initial = self.object.id
                form.base_fields['customer'].initial = self.object.id
                form.changed_data.append('customer')
                form.instance.customer_id = self.object.id
            else:
                form._changed_data = []
            if form._errors and 'customer' in form._errors:
                del form._errors['customer']

        if not address_formset.is_valid():
            return HttpResponse(str(address_formset.errors))
        address_formset.save()

        return super(CustomerUpdateView, self).post(request, *args, **kwargs)


class CustomerDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    model = Customer
    form_class = forms.CustomerDetailForm
    template_name = 'adminlte/common_detail.html'
