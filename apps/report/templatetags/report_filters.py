from __future__ import absolute_import, print_function, unicode_literals
from django import template

from ..models import Report

register = template.Library()


@register.simple_tag
def report_counter():
    return Report.objects.count()
