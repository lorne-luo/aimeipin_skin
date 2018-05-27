from django.urls import reverse
from rest_framework import serializers

from core.api.serializers import BaseSerializer
from ..models import Answer, InviteCode


class AnswerSerializer(BaseSerializer):
    """ Serializer for Answer """
    is_changeable_display = serializers.SerializerMethodField()
    survey_url = serializers.SerializerMethodField()
    report_add_url = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['city', 'name', 'sex', 'portrait', 'portrait_part', 'cosmetics', 'birth', 'height', 'weight', 'job',
                  'monthly_income', 'weixin_id', 'mobile', 'is_changeable_display', 'status', 'get_status_display',
                  'survey_url', 'report_add_url']
        read_only_fields = ['id']

    def get_is_changeable_display(self, obj):
        return '是' if obj.is_changeable else '否'

    def get_survey_url(self, obj):
        return reverse('survey:survey-pc', args=[obj.uuid])

    def get_report_add_url(self, obj):
        return reverse('report:report-add', args=[obj.id])


class InviteCodeSerializer(BaseSerializer):
    """ Serializer for InviteCode """
    invite_url = serializers.SerializerMethodField()

    class Meta:
        model = InviteCode
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['uuid', 'name', 'purpose', 'expiry_at', 'invite_url']
        read_only_fields = ['id']

    def get_invite_url(self, obj):
        return reverse('survey:survey-pc', args=[obj.uuid])
