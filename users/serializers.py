from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import VerifyCode

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'












