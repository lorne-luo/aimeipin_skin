import logging

import sys
from django.db.models import Q
from dal import autocomplete
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters

from core.api.filters import PinyinSearchFilter
from core.utils.string import include_non_asc
from core.django.autocomplete import HansSelect2ViewMixin
from braces.views import SuperuserRequiredMixin
from core.api.views import CommonViewSet
from ..models import PremiumProduct
from . import serializers

log = logging.getLogger(__name__)


class PremiumProductViewSet(CommonViewSet):
    """ API views for Product """
    queryset = PremiumProduct.objects.all()
    serializer_class = serializers.PremiumProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_fields = ['name_en', 'name_cn', 'brand__name_cn', 'brand__name_en']
    search_fields = ['name_cn', 'brand__name_cn', 'alias']
    pinyin_search_fields = ['name_cn', 'name_en', 'brand__name_en', 'pinyin']  # search only input are all ascii chars
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)


class PremiumProductAutocompleteAPIView(SuperuserRequiredMixin, HansSelect2ViewMixin, autocomplete.Select2QuerySetView):
    model = PremiumProduct
    paginate_by = 20
    create_field = 'name_cn'

    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'seller': self.request.profile})

    def get_queryset(self):
        purpose = self.forwarded.get('purpose')
        skin_type = self.forwarded.get('skin_type')
        category = self.forwarded.get('category')

        if purpose or skin_type or category:
            data = {}
            if purpose:
                data.update({'purpose': purpose})
            if skin_type:
                data.update({'skin_type': skin_type})
            if category:
                data.update({'category': category})
            qs = PremiumProduct.search_fit(**data)
        else:
            qs = PremiumProduct.objects.all()

        qs = qs.order_by('brand__name_en', 'name_cn')

        if include_non_asc(self.q):
            qs = qs.filter(
                Q(name_cn__icontains=self.q) | Q(brand__name_cn__icontains=self.q) | Q(alias__icontains=self.q))
        else:
            # all ascii, number and letter
            key = self.q.lower()
            qs = qs.filter(
                Q(pinyin__contains=key) | Q(name_cn__icontains=key) | Q(name_en__icontains=key) | Q(
                    brand__name_en__icontains=key))
        return qs


class PremiumProductSearchAPIView(PremiumProductAutocompleteAPIView):
    paginate_by = sys.maxsize
    create_field = None

    def get_results(self, context):
        return [
            {
                'id': self.get_result_value(result),
                'text': self.get_result_label(result),
                'image': result.pic.thumbnail.url if result.pic else None,
            } for result in context['object_list']
        ]
