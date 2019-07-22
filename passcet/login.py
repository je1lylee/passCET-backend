from django.http import HttpResponse
from untitled import settings
from passcet import checkcode
def login(request):
    token = request.POST.get('token')
    type = request.POST.get('type') #type 0：验证存在并发送验证码 type1：验证验证码并返回结果，同时把用户的ID返回给客户端
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    if token != settings.PASSCET_TOKEN:

    return HttpResponse('success')