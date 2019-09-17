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
from django.urls import path,include
from . import login
from . import heart_beat
import passcet.isrunning
import passcet.register
import passcet.checkcode
import passcet.addaccount
import passcet.getusericon
import passcet.loginstatuscheck
from passcet import getword
from passcet import login
from passcet import bindaccount
from passcet import unbindaccount
from passcet import addwordlist
from passcet import delwordlist
from passcet import getwordlist
from passcet import imagetoword
from passcet import getuserinfo
from passcet import pushlearningtime
from passcet import getlearningtime
from django.views.static import serve
#User System Word Timing

from untitled import function
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function.home), #这是启动页面 也就是 http://localhost:port的页面

    path('polls/', include('polls.urls')),
    # path('login/', login.home),
    path('system/heartbeat/' ,passcet.isrunning.home),#System
    path('user/register/',passcet.register.register),# User
    path('user/checkcode/',passcet.checkcode.checkcode),# User
    path('user/addaccount/',passcet.addaccount.addaccount),# User
    path('user/getusericon/',passcet.getusericon.getusericon),# User
    path('user/loginstatuscheck/',passcet.loginstatuscheck.loginstatuscheck),# User
    path('user/login/',login.login),# User
    path('user/bindaccount/',bindaccount.bindaccount),# User
    path('word/getword/',getword.getword),# Word
    path('unbindaccount/',unbindaccount.unbindaccount),# 暂缓
    path('word/addwordlist/',addwordlist.addwordlist),# Word
    path('word/delwordlist/',delwordlist.delwordlist),# Word
    path('word/getwordlist/',getwordlist.getwordlist),# Word
    path('word/imagetoword/',imagetoword.imagetoword),# Word
    path('user/getuserinfo/',getuserinfo.getuserinfo),# User
    path('timing/pushlearningtime/',pushlearningtime.pushlearningtime),# Timing
    path('timing/getlearningtime/',getlearningtime.getlearningtime),# Timing
]
