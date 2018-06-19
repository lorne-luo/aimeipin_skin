from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager

from core.auth_user.constant import ADMIN_GROUP


class AuthUserManager(UserManager):
    def _create_user(self, username, password, is_staff, is_superuser, email, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, mobile=None, email=None, password=None, **extra_fields):
        return self._create_user(username, password, False, False, email, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, password, True, True, email, **extra_fields)


class AuthUser(AbstractUser):
    WEBSITE = 'WEBSITE'
    WEIXIN = 'WEIXIN'
    USER_TYPE_CHOICES = (
        (WEBSITE, WEBSITE),
        (WEIXIN, WEIXIN),
    )
    email = models.EmailField(_('email address'), blank=True)
    mobile = models.CharField(_('mobile'), max_length=128, blank=True)
    type = models.CharField(_('type'), max_length=32, choices=USER_TYPE_CHOICES, blank=True, default=WEBSITE)
    # if type is WEBSIT mobile field is mobile, if type is WEIXIN mobile field is openid

    objects = AuthUserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    @property
    def profile(self):
        if getattr(self, 'seller', None):
            return getattr(self, 'seller')
        elif getattr(self, 'customer', None):
            return getattr(self, 'customer')
        return None

    @property
    def is_seller(self):
        return getattr(self, 'seller') is not None

    @property
    def is_customer(self):
        return getattr(self, 'customer') is not None

    def get_username(self):
        return self.mobile or self.email or self.username

    def in_group(self, group_names):
        if not isinstance(group_names, (list, tuple)):
            group_names = (group_names,)

        if self.is_superuser:
            return True
        user_groups = self.groups.values_list("name", flat=True)
        intersection = set(group_names).intersection(set(user_groups))
        return bool(intersection)

    @property
    def is_admin(self):
        return self.is_superuser or self.in_group(ADMIN_GROUP)

    def email_user(self, subject, message, from_email=None, **kwargs):
        if self.email:
            # todo send email
            pass

    def send_sms(self, content, app_name=None):
        if self.mobile:
            # todo send sms for china mobile number
            pass


class UserProfileMixin(object):
    @property
    def profile(self):
        return self

    @property
    def username(self):
        return self.auth_user.get_username()

    @property
    def date_joined(self):
        return self.auth_user.date_joined

    @property
    def is_admin(self):
        return self.auth_user.is_superuser or self.in_group(ADMIN_GROUP)

    @property
    def is_active(self):
        return self.auth_user.is_active

    def in_group(self, group_names):
        return self.auth_user.in_group(group_names)
