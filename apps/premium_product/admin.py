from django.contrib import admin
from .models import PremiumProduct


class PremiumProductAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_cn')
    ordering = ['brand']
    search_fields = ('name_en', 'name_cn')


admin.site.register(PremiumProduct, PremiumProductAdmin)
