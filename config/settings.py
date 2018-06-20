# -*- coding:utf-8 -*-
"""
Django settings for ozsales project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import environ
import datetime
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Load operating system environment variables and then prepare to use them
env = environ.Env()
env_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_file):
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined as environment variables.
    print('[environ] Loading : {}'.format(env_file))
    env.read_env(env_file)

BASE_URL = env('BASE_URL', default='http://skin.aimeipin.cc')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='n(jg24woqhp5e-9%r@vbm249e5yeqj%8t!1l*h=x%%o4d73g$6')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('0.0.0.0', '127.0.0.1')
ADMIN_EMAIL = env('ADMIN_EMAIL', default='dev@luotao.net')  # 管理员email地址
ADMINS = [('Admin', ADMIN_EMAIL)]

# Application definition
INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',

    'dal',
    'dal_select2',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # common app
    'core.auth_user',
    'core.commands',  # customized django commands
    'core.adminlte',
    'core.autocode',

    'apps.weixin',
    'apps.product',
    'apps.premium_product',
    'apps.brand',
    'apps.dashboard',
    'apps.survey',
    'apps.report',
    'apps.analysis',
    'apps.celery',  # celery tasks
    'utils',

    # third_app
    'django_extensions',
    'djcelery',
    'django_js_reverse',
    'rest_framework',
    'modelcluster',
    'taggit',
    'stdimage',
    'rest_framework_swagger',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    'core.django.middleware.TemplateContextMiddleware'
    # 'core.django.middleware.ProfileAuthenticationMiddleware',

)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='mysql://root:root@localhost:3306/ozsales')
}

DATABASES['default']['OPTIONS'] = {
    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

LANGUAGES = [
    ('cn', _('Simplified Chinese')),
]

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATE_FORMAT = 'Y/m/j'
DATETIME_FORMAT = 'Y/m/j H:i:s'
TIME_FORMAT = 'H:i:s'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', default=os.path.join(BASE_DIR, 'collectstatic'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = env('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

TEMP_ROOT = os.path.join(MEDIA_ROOT, 'temp')

# Templates
# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'dev@luotao.net'

# AUTH
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = 'auth_user.AuthUser'
AUTHENTICATION_BACKENDS = ['core.auth_user.backend.AuthUserAuthenticateBackend']
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/dashboard'
SESSION_COOKIE_AGE = 604800 * 4  # 4 weeks

# registration
# ACCOUNT_ACTIVATION_DAYS=7
# REGISTRATION_OPEN=True
# REGISTRATION_SALT='IH*&^AGBIovalaft1AXbas2213klsd73'

# CELERY
# ------------------------------------------------------------------------------
# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_BROKER_URL = BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_BROKER_TRANSPORT = BROKER_TRANSPORT = 'redis'
# CELERY_BROKER_TRANSPORT_OPTIONS = BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 604800}
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL
#
# CELERY_TASK_RESULT_EXPIRES = datetime.timedelta(days=1)  # Take note of the CleanUp task in middleware/tasks.py
# CELERY_MAX_CACHED_RESULTS = 1000
# CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
# CELERY_TRACK_STARTED = True
# CELERY_SEND_EVENTS = True
# CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
#
# CELERY_REDIS_CONNECT_RETRY = REDIS_CONNECT_RETRY = True
# CELERY_REDIS_DB = REDIS_DB = 0
# CELERY_BROKER_POOL_LIMIT = BROKER_POOL_LIMIT = 2
# CELERYD_CONCURRENCY = 1
# CELERYD_TASK_TIME_LIMIT = 600

# REST_FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    # 'ORDERING_PARAM' : 'order_by', # Renaming ordering to order_by like sql convention
    'PAGE_SIZE': 15,
    'PAGINATE_BY_PARAM': 'limit',  # Allow client to override, using `?limit=xxx`.
    'MAX_PAGINATE_BY': 999,  # Maximum limit allowed when using `?limit=xxx`.
    'UNICODE_JSON': True,
    'DEFAULT_PAGINATION_CLASS': 'core.api.pagination.CommonPageNumberPagination',

    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': ('%Y-%m-%d %H:%M:%S',),
    'DATE_FORMAT': '%Y-%m-%d',
    'DATE_INPUT_FORMATS': ('%Y-%m-%d',),
    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMATS': ('%H:%M:%S',),
    'LANGUAGES': (
        ('zh-hans', 'Simplified Chinese'),
    ),

    'LANGUAGE_CODE': 'zh-hans',
    'NON_FIELD_ERRORS_KEY': 'detail',

    'DEFAULT_RENDERER_CLASSES': [
        'core.api.renders.UTF8JSONRenderer',
        # 'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoObjectPermissions',
        # 'utils.api.permission.ObjectPermissions',
        'core.api.permission.CommonAPIPermissions',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        # 'rest_framework.filters.DjangoObjectPermissionsFilter', #Will exclusively use guardian tables for access
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.XMLRenderer',
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    )
}

# CONSTANTS SETTINGS
# ------------------------------------------------------------------------------
SITE_NAME = env('SITE_NAME', default='Aimeipin Skin')
# Others
PRODUCT_PHOTO_FOLDER = 'product'
BRAND_LOGO_PHOTO_FOLDER = 'brand'
PREMIUM_PRODUCT_PHOTO_FOLDER = 'premiumproduct'
ANSWER_PHOTO_FOLDER = 'answer'
QRCODE_FOLDER = 'qrcode'
REPORT_PDF_FOLDER = 'report'
# for django-guardian
ANONYMOUS_USER_ID = -1
SITE_ID = 1
INVITE_CODE_EXPIRY = 60  # days

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# LOCAL.PY
# ------------------------------------------------------------------------------
if os.path.exists(os.path.join(os.path.dirname(__file__), "local.py")):
    from .local import *
