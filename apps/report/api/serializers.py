from django.urls import reverse
from rest_framework import serializers
from core.api.serializers import BaseSerializer
from ..models import Report


class ReportSerializer(BaseSerializer):
    """ Serializer for Report """
    answer_display = serializers.SerializerMethodField()
    answer_url = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['answer', 'purpose', 'level', 'answer_display', 'answer_url', 'modified_at', 'created_at', 'pdf',
                  'is_delivered']
        read_only_fields = ['id']

    def get_answer_display(self, obj):
        return str(obj.answer) if obj.answer else ''

    def get_answer_url(self, obj):
        return reverse('survey:answer-detail', args=[obj.id])

    def get_download_url(self, obj):
        return reverse('report:report-download', args=[obj.id])
