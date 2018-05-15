import logging
from core.api.views import CommonViewSet
from ..models import Answer
from . import serializers

log = logging.getLogger(__name__)


class AnswerViewSet(CommonViewSet):
    """ API views for Answer """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    filter_fields = ['name', 'sex']
    search_fields = ['name']
