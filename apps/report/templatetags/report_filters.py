import os
import base64
from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import StaticNode
from django.contrib.staticfiles import finders

from ..models import Report

register = template.Library()


@register.simple_tag
def report_counter():
    return Report.objects.count()


@register.filter(name='file_to_base64')
def file_to_base64(file_instance):
    """convert image field into base64
    Usage::
        <img src="data:image;base64,{{ object.image|file_to_base64 }}"/>
    """
    if file_instance and os.path.exists(file_instance.path):
        file_instance = file_instance.file.file
        encoded_string = base64.b64encode(file_instance.read())
        encoded_string = encoded_string.decode("utf-8")
        return 'data:image;base64,' + encoded_string
    return ''


@register.simple_tag
def base64_static(path):
    """convert relative static url to base64
    Usage::
        <img src="data:image;base64,{% base64_static 'img/img.png' %}" />
    """
    file_path = staticfiles_storage.path(path)

    data_type = 'data:image;base64,'

    if path.lower().endswith('.ttf'):
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


@register.filter
def break_line(text):
    text = text or ''
    return text.replace('\r\n', '<br/>').replace('\n', '<br/>')
