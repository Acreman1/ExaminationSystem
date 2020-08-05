import os
import re

import xlrd
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler, JSONWebTokenAuthentication
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .serializers import *
from rest_framework import viewsets, generics
import csv
from ExaminationSystem.settings import MEDIA_ROOT


class MessageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MessageSer
    queryset = Message.objects.all()


class ClassifyView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassifySer
    queryset = Classify.objects.all()


class TopicView(viewsets.ReadOnlyModelViewSet, viewsets.mixins.CreateModelMixin):
    serializer_class = TopicSer
    queryset = Topic.objects.all()

    def perform_create(self, serializer):
        file = self.request.FILES.get('file')
        path = default_storage.save('files/'+file.name, ContentFile(file.read()))
        tmp_file = os.path.join(MEDIA_ROOT, path)

        wb = xlrd.open_workbook(tmp_file)
        wb.sheet_names()
        sh = wb.sheet_by_index(0)
        sh = wb.sheet_by_name(u'Sheet1')
        for rownum in range(1,sh.nrows):
            types = sh.row_values(rownum)[1]
            grade = 5
            answer = sh.row_values(rownum)[-3]
            options = None
            if sh.row_values(rownum)[1] == '单选题':
                options = sh.row_values(rownum)[-4]
            Topic.objects.create(types=types, grade=grade, answer=answer, options=options,message_id=int(serializer.data['message']))
            # serializer.save(types=types, grade=grade, answer=answer, options=options)
        os.remove(tmp_file)


class ScoreView(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.CreateModelMixin):
    serializer_class = ScoreSer
    queryset = Score.objects.all().order_by('-grade')
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        token = self.request.POST.get('jwt')
        token_user = jwt_decode_handler(token)
        print(token_user)
        serializer.save(an_user_id=token_user['user_id'])


