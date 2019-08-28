#解绑手机号或邮箱
from passcet import settingfile as SF
from django.http import HttpResponse
from passcet import models
def unbindaccount(request):
    return HttpResponse(SF.PASSCET_101_OK)