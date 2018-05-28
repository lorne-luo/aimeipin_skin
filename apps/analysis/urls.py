from django.conf.urls import url
from . import views

# urls for word
urlpatterns = [
    url(r'^word/add/$', views.WordAddView.as_view(), name='word-add'),
    url(r'^word/list/$', views.WordListView.as_view(), name='word-list'),
    url(r'^word/(?P<pk>\d+)/$', views.WordDetailView.as_view(), name='word-detail'),
    url(r'^word/(?P<pk>\d+)/edit/$', views.WordUpdateView.as_view(), name='word-update'),

    url(r'^skintype/add/$', views.SkinTypeAddView.as_view(), name='skintype-add'),
    url(r'^skintype/list/$', views.SkinTypeListView.as_view(), name='skintype-list'),
    url(r'^skintype/(?P<pk>\d+)/$', views.SkinTypeDetailView.as_view(), name='skintype-detail'),
    url(r'^skintype/(?P<pk>\d+)/edit/$', views.SkinTypeUpdateView.as_view(), name='skintype-update'),
]
