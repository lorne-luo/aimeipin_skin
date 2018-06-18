from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views as auth_views

# from wagtail.wagtailadmin import urls as wagtailadmin_urls
# from wagtail.wagtailcore import urls as wagtail_urls
# from wagtail.wagtaildocs import urls as wagtaildocs_urls
# from wagtail.wagtailimages import urls as wagtailimages_urls
# from apps.wagtail.search.views import search as wagtail_search

from core.auth_user.views import ChangePasswordView
from core import auth_user
from core.auth_user.forms import CustomPasswordResetForm, CustomSetPasswordForm

def if_installed(appname, *args, **kwargs):
    ret = url(*args, **kwargs)
    if appname not in settings.INSTALLED_APPS:
        ret.resolve = lambda *args: None
    return ret


wagtail_urlpatterns = [
    # url(r'^admin/', include(wagtailadmin_urls)),
    # url(r'^documents/', include(wagtaildocs_urls)),
    # url(r'^images/', include(wagtailimages_urls)),
    # url(r'^search/$', wagtail_search, name='wagtail_search'),
    # url(r'^pages/', include(wagtail_urls)),
]

apps_urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.dashboard.urls', namespace='dashboard')),
    url(r'^', include('core.auth_user.urls', namespace='users')),
    url(r'^customer/', include('apps.customer.urls', namespace='customer')),
    url(r'^brand/', include('apps.brand.urls', namespace='brand')),
    url(r'^product/', include('apps.product.urls', namespace='product')),
    url(r'^premium_product/', include('apps.premium_product.urls', namespace='premium_product')),
    url(r'^analysis/', include('apps.analysis.urls', namespace='analysis')),
    url(r'^survey/', include('apps.survey.urls', namespace='survey')),
    url(r'^report/', include('apps.report.urls', namespace='report')),
    url(r'^wx/', include('apps.weixin.urls', namespace='weixin')),
]

# REST API
api_urlpatterns = [
    url(r'^customer/', include('apps.customer.api.urls')),
    url(r'^brand/', include('apps.brand.api.urls')),
    url(r'^product/', include('apps.product.api.urls')),
    url(r'^premium_product/', include('apps.premium_product.api.urls')),
    url(r'^analysis/', include('apps.analysis.api.urls')),
    url(r'^survey/', include('apps.survey.api.urls')),
    url(r'^report/', include('apps.report.api.urls')),
]

urlpatterns = wagtail_urlpatterns + apps_urlpatterns + [
    # REST API
    url(r'^api/', include(api_urlpatterns, namespace='api')),

    # auth
    url('^auth/change-password/$', ChangePasswordView.as_view(), name='change_password'),
    url('^auth/change-password-done/$', auth_user.views.ChangePasswordDoneView.as_view(), name='password_change_done'),

    # password reset
    url(r'^password/reset/$', auth_views.password_reset, {'template_name': 'adminlte/password_reset_form.html',
                                                          'email_template_name': 'adminlte/password_reset_email.html',
                                                          'password_reset_form': CustomPasswordResetForm},
        name='password_reset'),
    url(r'^password/reset/done/$', auth_views.password_reset_done,
        {'template_name': 'adminlte/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'template_name': 'adminlte/password_reset_confirm.html',
         'set_password_form': CustomSetPasswordForm},
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete,
        {'template_name': 'adminlte/password_reset_complete.html'},
        name='password_reset_complete'),

    # dbsettings
    url(r'^djadmin/settings/', include('dbsettings.urls')),

    # django-tinymce
    url(r'^tinymce/', include('tinymce.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    # url(r'^home/', include(wagtail_urls)),
]

if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^api/docs/$', get_swagger_view(title='OZSales API'))
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
