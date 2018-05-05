'''
 Create initial common data 
'''
from django.contrib.auth import get_user_model
from django.core import management
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
import copy


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
        self.stdout.write(self.style.SUCCESS('Superuser and Admin group created.'))
