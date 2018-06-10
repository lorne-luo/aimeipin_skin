import logging
from django.db.models import Q
from dal import autocomplete
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters

from core.api.filters import PinyinSearchFilter
from core.utils.string import include_non_asc
from core.django.autocomplete import HansSelect2ViewMixin
from core.api.views import CommonViewSet
from ..models import Product
from . import serializers

log = logging.getLogger(__name__)


class ProductViewSet(CommonViewSet):
    """ API views for Product """
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_fields = ['name_en', 'name_cn', 'brand__id', 'brand__name_cn', 'brand__name_en']
    search_fields = ['name_cn', 'brand__name_cn']
    pinyin_search_fields = ['name_en', 'pinyin', 'brand__name_en']  # search only input are all ascii chars
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)


class ProductAutocompleteAPIView(HansSelect2ViewMixin, autocomplete.Select2QuerySetView):
    model = Product
    paginate_by = None

    # create_field = 'name_cn'
    #
    # def create_object(self, text):
    #     return self.get_queryset().create(**{self.create_field: text, 'seller': self.request.profile})

    def has_more(self, context):
        return False

    def get_queryset(self):
        qs = Product.objects.all()
        brand_id = self.request.GET.get('brand_id', '')
        category = self.forwarded.get('category')
        if brand_id:
            qs = qs.filter(brand__id=brand_id)
        if category:
            qs = qs.filter(category=category)

        if include_non_asc(self.q):
            qs = qs.filter(Q(name_cn__icontains=self.q))
        else:
            # all ascii, number and letter
            key = self.q.lower()
            if key:
                qs = qs.filter(
                    Q(pinyin__contains=key) | Q(name_en__icontains=key))
        return qs

    def get_results(self, context):
        return [
            {
                'id': self.get_result_value(result),
                'text': self.get_result_label(result),
                'image': result.pic.url if result.pic else None,
            } for result in context['object_list']
        ]
