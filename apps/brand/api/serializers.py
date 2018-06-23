from rest_framework import serializers

from apps.premium_product.models import PremiumProduct
from apps.product.models import Product
from core.api.serializers import BaseSerializer
from ..models import Brand


class BrandSerializer(BaseSerializer):
    """ Serializer for Brand """
    product_count = serializers.SerializerMethodField()
    premium_product_count = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['name_en', 'name_cn', 'alias', 'product_count', 'premium_product_count']
        read_only_fields = ['id']

    def get_product_count(self, obj):
        return Product.objects.filter(brand=obj).count()

    def get_premium_product_count(self, obj):
        return PremiumProduct.objects.filter(brand=obj).count()
