from core.api.serializers import BaseSerializer
from ..models import Brand


class BrandSerializer(BaseSerializer):
    """ Serializer for Brand """

    class Meta:
        model = Brand
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['name_en', 'name_cn', 'first_letter_en', 'first_letter_cn', 'logo']
        read_only_fields = ['id']
