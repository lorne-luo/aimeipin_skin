'''
 Create initial common data
'''
import os

from django.contrib.auth import get_user_model
from django.core import management
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from django.conf import settings


class Command(BaseCommand):
    help = 'Create default group, superuser, topics and sectors.'

    def handle(self, *args, **options):
        admin_group, created = Group.objects.get_or_create(name='Admin')

        User = get_user_model()
        admin = User.objects.filter(is_superuser=True).first()
        if not admin:
            admin = User.objects.create_superuser(email='dev@luotao.net',
                                                  password='123456',
                                                  first_name='Tao',
                                                  last_name='Luo')
        admin.groups.add(admin_group)
        admin.save()

        os.makedirs(os.path.join(settings.MEDIA_ROOT, settings.BRAND_LOGO_PHOTO_FOLDER), exist_ok=True)
        os.makedirs(os.path.join(settings.MEDIA_ROOT, settings.PRODUCT_PHOTO_FOLDER), exist_ok=True)
        os.makedirs(os.path.join(settings.MEDIA_ROOT, settings.PREMIUM_PRODUCT_PHOTO_FOLDER), exist_ok=True)
        os.makedirs(os.path.join(settings.MEDIA_ROOT, settings.ANSWER_PHOTO_FOLDER), exist_ok=True)
        os.makedirs(os.path.join(settings.MEDIA_ROOT, settings.QRCODE_FOLDER), exist_ok=True)

        self.stdout.write(self.style.SUCCESS('Superuser and Admin group created.'))
