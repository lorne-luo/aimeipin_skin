from core.api.serializers import BaseSerializer
from ..models import Word


class WordSerializer(BaseSerializer):
    """ Serializer for Word """

    class Meta:
        model = Word
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['purpose', 'oily_type', 'sensitive_type', 'pigment_type', 'loose_type']
        read_only_fields = ['id']
