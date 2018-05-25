# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django import template

from core.adminlte.templatetags.adminlte_tags import get_attr
from ..models import Answer

register = template.Library()


@register.filter(name='render_products')
def render_products(obj, field_name):
    items = []
    if hasattr(obj, field_name) or '.' in field_name:
        items = get_attr(obj, field_name)
        if hasattr(items, 'through'):
            items = items.all()
        else:
            return ''

    return '\n'.join(['<p>%s</p>' % item for item in items])


@register.simple_tag
def answer_counter():
    return Answer.objects.count()
