from rest_framework import serializers

from core.api.serializers import BaseSerializer
from ..models import Answer, InviteCode


class AnswerSerializer(BaseSerializer):
    """ Serializer for Answer """
    is_changeable_display = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['city', 'name', 'sex', 'portrait', 'portrait_part', 'cosmetics', 'birth', 'height', 'weight', 'job',
                  'monthly_income', 'weixin_id', 'mobile', 'is_changeable_display', 'status', 'get_status_display']
        read_only_fields = ['id']

    def get_is_changeable_display(self, obj):
        return '是' if obj.is_changeable else '否'


class InviteCodeSerializer(BaseSerializer):
    """ Serializer for InviteCode """

    class Meta:
        model = InviteCode
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['code', 'name', 'expiry_at']
        read_only_fields = ['id']
