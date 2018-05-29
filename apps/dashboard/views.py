# coding=utf-8
from braces.views import MultiplePermissionsRequiredMixin, SuperuserRequiredMixin, LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.views.generic import TemplateView


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'
