import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from core.api.filters import PinyinSearchFilter
from core.api.views import CommonViewSet
from ..models import Report
from . import serializers

log = logging.getLogger(__name__)


class ReportViewSet(CommonViewSet):
    """ API views for Report """
    queryset = Report.objects.all()
    serializer_class = serializers.ReportSerializer
    filter_fields = ['purpose', 'level']
    search_fields = ['answer__name', 'answer__uuid', 'answer__customer__openid']
    search_id_for_number = True
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)
