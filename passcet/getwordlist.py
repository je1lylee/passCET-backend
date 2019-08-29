# 获取用户生词表
from passcet import settingfile as SF
from django.http import HttpResponse
def getwordlist(request):
    return HttpResponse(SF.PASSCET_101_OK)