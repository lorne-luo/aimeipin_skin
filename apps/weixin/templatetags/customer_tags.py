from django import template
from ..models import WxUser

register = template.Library()


@register.simple_tag
def customer_counter():
    return WxUser.objects.count()


