from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:brand-list'), reverse('api:brand-detail', kwargs={'pk': 1})
router.register(r'brand', views.BrandViewSet, base_name='brand')

urlpatterns = [
    url(r'^brand/brand/autocomplete/$', views.BrandAutocompleteAPIView.as_view(), name='brand-autocomplete'),
]

urlpatterns += router.urls
