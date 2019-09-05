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
            print('err')
        elif email != None:
            user_info=models.passcet_user.objects.filter(email=email)
            tfile = list(user_info.values())[0]
            print([i for i in tfile.keys()][:5])
            print(tfile)
            print(type(tfile))
            print(json.dumps(list(user_info.values())[0:5]))
        elif phone !=None:
            pass
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    return HttpResponse(SF.PASSCET_101_OK)