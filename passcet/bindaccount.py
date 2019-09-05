from django.http import HttpResponse
import json
from passcet import settingfile as SF
from passcet import models
from passcet import register
from passcet import checkcode
from passcet import takelog
# 检查账号是否存在，如果存在检查将要绑定的手机或邮箱是不是已经被绑定过了
def bindaccount(request):
    token = request.POST.get('token')
    type = request.POST.get('type')
    # 0:已经绑定邮箱，需要绑定手机号；1：已经绑定手机需要绑定邮箱
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    option = request.POST.get('option')
    # 0：发送验证码 1：验证验证码
    id = request.POST.get('id')
    code = request.POST.get('code')
    #验证TOKEN
    if token != None and token == SF.PASSCET_TOKEN:
        if type != None and (phone != None or email != None) and type != None and option != None:
            if type == 0: # 0:已经绑定邮箱，需要绑定手机号
                if len(models.passcet_user.objects.filter(email = email)) == 1: #查库，有这个账号
                    if option == 0: # send code
                        return register.sendSMS(phone)
                    elif option == 1: #check code
                        codestatus_json = checkcode.checkPhone(phone,code) #检查短信的验证码是否正确
                        codestatus = json.loads(codestatus_json.text)
                        if 'code' in codestatus:
                            if(codestatus['code'] == '104'):
                                models.passcet_user.objects.filter(email = email).update(phone=phone);
                                take_log(SF.PASSCET_108_BIND_PHONE_SUCCESS)
                                return HttpResponse(SF.PASSCET_108_BIND_PHONE_SUCCESS)
                    else:
                        take_log(SF.PASSCET_202_PARAMETER_ERROR)
                        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
                else:
                    take_log(SF.PASSCET_205_USER_DOES_NOT_EXIST)
                    return HttpResponse(SF.PASSCET_205_USER_DOES_NOT_EXIST)
            elif type == 1:
                if len(models.passcet_user.objects.filter(phone=phone)) == 1:
                    if option ==0:
                        return register.sendMail(email)
                    elif option == 1:
                        codestatus_json = checkcode.chenkemail(id,code)
                        codestatus = json.loads(codestatus_json.text)
                        if code in codestatus:
                            if codestatus['code'] == '105':
                                models.passcet_user.objects.filter(phone=phone).update(email = email)
                                take_log(SF.PASSCET_109_BIND_EMAIL_SUCCESS)
                                return HttpResponse(SF.PASSCET_109_BIND_EMAIL_SUCCESS)
                    else:
                        take_log(SF.PASSCET_202_PARAMETER_ERROR)
                        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
            else:
                take_log(SF.PASSCET_202_PARAMETER_ERROR)
                return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
        else:
            take_log(SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        take_log(SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)

def take_log(status):
    takelog.takelog('bindaccount',status)