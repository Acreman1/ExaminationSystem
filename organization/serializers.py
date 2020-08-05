from .models import *
from rest_framework import serializers


class TopicSer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class MessageSer(serializers.ModelSerializer):
    up_user = serializers.ReadOnlyField(source='up_user.name')
    classify = serializers.ReadOnlyField(source='classify.name')
    classify1 = serializers.ReadOnlyField(source='classify.id')
    message_key = TopicSer(many=True)

    class Meta:
        model = Message
        fields = '__all__'


class ClassifySer(serializers.ModelSerializer):
    # source = 'class_key.title' 
    class_key = MessageSer(many=True)

    class Meta:
        model = Classify
        fields = '__all__'


class ScoreSer(serializers.ModelSerializer):
    an_user = serializers.ReadOnlyField(source='an_user.name')

    class Meta:
        model = Score
        fields = '__all__'

