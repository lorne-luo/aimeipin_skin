from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:answer-list'), reverse('api:answer-detail', kwargs={'pk': 1})
router.register(r'answer', views.AnswerViewSet, base_name='answer')

urlpatterns = [
]

urlpatterns += router.urls
