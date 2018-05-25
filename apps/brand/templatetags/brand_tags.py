from django import template
from ..models import Brand

register = template.Library()


@register.simple_tag
def brand_counter():
    return Brand.objects.count()
