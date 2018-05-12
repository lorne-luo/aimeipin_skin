from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

# urls for word
urlpatterns = [
    url(r'^word/add/$', login_required(views.WordAddView.as_view()), name='word-add'),
    url(r'^word/list/$', login_required(views.WordListView.as_view()), name='word-list'),
    url(r'^word/(?P<pk>\d+)/$', views.WordDetailView.as_view(), name='word-detail'),
    url(r'^word/(?P<pk>\d+)/edit/$', login_required(views.WordUpdateView.as_view()), name='word-update'),
]
