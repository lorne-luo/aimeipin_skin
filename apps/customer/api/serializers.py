from rest_framework import serializers
from core.api.serializers import BaseSerializer
from ..models import Customer


# Serializer for customer
class CustomerSerializer(BaseSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['name', 'sex', 'age', 'mobile', 'weixin_id', 'remark']
        read_only_fields = ['id']
