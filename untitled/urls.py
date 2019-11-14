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
from passcet import unbindaccount
import passcet.isrunning

# 主要模块引入
from passcet.user import register, checkcode, addaccount, getusericon, loginstatuscheck, login, bindaccount
from passcet.word import imagetoword, getwordlist, getuserinfo, addwordlist, getword, delwordlist, getbriefword
from passcet.timing import pushlearningtime, getlearningtime
from passcet.feedback import pushfeedback
# User System Word Timing
# 导入辅助函数get_schema_view
# 导入两个类
from untitled import function

app_name = 'rest_framework'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function.home),  # 这是启动页面 也就是 http://localhost:port的页面
    path('polls/', include('polls.urls')),
    # path('login/', login.home),
    # 测试接口
    path('system/heartbeat/', passcet.isrunning.home),  # System
    # 用户相关接口
    path('user/register/', passcet.user.register.register),
    path('user/checkcode/', passcet.user.checkcode.checkcode),
    path('user/addaccount/', passcet.user.addaccount.addaccount),
    path('user/getusericon/', passcet.user.getusericon.getusericon),
    path('user/getuserinfo/', getuserinfo.getuserinfo),
    path('user/loginstatuscheck/', passcet.user.loginstatuscheck.loginstatuscheck),
    path('user/login/', login.login),
    path('user/bindaccount/', bindaccount.bindaccount),
    # 单词相关接口
    path('word/getword/', getword.getword),
    path('word/addwordlist/', addwordlist.addwordlist),
    path('word/delwordlist/', delwordlist.delwordlist),
    path('word/getwordlist/', getwordlist.getwordlist),
    path('word/imagetoword/', imagetoword.imagetoword),
    path('word/getbriefword/', getbriefword.getbriefword),
    # 计时相关接口
    path('timing/pushlearningtime/', pushlearningtime.pushlearningtime),
    path('timing/getlearningtime/', getlearningtime.getlearningtime),
    # 反馈相关接口
    path('feedback/pushfeedback/', pushfeedback.pushfeedback),
    # 其他接口
    path('unbindaccount/', unbindaccount.unbindaccount),

]
