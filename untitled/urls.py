"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import passcet.isrunning
import passcet.user.register
import passcet.user.checkcode
import passcet.user.addaccount
import passcet.user.getusericon
import passcet.user.loginstatuscheck
from passcet.user import login, bindaccount
from passcet import unbindaccount
from passcet.word import imagetoword, getwordlist, getuserinfo, addwordlist, getword, delwordlist
from passcet.timing import pushlearningtime, getlearningtime
# User System Word Timing
# 导入辅助函数get_schema_view
# 导入两个类
from untitled import function
app_name = 'rest_framework'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function.home), #这是启动页面 也就是 http://localhost:port的页面
    path('polls/', include('polls.urls')),
    # path('login/', login.home),
    # 测试接口
    path('system/heartbeat/', passcet.isrunning.home),  # System
    # 用户相关接口
    path('user/register/', passcet.user.register.register),  # User
    path('user/checkcode/', passcet.user.checkcode.checkcode),  # User
    path('user/addaccount/', passcet.user.addaccount.addaccount),  # User
    path('user/getusericon/', passcet.user.getusericon.getusericon),  # User
    path('user/loginstatuscheck/', passcet.user.loginstatuscheck.loginstatuscheck),  # User
    path('user/login/', login.login),  # User
    path('user/bindaccount/', bindaccount.bindaccount),  # User
    # 单词相关接口
    path('word/getword/', getword.getword),  # Word
    path('unbindaccount/', unbindaccount.unbindaccount),  # 暂缓
    path('word/addwordlist/', addwordlist.addwordlist),  # Word
    path('word/delwordlist/', delwordlist.delwordlist),  # Word
    path('word/getwordlist/', getwordlist.getwordlist),  # Word
    path('word/imagetoword/', imagetoword.imagetoword),  # Word
    path('user/getuserinfo/', getuserinfo.getuserinfo),  # User
    # 计时相关接口
    path('timing/pushlearningtime/', pushlearningtime.pushlearningtime),  # Timing
    path('timing/getlearningtime/', getlearningtime.getlearningtime),  # Timing

]
