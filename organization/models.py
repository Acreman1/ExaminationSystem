from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


# 试题分类
class Classify(models.Model):
    name = models.CharField('类别名',max_length=30,null=False)

    def __str__(self):
        return self.name


# 试卷详情信息
class Message(models.Model):
    title = models.CharField('试卷名',max_length=30,null=False)
    introduce = models.CharField('试卷介绍',max_length=256,null=False)
    up_user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    classify = models.ForeignKey('Classify', on_delete=models.CASCADE,null=False)


# 总成绩
class Score(models.Model):
    grade = models.IntegerField("总分",default=0)
    add_time = models.DateTimeField("时间",default=datetime.now)
    an_user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    message = models.ForeignKey('Message', on_delete=models.CASCADE,null=False)


# 单个试题
class Topic(models.Model):
    title = models.CharField('试题题目',max_length=256,null=False)
    grade = models.IntegerField("分数",default=0)
    message = models.ForeignKey('Message', on_delete=models.CASCADE,null=False)
    types = models.CharField('题目类型',max_length=30,null=False)
    answer = models.CharField('答案',max_length=256,null=False)
    options = models.CharField('选项',max_length=256,null=True)

