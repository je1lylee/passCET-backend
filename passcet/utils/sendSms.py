import requests
import json
from django.http import HttpResponse
from passcet import settingfile as SF
from passcet.utils.takeLog import takelog
def sendSMS(phoneNumber):
    """
    发送短信验证码
    :param phoneNumber:
    :return:
    """
    url = 'https://api2.bmob.cn/1/requestSmsCode'
    # 处理发送短信的逻辑 返回发送状态
    sendData = {
        'mobilePhoneNumber': phoneNumber,
        'template': 'new'
    }
    headers = {
        'X-Bmob-Application-Id': 'x',
        'X-Bmob-REST-API-Key': 'x',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
    }
    res = requests.post('https://api2.bmob.cn/1/requestSmsCode', data=json.dumps(sendData), headers=headers)
    # return HttpResponse(res.text)
    print(res.text)
    takelog(__file__,SF.PASSCET_102_SEND_PHONE_MESSAGE_OK)
    return HttpResponse(SF.PASSCET_102_SEND_PHONE_MESSAGE_OK)
