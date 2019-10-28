from django.http import HttpResponse
from passcet.models import passcet_user
import json
import requests
import time
import passcet.models
from passcet import settingfile as SF
from passcet import takelog
def verifiyMailCode(emailAddress):
    #  需要验证id和code是否对应,time是否超时.可能要定期删个库啥的。。
    queryDB = passcet.models.passcet_emailcode.objects.filter(id=id)  # 通过过滤器查询指定的记录
    print(queryDB.exists())  # 存在值T 不存在F
    if queryDB.exists():
        print('在数据库里查询到了结果')
        for i in queryDB:
            if str(i.code) == str(code) and time.time() - i.time <= 600:
                take_log(SF.PASSCET_105_CHECK_EMAIL_MESSAGE_OK)
                return HttpResponse(SF.PASSCET_105_CHECK_EMAIL_MESSAGE_OK)
            else:
                print(time.time() - i.time)
                take_log(SF.PASSCET_208_EMAIL_MESSAGE_ERROR)
                return HttpResponse(SF.PASSCET_208_EMAIL_MESSAGE_ERROR)
    else:
        take_log(SF.PASSCET_209_EMAIL_MESSAGE_ID_ERROR)
        return HttpResponse(SF.PASSCET_209_EMAIL_MESSAGE_ID_ERROR)