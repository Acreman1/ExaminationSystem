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
    queryset = Score.objects.all().order_by('grade')

    def perform_create(self, serializer):
        serializer.save(an_user_id=2)

