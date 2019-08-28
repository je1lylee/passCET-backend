#解绑手机号或邮箱
from passcet import settingfile as SF
from django.http import HttpResponse
from passcet import models
def unbindaccount(request):
    token = request.POST.get('token')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    # 等待后续添加此功能
    return HttpResponse(SF.PASSCET_101_OK)