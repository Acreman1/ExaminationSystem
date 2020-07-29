from rest_framework import viewsets
from .models import *


class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfile
    queryset = UserProfile.objects.all()