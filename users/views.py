from rest_framework import viewsets
from .serializers import *


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSer
    queryset = UserProfile.objects.all()