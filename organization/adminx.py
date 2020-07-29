import xadmin
from .models import *


class MessageAdmin():
    list_display = ['introduce', 'up_user', 'classify']


class ClassifyAdmin():
    list_display = ['name']


xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Classify, ClassifyAdmin)
