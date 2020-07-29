from rest_framework import serializers
from .models import *


class UserSer(serializers.ModelSerializer):
    model = UserProfile
    fields = '__all__'