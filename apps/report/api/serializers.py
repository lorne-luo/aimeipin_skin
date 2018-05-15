from core.api.serializers import BaseSerializer
from ..models import Report


class ReportSerializer(BaseSerializer):
    """ Serializer for Report """

    class Meta:
        model = Report
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['purpose', 'level']
        read_only_fields = ['id']
