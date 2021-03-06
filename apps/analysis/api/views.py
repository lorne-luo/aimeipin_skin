import logging

from braces.views import SuperuserRequiredMixin
from dal import autocomplete
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from core.api.filters import PinyinSearchFilter
from core.api.permission import AdminOnlyPermissions
from core.django.autocomplete import HansSelect2ViewMixin
from core.api.views import CommonViewSet
from ..models import Word, SkinType
from . import serializers

log = logging.getLogger(__name__)


class WordViewSet(CommonViewSet):
    """ API views for Word """
    queryset = Word.objects.all()
    serializer_class = serializers.WordSerializer
    filter_fields = ['purpose', 'oily_type__name', 'sensitive_type__name', 'pigment_type__name', 'loose_type__name']
    search_fields = ['purpose', 'oily_type__name', 'sensitive_type__name', 'pigment_type__name', 'loose_type__name']
    permission_classes = (AdminOnlyPermissions,)
    pinyin_search_fields = ['pinyin']  # search only input are all ascii chars
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)


class SkinTypeViewSet(CommonViewSet):
    """ API views for Word """
    queryset = SkinType.objects.all()
    serializer_class = serializers.SkinTypeSerializer
    filter_fields = ['name', 'short_name']
    search_fields = ['name',]
    permission_classes = (AdminOnlyPermissions,)

class WordAutocompleteAPIView(SuperuserRequiredMixin, HansSelect2ViewMixin, autocomplete.Select2QuerySetView):
    model = Word
    paginate_by = 20
