""" 为应用程序users定义URL模式 """

from django.conf.urls import url
from django.contrib.auth.views import login     # 使用默认登录视图

from . import views

app_name = '[users]',
urlpatterns = [
    # 登录界面
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),
    # 注册界面
    url(r'^register/$', views.register, name='register'),
]
