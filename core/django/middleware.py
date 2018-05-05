#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.conf import settings
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.utils.deprecation import MiddlewareMixin

__author__ = 'lorne'


class ProfileAuthenticationMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        super(ProfileAuthenticationMiddleware, self).process_request(request)
        profile = getattr(request.user, 'profile', None)
        setattr(request, 'profile', profile)


class TemplateContextMiddleware(MiddlewareMixin):
    """ common template context """

    def process_template_response(self, request, response):
        response.context_data['page_system_name'] = settings.SITE_NAME
        return response
