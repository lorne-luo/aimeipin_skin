from django.forms import ModelForm
from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ('name', 'name_py')
    ordering = ['-created_at']


admin.site.register(Customer, CustomerAdmin)
