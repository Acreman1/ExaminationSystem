from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler, JSONWebTokenAuthentication

from .serializers import *
from rest_framework import viewsets


class MessageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MessageSer
    queryset = Message.objects.all()


class ClassifyView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassifySer
    queryset = Classify.objects.all()


class TopicView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopicSer
    queryset = Topic.objects.all()


class ScoreView(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.CreateModelMixin):
    serializer_class = ScoreSer
    queryset = Score.objects.all().order_by('-grade')
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        token = self.request.POST.get('jwt')
        token_user = jwt_decode_handler(token)
        print(token_user)
        serializer.save(an_user_id=token_user['user_id'])


