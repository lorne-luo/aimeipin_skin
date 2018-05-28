from core.api.serializers import BaseSerializer
from ..models import Word, SkinType


class WordSerializer(BaseSerializer):
    """ Serializer for Word """

    class Meta:
        model = Word
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['purpose', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type']
        read_only_fields = ['id']


class SkinTypeSerializer(BaseSerializer):
    """ Serializer for Word """

    class Meta:
        model = SkinType
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['dimension', 'name', 'short_name', 'description']
        read_only_fields = ['id']
