from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:wxuser-list'), reverse('api:wxuser-detail', kwargs={'pk': 1})
router.register(r'wxuser', views.WxUserViewSet, base_name='wxuser')

urlpatterns = [
    # url(r'^wxuser/autocomplete/$', views.CustomerAutocomplete.as_view(), name='customer-autocomplete'),
]

urlpatterns += router.urls
