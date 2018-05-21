from core.api.serializers import BaseSerializer
from ..models import Answer, InviteCode


class AnswerSerializer(BaseSerializer):
    """ Serializer for Answer """

    class Meta:
        model = Answer
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['city', 'name', 'sex', 'portrait', 'portrait_part', 'cosmetics', 'birth', 'height', 'width', 'job',
                  'monthly_income', 'weixin_id', 'mobile']
        read_only_fields = ['id']


class InviteCodeSerializer(BaseSerializer):
    """ Serializer for InviteCode """

    class Meta:
        model = InviteCode
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['code', 'name', 'expiry_at']
        read_only_fields = ['id']
