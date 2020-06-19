from django.http import HttpResponse
from passcet.models import passcet_user
import json
import requests
import time
import passcet.models
from passcet import settingfile as SF
from passcet.utils.takeLog import takelog
def verifiySmsCode(phoneNumber, code):
    sendData = {
        'mobilePhoneNumber': phoneNumber
    }
    headers = {
        'X-Bmob-Application-Id': 'x',
        'X-Bmob-REST-API-Key': 'x',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
    }
    res = requests.post('https://api2.bmob.cn/1/verifySmsCode/' + code, data=json.dumps(sendData), headers=headers)
    json_res = json.loads(res.text)  # 解码为python对象 /dict
    if 'msg' in json_res:
        if (json_res['msg'] == 'ok'):
            # 返回成功的标志告诉前端执行其他操作
            takelog(__file__,SF.PASSCET_104_CHECK_PHONE_MESSAGE_OK)
            return HttpResponse(SF.PASSCET_104_CHECK_PHONE_MESSAGE_OK)
    else:
        print(res.text)
        takelog(__file__,SF.PASSCET_207_PHONE_MESSAGE_ERROR)
        return HttpResponse(SF.PASSCET_207_PHONE_MESSAGE_ERROR)
