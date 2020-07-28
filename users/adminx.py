import xadmin
from xadmin import views


class BaseSetting(object):
    # xadmin的基础配置
    enabel_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 设置网站标题和页脚
    site_title = "智慧考试系统后台管理页面"
    site_footer = "ExaminationSystem By 【S·A·Y】 - 2020"


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)