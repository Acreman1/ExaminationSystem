from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from django.urls import path,include
import xadmin

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-path/',include('rest_framework.urls'),name='restFramework'),
    path('',include(router.urls)),
    path('login/', obtain_jwt_token),
]
