import xadmin
from xadmin import views
from .models import EmailVerifyRecord

class BaseSetting(object):
    # xadmin的基础配置
    enabel_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 设置网站标题和页脚
    site_title = "智慧考试系统后台管理页面"
    site_footer = "ExaminationSystem By 【S·A·Y】 - 2020"
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
