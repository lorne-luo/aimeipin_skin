# coding=utf-8
from django import forms

from .models import WxUser


class WxUserDetailForm(forms.ModelForm):
    class Meta:
        model = WxUser
        fields = ['weixin_id', 'is_subscribe', 'nickname', 'openid', 'sex', 'province', 'city', 'country',
                  'headimg_url']
