from django.conf.urls import url
from . import views

# urls for Report
urlpatterns = [
    url(r'^report/add/$', views.ReportAddView.as_view(), name='report-add'),
    url(r'^report/list/$', views.ReportListView.as_view(), name='report-list'),
    url(r'^report/(?P<pk>\d+)/$', views.ReportDetailView.as_view(), name='report-detail'),
    url(r'^report/(?P<pk>\d+)/edit/$', views.ReportUpdateView.as_view(), name='report-update'),
]