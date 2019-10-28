from django.http import HttpResponse
from passcet import checkcode, models, settingfile as SF, register
from passcet.utils.takeLog import takelog


def login(request):
    token = request.POST.get('token')
    type = request.POST.get('type')  # type 0：验证存在并发送验证码 type1：验证验证码并返回结果，同时把用户的ID等信息返回给客户端。
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    id = request.POST.get('id')
    code = request.POST.get('code')
    if token == SF.PASSCET_TOKEN and token != None:
        if type != None:
            if type == '0' and (phone != None or email != None):  # 用户是否存在
                if phone == None:
                    # 处理邮件验证码
                    if len(models.passcet_user.objects.filter(email=email)) == 1:
                        takelog(__file__, SF.PASSCET_101_OK)
                        return register.sendMail(email)
                    else:
                        takelog(__file__, SF.PASSCET_205_USER_DOES_NOT_EXIST)
                        return HttpResponse(SF.PASSCET_205_USER_DOES_NOT_EXIST)
                else:
                    if len(models.passcet_user.objects.filter(phone=phone)) == 1:
                        takelog(__file__, SF.PASSCET_101_OK)
                        return register.sendSMS(phone)
                    else:
                        takelog(__file__, SF.PASSCET_205_USER_DOES_NOT_EXIST)
                        return HttpResponse(SF.PASSCET_205_USER_DOES_NOT_EXIST)
            elif type == '1':
                if phone != None and code != None:
                    takelog(__file__, SF.PASSCET_101_OK)
                    return checkcode.checkPhone(phone, code)
                elif id != None and code != None:
                    takelog(__file__, SF.PASSCET_101_OK)
                    return checkcode.chenkemail(id, code)
                else:
                    takelog(__file__, SF.PASSCET_202_PARAMETER_ERROR)
                    return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)  # 缺少参数
            else:
                takelog(__file__, SF.PASSCET_202_PARAMETER_ERROR)
                return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
        else:
            takelog(__file__, SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        takelog(__file__, SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
