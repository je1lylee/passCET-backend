from django.http import HttpResponse
from passcet.models import passcet_user
import json
import requests
import time
import passcet.models
from passcet import settingfile as SF
from passcet import takelog
#author: NsuMicClub-Liguodong
def checkcode(request):
    token = request.GET.get('token')
    phoneNumber = request.GET.get('phone')
    id = request.GET.get('id')
    code = request.GET.get('code')
    if token == SF.PASSCET_TOKEN and code != None:
        if (phoneNumber != None):
            return checkPhone(phoneNumber, code)
        elif (id != None):
            return chenkemail(id, code)
    else:
        take_log(SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)


def checkPhone(phoneNumber, code):
    sendData = {
        'mobilePhoneNumber': phoneNumber
    }
    headers = {
        'X-Bmob-Application-Id': '2a26931e1a16ae43b9a3ba96735606f2',
        'X-Bmob-REST-API-Key': '1b6d994b79583ea0e41bb98c2083f021',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
    }
    res = requests.post('https://api2.bmob.cn/1/verifySmsCode/' + code, data=json.dumps(sendData), headers=headers)
    json_res = json.loads(res.text)  # 解码为python对象 /dict
    if 'msg' in json_res:
        if (json_res['msg'] == 'ok'):
            # 返回成功的标志告诉前端执行其他操作
            take_log(SF.PASSCET_104_CHECK_PHONE_MESSAGE_OK)
            return HttpResponse(SF.PASSCET_104_CHECK_PHONE_MESSAGE_OK)
    else:
        print(res.text)
        take_log(SF.PASSCET_207_PHONE_MESSAGE_ERROR)
        return HttpResponse(SF.PASSCET_207_PHONE_MESSAGE_ERROR)
def chenkemail(id, code):
    #  需要验证id和code是否对应,time是否超时.可能要定期删个库啥的。。
    queryDB = passcet.models.passcet_emailcode.objects.filter(id=id) #通过过滤器查询指定的记录
    print(queryDB.exists()) #  存在值T 不存在F
    if queryDB.exists():
        print('在数据库里查询到了结果')
        for i in queryDB:
            if str(i.code) == str(code) and time.time()-i.time <= 600:
                take_log(SF.PASSCET_105_CHECK_EMAIL_MESSAGE_OK)
                return HttpResponse(SF.PASSCET_105_CHECK_EMAIL_MESSAGE_OK)
            else:
                print(time.time()-i.time)
                take_log(SF.PASSCET_208_EMAIL_MESSAGE_ERROR)
                return HttpResponse(SF.PASSCET_208_EMAIL_MESSAGE_ERROR)
    else:
        take_log(SF.PASSCET_209_PHONE_MESSAGE_ID_ERROR)
        return HttpResponse(SF.PASSCET_209_PHONE_MESSAGE_ID_ERROR)
def take_log(status):
    takelog('checkcode',status)