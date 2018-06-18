from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:brand-list'), reverse('api:brand-detail', kwargs={'pk': 1})
router.register(r'premium_product', views.PremiumProductViewSet, base_name='premiumproduct')

urlpatterns = [
    url(r'^premium_product/autocomplete/$', views.PremiumProductAutocompleteAPIView.as_view(), name='premiumproduct-autocomplete'),
    url(r'^premium_product/search/$', views.PremiumProductSearchAPIView.as_view(), name='premiumproduct-search'),

]

urlpatterns += router.urls
