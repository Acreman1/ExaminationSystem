import xadmin
from .models import Classify,Message,Score,Topic


class ClassAdmin(object):
    list_display = ['name']


class MessAdmin(object):
    list_display = ['title','introduce','up_user','classify']
    list_filter = ['title']
    search_fields = ['title']


class ScoreAdmin(object):
    list_display = ['grade','add_time','an_user','message']
    search_fields = ['an_user']


class TopicAdmin(object):
    list_display = ['title','grade','message','types','answer','options']
    list_filter = ['title','types','grade']
    search_fields = ['title']


xadmin.site.register(Classify, ClassAdmin)
xadmin.site.register(Message, MessAdmin)
xadmin.site.register(Score, ScoreAdmin)
xadmin.site.register(Topic, TopicAdmin)
