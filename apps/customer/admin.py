from django.forms import ModelForm
from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_order_link', 'get_primary_address', 'order_count', 'last_order_time')
    list_display_links = ['name', 'get_primary_address']
    search_fields = ('name', 'mobile')
    ordering = ['-last_order_time']

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ['password', 'primary_address']
        self.form = ModelForm

        return super(CustomerAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.exclude = ['password']
        return super(CustomerAdmin, self).change_view(request, object_id, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.save()


admin.site.register(Customer, CustomerAdmin)
