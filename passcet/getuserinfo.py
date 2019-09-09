# 返回用户的id,昵称，邮箱，手机，头像的md5，学习等级。
from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import models
import json

def getuserinfo(request):
    token = request.POST.get('token')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    if token!=None and token == SF.PASSCET_TOKEN:
        if email == None and phone ==None:
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
        elif email != None:
            return getviaemail(email)
        elif phone !=None:
            return getviaphone(phone)
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    return HttpResponse(SF.PASSCET_101_OK)

def getviaemail(email):
    user_info = models.passcet_user.objects.filter(email=email)
    return json.dumps(list(user_info.values()))
def getviaphone(phone):
    user_info = models.passcet_user.objects.filter(phone=phone)
    return json.dumps(list(user_info.values()))