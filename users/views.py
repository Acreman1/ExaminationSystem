from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q

from rest_framework import viewsets,authentication,generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializers
from utils.peimissions import IsOwnerReadOnly

User = get_user_model()


class CustomBackend(ModelBackend):
    # 自定义用户验证
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewSet(viewsets.ViewSetMixin,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [JSONWebTokenAuthentication,authentication.SessionAuthentication]

    def get_object(self):
        return self.request.user


def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    return {
        'token': token,
        'user': UserSerializers(user, context={'request': request}).data
    }





