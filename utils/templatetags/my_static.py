import time
from django import template
from django.conf import settings
from django.templatetags.static import StaticNode

register = template.Library()


class VersionStaticNode(StaticNode):
    def render(self, context):
        url = super(VersionStaticNode, self).render(context)
        return '%s?v=%s' % (url, settings.VERSION)


@register.tag('version_static')
def static_with_version(parser, token):
    """
        {% static "myapp/css/base.css" %}
        /myapp/css/base.css?v=123124124
    """
    return VersionStaticNode.handle_token(parser, token)


class UncachedStaticNode(StaticNode):
    def render(self, context):
        url = super(UncachedStaticNode, self).render(context)
        timestamp = int(time.time())
        return '%s?v=%s' % (url, timestamp)


@register.tag('uncached_static')
def uncached_static(parser, token):
    """
        {% static "myapp/css/base.css" %}
        /myapp/css/base.css?v=123124124
    """
    return UncachedStaticNode.handle_token(parser, token)
