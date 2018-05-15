from core.api.serializers import BaseSerializer
from ..models import Answer


class AnswerSerializer(BaseSerializer):
    """ Serializer for Answer """

    class Meta:
        model = Answer
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['city', 'name', 'sex', 'portrait', 'portrait_part', 'cosmetics', 'birth', 'height', 'width', 'job',
                  'monthly_income', 'weixin_id', 'mobile']
        read_only_fields = ['id']
