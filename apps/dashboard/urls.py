# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.DashboardHomeView.as_view(), name='home'),
]
