from django.http import HttpResponse
from passcet.models import passcet_user
from django.core.mail import send_mail
import json
import requests
import time
import random
import passcet.models
from passcet import settingfile as SF
#Author :NsuMicClub-Liguodong
# URL register/?token= & phone = & email = //token必填 phone和email任选一个即可
# 传入参数 email或者是phone 判断如果email或者是phone重复就返回错误
# 如果没毛病就调用“请求短信验证码”返回一个验证码并返回成功的验证码
def register(request):
    # 处理登录的请求
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    token = request.GET.get('token')
    if phone == None and email == None :
        return HttpResponse('参数缺失！')
    if token == SF.PASSCET_TOKEN:  # 对token进行验证 如果正确才执行逻辑
        username = passcet_user.objects.all()  # 从数据库中拿到集合
        for usernames in username:#轮询没问题后再执行发送相关的逻辑
            if request.GET.get('email') == usernames.email or request.GET.get('phone') == str(usernames.phone):
                return HttpResponse('{"status":"Duplicate phone or e-mail"}')  # 出现重复的手机号或密码时进行检测
        if phone != None: #如果phone里传过来了参数就发送短信
            return sendSMS(phone)
        if email != None: #如果email里传过来了参数就发送电子邮件
            return sendMail(email)
    else:
        return HttpResponse('{"status": "token-error"}')  # token错误
def sendSMS(phoneNumber):
    url = 'https://api2.bmob.cn/1/requestSmsCode'
    # 处理发送短信的逻辑 返回发送状态
    sendData = {
        'mobilePhoneNumber': phoneNumber,
        'template' : 'new'
    }
    headers = {
        'X-Bmob-Application-Id' :'2a26931e1a16ae43b9a3ba96735606f2',
        'X-Bmob-REST-API-Key' : '1b6d994b79583ea0e41bb98c2083f021',
        'Content-Type' :'application/json',
        'Cache-Control' : 'no-cache'
    }
    res = requests.post('https://api2.bmob.cn/1/requestSmsCode',data = json.dumps(sendData),headers = headers)
    # return HttpResponse(res.text)
    print(res.text)
    return HttpResponse('{"type":"phone","status":"OK"}')


def sendMail(emailAddress):
    # 处理发邮件的逻辑 返回发送状态
    #生成两个随机数，一个作为ID一个作为Code 加上时间戳 10min 就是10*60=600 sec
    # 这里可能需要编写一个经常运行的程序来保证验证码表在凌晨两点进行清空
    curlTime = time.time()
    id = random.randint(100000,999999)
    code = random.randint(100000,999999)
    #需要存入数据库并在验证方法中进行验证
    passcet.models.passcet_emailcode.objects.create(id=id,code=code,time=curlTime)
    send_mail('PassCET-验证邮件','您的验证码是['+str(code)+']，有效期10分钟。如非本人操作,请忽略.','passcetapp@163.com',[emailAddress] ,fail_silently=False)
    return HttpResponse('{"id":"'+str(id)+'"}')
