from django.urls import reverse
from rest_framework import serializers

from core.api.serializers import BaseSerializer
from ..models import Answer, InviteCode


class AnswerSerializer(BaseSerializer):
    """ Serializer for Answer """
    survey_url = serializers.SerializerMethodField()
    report_add_url = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    qrcode_url = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['city', 'name', 'sex', 'portrait', 'portrait_part', 'cosmetics', 'birth', 'height', 'weight', 'job',
                  'monthly_income', 'weixin_id', 'mobile', 'is_changeable', 'status', 'get_status_display',
                  'survey_url', 'report_add_url', 'age', 'qrcode_url', 'purpose', 'level']
        read_only_fields = ['id']

    def get_age(self, obj):
        return obj.age

    def get_qrcode_url(self, obj):
        return obj.get_qrcode_url()

    def get_survey_url(self, obj):
        if obj.uuid:
            return reverse('survey:answer', args=[obj.uuid])
        return ''

    def get_report_add_url(self, obj):
        return reverse('report:report-add', args=[obj.id])


class InviteCodeSerializer(BaseSerializer):
    """ Serializer for InviteCode """
    invite_url = serializers.SerializerMethodField()

    class Meta:
        model = InviteCode
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['uuid', 'name', 'purpose', 'expiry_at', 'invite_url', 'qrcode_url']
        read_only_fields = ['id']

    def get_invite_url(self, obj):
        return obj.url
