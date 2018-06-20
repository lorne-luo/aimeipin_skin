import logging

from core.api.permission import AdminOnlyPermissions
from core.api.views import CommonViewSet
from ..models import WxUser

from . import serializers

log = logging.getLogger(__name__)


class WxUserViewSet(CommonViewSet):
    """api views for Customer"""
    queryset = WxUser.objects.all()
    serializer_class = serializers.WxUserSerializer
    filter_fields = ['nickname']
    search_fields = ['nickname']
    permission_classes = (AdminOnlyPermissions,)
