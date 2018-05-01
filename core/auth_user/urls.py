from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^login/', views.member_login, name='login'),
    url(r'^logout/', views.member_logout, name='logout'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
)
