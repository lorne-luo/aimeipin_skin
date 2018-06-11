from django.conf.urls import url
from . import views

# urls for Report
urlpatterns = [
    url(r'^report/add/(?P<answer_id>\d+)/$', views.ReportAddView.as_view(), name='report-add'),
    url(r'^report/list/$', views.ReportListView.as_view(), name='report-list'),
    url(r'^report/(?P<pk>\d+)/$', views.ReportDetailView.as_view(), name='report-detail'),
    url(r'^(?P<uuid>\w+)/$', views.ReportDisplayView.as_view(), name='report-display'),
    url(r'^report/(?P<pk>\d+)/download2/$', views.ReportDownloadView.as_view(), name='report-download2'),
    url(r'^report/(?P<pk>\d+)/download/$', views.ReportDownloadView2.as_view(), name='report-download'),
    url(r'^report/(?P<pk>\d+)/edit/$', views.ReportUpdateView.as_view(), name='report-update'),
]
