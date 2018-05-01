# coding=utf-8
from django.conf.urls import url
from . import views

# urls for customer
urlpatterns = [
    url(r'^customer/add/$', views.CustomerAddView.as_view(), name='customer-add'),
    url(r'^customer/list/$', views.CustomerListView.as_view(), name='customer-list'),
    url(r'^customer/(?P<pk>\d+)/$', views.CustomerDetailView.as_view(), name='customer-detail'),
    url(r'^customer/(?P<pk>\d+)/edit/$', views.CustomerUpdateView.as_view(), name='customer-update'),
]
