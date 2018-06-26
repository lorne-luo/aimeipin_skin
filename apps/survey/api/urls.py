from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:answer-list'), reverse('api:answer-detail', kwargs={'pk': 1})
router.register(r'answer', views.AnswerViewSet, base_name='answer')
router.register(r'invitecode', views.InviteCodeViewSet, base_name='invitecode')

urlpatterns = [
    url(r'^answer/rotate/(?P<pk>\d+)/$', views.AnswerPicRotateView.as_view(), name="answer-rotate"),

]

urlpatterns += router.urls
