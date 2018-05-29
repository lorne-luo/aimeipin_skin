from rest_framework import serializers

from core.api.serializers import BaseSerializer
from ..models import Word, SkinType


class WordSerializer(BaseSerializer):
    """ Serializer for Word """
    oily_type_display = serializers.SerializerMethodField()
    sensitive_type_display = serializers.SerializerMethodField()
    pigment_type_display = serializers.SerializerMethodField()
    loose_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Word
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['purpose', 'oily_type_display', 'sensitive_type_display', 'pigment_type_display',
                  'loose_type_display']
        read_only_fields = ['id']

    def get_oily_type_display(self, obj):
        return obj.oily_type.name

    def get_sensitive_type_display(self, obj):
        return obj.sensitive_type.name

    def get_pigment_type_display(self, obj):
        return obj.pigment_type.name

    def get_loose_type_display(self, obj):
        return obj.loose_type.name


class SkinTypeSerializer(BaseSerializer):
    """ Serializer for Word """

    class Meta:
        model = SkinType
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['dimension', 'name', 'short_name', 'description']
        read_only_fields = ['id']
