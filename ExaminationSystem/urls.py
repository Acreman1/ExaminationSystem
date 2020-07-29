from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from django.urls import path,include
import xadmin
from rest_framework.routers import DefaultRouter
from organization.views import *
from users.views import *

routers = DefaultRouter()
routers.register('message', MessageView)
routers.register('user', UserView)
routers.register('class', ClassifyView)
routers.register('topic', TopicView)
routers.register('score', ScoreView)

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(routers.urls))
    path('api-path/',include('rest_framework.urls'),name='restFramework'),
    path('login/', obtain_jwt_token),
]
