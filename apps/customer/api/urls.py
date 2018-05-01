from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:customer-list'), reverse('api:customer-detail', kwargs={'pk': 1})
router.register(r'customer', views.CustomerViewSet, base_name='customer')

urlpatterns = [
    url(r'^customer/autocomplete/$', views.CustomerAutocomplete.as_view(), name='customer-autocomplete'),
]

urlpatterns += router.urls
