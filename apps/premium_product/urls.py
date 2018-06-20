from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^premium_product/add/$', views.PremiumProductAddView.as_view(), name="premiumproduct-add"),
    url(r'^premium_product/$', views.PremiumProductListView.as_view(), name="premiumproduct-list"),
    url(r'^premium_product/(?P<pk>\d+)/$', views.PremiumProductDetailView.as_view(), name="premiumproduct-detail"),
    url(r'^premium_product/(?P<pk>\d+)/edit/$', views.PremiumProductUpdateView.as_view(), name="premiumproduct-update"),
    url(r'^premium_product/import/$', views.PremiumProductImportView.as_view(), name="premiumproduct-import"),
]
