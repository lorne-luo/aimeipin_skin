import logging
from core.api.views import CommonViewSet
from ..models import Report
from . import serializers

log = logging.getLogger(__name__)


class ReportViewSet(CommonViewSet):
    """ API views for Report """
    queryset = Report.objects.all()
    serializer_class = serializers.ReportSerializer
    filter_fields = ['purpose', 'level']
    search_fields = ['answer__name', 'answer__uuid']
