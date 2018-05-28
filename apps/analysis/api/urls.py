from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:word-list'), reverse('api:word-detail', kwargs={'pk': 1})
router.register(r'word', views.WordViewSet, base_name='word')
router.register(r'skintype', views.SkinTypeViewSet, base_name='skintype')

urlpatterns = [
    url(r'^word/autocomplete/$', views.WordAutocompleteAPIView.as_view(), name='word-autocomplete'),
]

urlpatterns += router.urls
