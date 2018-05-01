from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

# urls for brand
urlpatterns = [
    url(r'^brand/add/$', login_required(views.BrandAddView.as_view()), name='brand-add'),
    url(r'^brand/list/$', login_required(views.BrandListView.as_view()), name='brand-list'),
    url(r'^brand/(?P<pk>\d+)/$', views.BrandDetailView.as_view(), name='brand-detail'),
    url(r'^brand/(?P<pk>\d+)/edit/$', login_required(views.BrandUpdateView.as_view()), name='brand-update'),
]
