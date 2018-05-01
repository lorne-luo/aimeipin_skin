# coding=utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from core.api.routers import PostHackedRouter
from . import views


urlpatterns = []

# urls for page
urlpatterns += (
    url(r'^login$', views.wx_login, name='login'),
    url(r'^auth$', views.wx_auth, name='auth'),
    url(r'^index', views.wx_index, name='index'),
    # url(r'^pay_notify', views.wx_pay_notify, name='pay_notify'),
)
