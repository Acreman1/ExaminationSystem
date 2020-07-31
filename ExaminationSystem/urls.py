from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from django.urls import path,include
import xadmin
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from users.views import UserViewset,SendMailViewset,ActiveViewset
from users.views import ResetViewset,ForgetViewset,ModifyPwdView
from organization.views import *
# from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewset,basename='users')
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
    path('',include('social_django.urls',namespace='social'))
    path('send/',csrf_exempt(SendMailViewset.as_view()),name='send'),
    path('forget/',csrf_exempt(ForgetViewset.as_view()),name='forget'),
    path('modify/',csrf_exempt(ModifyPwdView.as_view()),name='modify'),
    path('active/<code>/',csrf_exempt(ActiveViewset.as_view()),name='active'),
    path('reset/<code>/',csrf_exempt(ResetViewset.as_view()),name='reset'),


]
