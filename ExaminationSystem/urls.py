from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from django.urls import path,include
import xadmin
from rest_framework import routers
from users.views import *
from organization.views import *

router = routers.DefaultRouter()
router.register(r'users',UserViewset,basename='users')
router.register('phone',PhoneViewset,basename="phone")
# router.register(r'users',UserViewSet)
router.register('message', MessageView)
router.register('class', ClassifyView)
router.register('topic', TopicView)
router.register('score', ScoreView)


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path(r'',include(router.urls)),
     path('login/', obtain_jwt_token),
    path('',include('social_django.urls',namespace='social')),
    path('code/',CodeViewset.as_view(),name='code'),
    path('send/',SendMailViewset.as_view(),name='send'),
    path('forget/',ForgetViewset.as_view(),name='forget'),
    path('modify/',ModifyPwdView.as_view(),name='modify'),
    path('active/<code>/',ActiveViewset.as_view(),name='active'),
    path('reset/<code>/',ResetViewset.as_view(),name='reset'),


]
