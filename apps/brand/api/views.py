import logging

import sys
from django.db.models import Q
from dal import autocomplete
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters

from core.api.filters import PinyinSearchFilter
from core.utils.string import include_non_asc
from core.django.autocomplete import HansSelect2ViewMixin
from core.api.views import CommonViewSet
from ..models import Brand
from . import serializers

log = logging.getLogger(__name__)


class BrandViewSet(CommonViewSet):
    """ API views for Brand """
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    filter_fields = ['name_en', 'name_cn']
    search_fields = ['name_cn']
    pinyin_search_fields = ['name_en', 'pinyin']  # search only input are all ascii chars
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)


class BrandAutocompleteAPIView(HansSelect2ViewMixin, autocomplete.Select2QuerySetView):
    model = Brand
    paginate_by = sys.maxsize  # no pagination

    # create_field = 'name_cn'
    #
    # def create_object(self, text):
    #     if include_non_asc(text):
    #         return self.get_queryset().create(**{'name_cn': text})
    #     else:
    #         return self.get_queryset().create(**{'name_en': text})

    def get_queryset(self):
        qs = Brand.objects.all()

        if include_non_asc(self.q):
            qs = qs.filter(name_cn__icontains=self.q)
        else:
            # all ascii, number and letter
            key = self.q.lower()
            qs = qs.filter(
                Q(pinyin__icontains=key) | Q(name_en__icontains=key))
        return qs

    def get_results(self, context):
        return [
            {
                'id': self.get_result_value(result),
                'text': self.get_result_label(result),
                'image': result.logo.url if result.logo else None,
            } for result in context['object_list']
        ]
