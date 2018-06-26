import json
import logging

import os
from PIL import Image
from django.http import Http404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.views import CommonViewSet
from ..models import Answer, InviteCode
from . import serializers

log = logging.getLogger(__name__)


class AnswerViewSet(CommonViewSet):
    """ API views for Answer """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    filter_fields = ['name', 'uuid', 'customer_id']
    search_fields = ['name', 'uuid', 'customer__openid']


class InviteCodeViewSet(CommonViewSet):
    """ API views for InviteCode """
    queryset = InviteCode.objects.all()
    serializer_class = serializers.InviteCodeSerializer
    filter_fields = ['id'] + ['uuid', 'name']
    search_fields = ['uuid', 'name']
    ordering_fields = ['id', 'expiry_at']


class AnswerPicRotateView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        direction = self.request.POST.get('direction', None)
        field_name = self.request.POST.get('field_name', None)
        pk = kwargs.get('pk', None)
        if not all([direction, field_name, pk]):
            return Response({'success': False, 'detail': 'Parameter not complete'})

        answer = Answer.objects.filter(id=pk).first()
        if not answer:
            raise Http404

        field = getattr(answer, field_name)
        if not field or not os.path.exists(field.path):
            raise Http404

        direction = Image.ROTATE_270 if direction == 'right' else Image.ROTATE_90
        with Image.open(field.path) as im:
            im = im.transpose(direction)
            im.save(field.path)
        field.render_variations(True)
        return Response({'success': True})
