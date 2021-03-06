from rest_framework import serializers
from core.api.serializers import BaseSerializer
from ..models import Product


class ProductSerializer(BaseSerializer):
    """Serializer for product"""
    brand_display = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'edit_url', 'detail_url', 'name_en', 'name_cn', 'pic', 'category', 'brand_display', 'thumbnail',
                  'alias']
        read_only_fields = ['id']

    def get_thumbnail(self, obj):
        return obj.pic.thumbnail.url if obj.pic else None

    def get_brand_display(self, obj):
        return str(obj.brand) if obj.brand else ''
