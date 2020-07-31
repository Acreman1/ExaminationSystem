from django.urls import path,include
import xadmin
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from users.views import UserViewset,SendMailViewset,ActiveViewset
from users.views import ResetViewset,ForgetViewset,ModifyPwdView


router = routers.DefaultRouter()
router.register(r'users',UserViewset,basename='users')



urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path(r'',include(router.urls)),
    path('send/',csrf_exempt(SendMailViewset.as_view()),name='send'),
    path('forget/',csrf_exempt(ForgetViewset.as_view()),name='forget'),
    path('modify/',csrf_exempt(ModifyPwdView.as_view()),name='modify'),
    path('active/<code>/',csrf_exempt(ActiveViewset.as_view()),name='active'),
    path('reset/<code>/',csrf_exempt(ResetViewset.as_view()),name='reset'),


]
