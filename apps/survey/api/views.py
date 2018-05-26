import logging
from core.api.views import CommonViewSet
from ..models import Answer, InviteCode
from . import serializers

log = logging.getLogger(__name__)


class AnswerViewSet(CommonViewSet):
    """ API views for Answer """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    filter_fields = ['name', 'sex']
    search_fields = ['name']


class InviteCodeViewSet(CommonViewSet):
    """ API views for InviteCode """
    queryset = InviteCode.objects.all()
    serializer_class = serializers.InviteCodeSerializer
    filter_fields = ['id'] + ['uuid', 'name']
    search_fields = ['uuid', 'name']
    ordering_fields = ['id'] + ['uuid', 'name']
