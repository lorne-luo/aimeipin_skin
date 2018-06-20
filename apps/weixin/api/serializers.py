from core.api.serializers import BaseSerializer
from ..models import WxUser


# Serializer for customer
class WxUserSerializer(BaseSerializer):
    class Meta:
        model = WxUser
        fields = ['id', 'detail_url'] + \
                 ['weixin_id', 'is_subscribe', 'nickname', 'openid', 'sex', 'province', 'city',
                  'country', 'headimg_url', 'created_at']

        read_only_fields = ['id']
