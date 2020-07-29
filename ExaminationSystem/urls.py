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

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('auth', include('rest_framework.urls')),
    path('', include(routers.urls))
]
