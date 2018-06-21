from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/add/$', views.ProductAddView.as_view(), name="product-add"),
    url(r'^product/$', views.ProductListView.as_view(), name="product-list"),
    url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name="product-detail"),
    url(r'^product/(?P<pk>\d+)/edit/$', views.ProductUpdateView.as_view(), name="product-update"),
    url(r'^product/import/$', views.ProductImportView.as_view(), name="product-import"),
]
