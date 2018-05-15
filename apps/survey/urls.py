from django.conf.urls import url
from . import views

# urls for answer
urlpatterns = [
    url(r'^answer/add/$', views.AnswerAddView.as_view(), name='answer-add'),
    url(r'^answer/list/$', views.AnswerListView.as_view(), name='answer-list'),
    url(r'^answer/(?P<pk>\d+)/$', views.AnswerDetailView.as_view(), name='answer-detail'),
    url(r'^answer/(?P<pk>\d+)/edit/$', views.AnswerUpdateView.as_view(), name='answer-update'),
]
