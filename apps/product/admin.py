from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_cn','name_en')
    ordering = ['brand']
    search_fields = ('name_en', 'name_cn')


admin.site.register(Product, ProductAdmin)
