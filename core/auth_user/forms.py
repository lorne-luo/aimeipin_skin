from django import forms
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .models import AuthUser


class UserProfileForm(forms.ModelForm):
    name = forms.CharField(label=u'姓名', max_length=30, required=True,
                           widget=forms.TextInput(attrs={'placeholder': u'姓名'}))
    mobile = forms.CharField(label=u'手机号', max_length=30, required=True, validators=[
        RegexValidator(regex='^\d*$', message=u'澳洲或国内手机号，无需区号', code='Invalid number')],
                             widget=forms.TextInput(attrs={'placeholder': u'澳洲或国内手机号，无需区号'}))
    email = forms.EmailField(label=u"电子邮件", required=True, widget=forms.EmailInput(attrs={'placeholder': u'电子邮件'}))
    password = forms.CharField(label=u"更改密码", min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'无需更改请留空'}),
                               required=False, error_messages={'min_length': _(u'密码最小长度6位')})
    password2 = forms.CharField(label=u"确认密码", min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'确认密码'}),
                                required=False, error_messages={'min_length': _(u'密码最小长度6位')})

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AuthUser
        exclude = ['expire_at', 'start_at', 'auth_user', 'country']

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            self.add_error('password2', u'确认密码不匹配，请重新输入')
        if AuthUser.objects.filter(email=email).exclude(id=self.instance.auth_user.id).exists():
            self.add_error('email', u'该电子邮件已存在')
        if AuthUser.objects.filter(mobile=mobile).exclude(id=self.instance.auth_user.id).exists():
            self.add_error('mobile', u'该手机号码已存在')

        return self.cleaned_data


class PasswordLengthValidator(object):
    ''' check password length '''

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 4:
            raise ValidationError("Password must be at least 4 characters.")
        return password1


class RegisterForm(forms.Form):
    mobile = forms.CharField(label=u"澳洲或国内手机", error_messages={'required': _(u'澳洲或国内手机号, 必填项')}, validators=[
        RegexValidator(regex='^\d*$', message=u'澳洲或国内手机号，无需区号', code='Invalid number')])
    email = forms.EmailField(label=u"电子邮件", error_messages={'required': _(u'电子邮件, 必填项')})
    # name = forms.CharField(label=u"姓名", required=False)
    password = forms.CharField(widget=forms.PasswordInput, label=u"密 码", min_length=6, error_messages={
        'min_length': _(u'密码最小长度6位'),
        'required': _(u'密码, 必填项'),
    })
    password_confirm = forms.CharField(widget=forms.PasswordInput, label=u"确认密码", min_length=6, error_messages={
        'min_length': _(u'密码最小长度6位'),
        'required': _(u'重复密码, 必填项'),
    })

    # layout = Layout('mobile', 'email',
    #                 Row('password', 'password_confirm'))

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirm')

        if password1 and password1 != password2:
            self.add_error('password_confirm', u'确认密码不匹配，请重新输入')
        if AuthUser.objects.filter(email=email).exists():
            self.add_error('email', u'该电子邮件已存在')
        if AuthUser.objects.filter(mobile=mobile).exists():
            self.add_error('mobile', u'该手机号码已存在')

        return self.cleaned_data


class LoginForm(forms.Form):
    mobile = forms.CharField(label=u"澳洲或国内手机或电子邮件", error_messages={'required': _(u'请填写手机号或电子邮件')})
    password = forms.CharField(widget=forms.PasswordInput, label=u"密 码", min_length=6, error_messages={
        'min_length': _(u'密码最小长度6位'),
        'required': _(u'请填写密码'),
    })


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, error_messages={'required': _(u'请填写电子邮件')})

    def clean_email(self):
        email = self.cleaned_data['email']
        if not AuthUser.objects.filter(email=email).exists():
            raise forms.ValidationError("该电子邮件不存在，请重新输入")
        return email


class CustomSetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': _(u"确认密码不匹配，请重新输入"),
    }
    new_password1 = forms.CharField(widget=forms.PasswordInput, label=u"密 码", min_length=6, error_messages={
        'min_length': _(u'密码最小长度6位'),
        'required': _(u'密码, 必填项'),
    })
    new_password2 = forms.CharField(widget=forms.PasswordInput, label=u"确认密码", min_length=6, error_messages={
        'min_length': _(u'密码最小长度6位'),
        'required': _(u'重复密码, 必填项'),
    })
