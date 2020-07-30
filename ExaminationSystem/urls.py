from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from django.urls import path,include
import xadmin
from organization.views import *
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register('message', MessageView)
router.register('class', ClassifyView)
router.register('topic', TopicView)
router.register('score', ScoreView)


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
    path('api-path/', include('rest_framework.urls'), name='restFramework'),
    path('login/', obtain_jwt_token),
]
