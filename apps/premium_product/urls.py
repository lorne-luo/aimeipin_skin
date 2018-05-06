from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^premium_product/add/$', login_required(views.PremiumProductAddView.as_view()), name="premiumproduct-add"),
    url(r'^premium_product/$', views.PremiumProductListView.as_view(), name="premiumproduct-list"),
    url(r'^premium_product/(?P<pk>\d+)/$', views.PremiumProductDetailView.as_view(), name="premiumproduct-detail"),
    url(r'^premium_product/(?P<pk>\d+)/edit/$', login_required(views.PremiumProductUpdateView.as_view()), name="premiumproduct-update"),
]
