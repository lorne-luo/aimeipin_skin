import os
import base64
from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import StaticNode
from django.contrib.staticfiles import finders

from config import settings
from ..models import Report

register = template.Library()


@register.simple_tag
def report_counter():
    return Report.objects.count()


@register.simple_tag
def base64_static(path):
    """convert relative static url to base64
    Usage::
        <img src="data:image;base64,{% base64_static 'img/img.png' %}" />
    """
    file_path = staticfiles_storage.path(path)

    data_type = 'data:image/png;base64,'

    if path.endswith('.ttf'):
        data_type = 'data:application/x-font-ttf;charset=utf-8;base64,'

    if os.path.exists(file_path):
        with open(file_path, "rb") as file_data:
            encoded_string = base64.b64encode(file_data.read())
            encoded_string = encoded_string.decode("utf-8")
            return data_type + encoded_string
    return ''


class InlineStaticNode(StaticNode):
    def render(self, context):
        path = self.path.resolve(context)
        if settings.DEBUG:
            file_path = finders.find(path)
        else:
            file_path = staticfiles_storage.path(path)

        wrapper = '%s'
        if path.endswith('.css'):
            wrapper = '<style type="text/css">%s</style>'
        elif path.endswith('.js'):
            wrapper = '<script type="text/javascript">%s</script>'

        if os.path.exists(file_path):
            with open(file_path, "rb") as file_data:
                return wrapper % file_data.read().decode("utf-8")
        return ''


@register.tag
def inline_static(parser, token):
    """read content from file and render it as inline, this one can't use `simple_tag` as it always apply autoescape
    Usage::
        <style type="text/css">
            {% inline_static 'css/style.css' %}
        </style>
    """
    return InlineStaticNode.handle_token(parser, token)
