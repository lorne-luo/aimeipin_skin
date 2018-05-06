from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:brand-list'), reverse('api:brand-detail', kwargs={'pk': 1})
router.register(r'premium_product', views.PremiumProductViewSet, base_name='premium_product')

urlpatterns = [
    url(r'^premium_product/premium_product/autocomplete/$', views.PremiumProductAutocompleteAPIView.as_view(), name='premium_product-autocomplete'),
]

urlpatterns += router.urls
