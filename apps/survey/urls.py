from django.conf.urls import url
from . import views

# urls for answer
urlpatterns = [
    url(r'^answer/add/$', views.AnswerAddView.as_view(), name='answer-add'),
    url(r'^answer/list/$', views.AnswerListView.as_view(), name='answer-list'),
    url(r'^answer/(?P<pk>\d+)/$', views.AnswerDetailView.as_view(), name='answer-detail'),
    url(r'^answer/score/(?P<uuid>\d+)/$', views.AnswerScoreView.as_view(), name='answer-score'),
    url(r'^answer/(?P<pk>\d+)/edit/$', views.AnswerUpdateView.as_view(), name='answer-update'),
    url(r'^pc/(?P<uuid>\w+)/$', views.SurveyFillView.as_view(), name='survey-pc'),
    url(r'^wx/(?P<uuid>\w+)/$', views.SurveyFillView.as_view(), name='survey-wx'),
    url(r'^invitecode/add/$', views.InviteCodeAddView.as_view(), name='invitecode-add'),
    url(r'^invitecode/list/$', views.InviteCodeListView.as_view(), name='invitecode-list'),
    url(r'^invitecode/(?P<pk>\d+)/$', views.InviteCodeDetailView.as_view(), name='invitecode-detail'),
    url(r'^invitecode/(?P<pk>\d+)/edit/$', views.InviteCodeUpdateView.as_view(), name='invitecode-update'),
]
