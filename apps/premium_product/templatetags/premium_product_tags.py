from django import template
from ..models import PremiumProduct

register = template.Library()


@register.simple_tag
def premium_product_counter():
    return PremiumProduct.objects.count()

