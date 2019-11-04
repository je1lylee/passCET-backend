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
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
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
# User System Word Timing
# 导入辅助函数get_schema_view
from rest_framework.schemas import get_schema_view
# 导入两个类
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
schema_view = get_schema_view(title='API',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])
from untitled import function
app_name = 'rest_framework'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function.home), #这是启动页面 也就是 http://localhost:port的页面
    path('polls/', include('polls.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # api-auth对应授权登录url
    path('docs/',schema_view,name='docs'),
    # path('login/', login.home),
    # 测试接口
    path('system/heartbeat/', passcet.isrunning.home),  # System
    # 用户相关接口
    path('user/register/', passcet.register.register),  # User
    path('user/checkcode/', passcet.checkcode.checkcode),  # User
    path('user/addaccount/', passcet.addaccount.addaccount),  # User
    path('user/getusericon/', passcet.getusericon.getusericon),  # User
    path('user/loginstatuscheck/', passcet.loginstatuscheck.loginstatuscheck),  # User
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
