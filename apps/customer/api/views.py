import logging
from dal import autocomplete
from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from core.api.filters import PinyinSearchFilter
from core.django.autocomplete import HansSelect2ViewMixin
from core.django.permission import SellerRequiredMixin
from core.utils.string import include_non_asc
from core.api.permission import SellerPermissions
from core.api.views import CommonViewSet
from ..models import Customer

from . import serializers

log = logging.getLogger(__name__)

class CustomerViewSet(CommonViewSet):
    """api views for Customer"""
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filter_fields = ['name', 'email', 'mobile','remark']
    search_fields = ['name', 'remark']
    permission_classes = (SellerPermissions,)
    pinyin_search_fields = ['name_py', 'mobile']  # search only input are all ascii chars
    filter_backends = (DjangoFilterBackend,
                       PinyinSearchFilter,
                       filters.OrderingFilter)

    def get_queryset(self):
        queryset = super(CustomerViewSet, self).get_queryset()
        if self.request.user.is_admin or self.request.user.is_superuser:
            return queryset
        return queryset.filter(seller=self.request.profile)


class CustomerAutocomplete(SellerRequiredMixin, HansSelect2ViewMixin, autocomplete.Select2QuerySetView):
    model = Customer
    paginate_by = 20

    def create_object(self, text):
        return self.get_queryset().create(**{self.create_field: text, 'seller': self.request.profile})

    def get_queryset(self):
        qs = Customer.objects.belong_to(self.request.user).annotate(
            order_count_num=Count('order')).order_by('-order_count_num')

        if include_non_asc(self.q):
            qs = qs.filter(name__icontains=self.q)
        else:
            # all ascii, number and letter
            if self.q.isdigit():
                qs = qs.filter(mobile__icontains=self.q)
            else:
                qs = qs.filter(pinyin__contains=self.q.lower())
        return qs

