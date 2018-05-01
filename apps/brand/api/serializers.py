from core.api.serializers import BaseSerializer
from ..models import Brand


class BrandSerializer(BaseSerializer):
    """ Serializer for Brand """

    class Meta:
        model = Brand
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['name_en', 'name_cn', 'short_name', 'remarks']
        read_only_fields = ['id']
