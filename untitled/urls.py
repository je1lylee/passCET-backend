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
from django.views.static import serve

from untitled import function
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function.home), #这是启动页面 也就是 http://localhost:port的页面

    path('polls/', include('polls.urls')),
    # path('login/', login.home),
    path('heartbeat/' ,passcet.isrunning.home),
    path('register/',passcet.register.register),
    path('checkcode/',passcet.checkcode.checkcode),
    path('addaccount/',passcet.addaccount.addaccount),
    path('getusericon/',passcet.getusericon.getusericon),
    path('loginstatuscheck/',passcet.loginstatuscheck.loginstatuscheck),
    path('login/',login.login),
    path('bindaccount/',bindaccount.bindaccount),
    path('getword/',getword.getword),
    path('unbindaccount/',unbindaccount.unbindaccount),
]
