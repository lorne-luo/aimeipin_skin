from rest_framework import serializers

from core.api.serializers import BaseSerializer
from ..models import WxUser


# Serializer for customer
class WxUserSerializer(BaseSerializer):
    sex_display = serializers.SerializerMethodField()

    class Meta:
        model = WxUser
        fields = ['id', 'detail_url'] + \
                 ['weixin_id', 'is_subscribe', 'nickname', 'openid', 'sex', 'province', 'city',
                  'country', 'headimg_url', 'created_at', 'sex_display']

        read_only_fields = ['id']

    def get_sex_display(self, obj):
        if obj.sex == '1':
            return '男'
        elif obj.sex == '2':
            return '女'
        else:
            return '未知'
