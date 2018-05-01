# coding=utf-8
from braces.views import MultiplePermissionsRequiredMixin, SuperuserRequiredMixin, LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.views.generic import TemplateView

from core.django.permission import SellerOwnerOrSuperuserRequiredMixin
from core.django.views import CommonContextMixin


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'
