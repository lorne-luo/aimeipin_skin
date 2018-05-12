import logging
from dal import autocomplete
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from core.api.filters import PinyinSearchFilter
from core.api.permission import AdminOnlyPermissions
from core.django.autocomplete import HansSelect2ViewMixin
from core.django.permission import SellerRequiredMixin
from core.api.views import CommonViewSet
from ..models import Word
from . import serializers

log = logging.getLogger(__name__)


class WordViewSet(CommonViewSet):
    """ API views for Word """
    queryset = Word.objects.all()
    serializer_class = serializers.WordSerializer
    filter_fields = ['purpose', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type']
    search_fields = ['purpose', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type']
    permission_classes = (AdminOnlyPermissions,)
    pinyin_search_fields = ['pinyin']  # search only input are all ascii chars
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)


class WordAutocompleteAPIView(SellerRequiredMixin, HansSelect2ViewMixin, autocomplete.Select2QuerySetView):
    model = Word
    paginate_by = 20
