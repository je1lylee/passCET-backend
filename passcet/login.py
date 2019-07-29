from django.http import HttpResponse
from passcet import checkcode,models,settingfile as SF,register
def login(request):
    token = request.POST.get('token')
    type = request.POST.get('type') #type 0：验证存在并发送验证码 type1：验证验证码并返回结果，同时把用户的ID返回给客户端
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    if token != SF.PASSCET_TOKEN and token != None:
        if type != None and (phone!=None or email != None):
            if type == 0: #用户是否存在
                if phone == None:
                    # 处理邮件验证码
                    if len(models.passcet_user.objects.filter(email=email)) == 1:
                        register.sendMail(email)
                    else:
                        return HttpResponse(SF.PASSCET_USER_DOES_NOT_EXIST)
                else:
                    if len(models.passcet_user.objects.filter(phone=phone)) == 1:
                        register.sendSMS(phone)
                    else:
                        return HttpResponse(SF.PASSCET_USER_DOES_NOT_EXIST)
            elif type == 1:
                print()
            else:
                return HttpResponse(SF.PASSCET_PARAMETER_ERROR)
        else:
            return HttpResponse(SF.PASSCET_PARAMETER_ERROR)
    else:
        return HttpResponse(SF.PASSCET_TOKEN_ERROR)