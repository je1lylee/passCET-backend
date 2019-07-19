from django.http import HttpResponse
from passcet.models import passcet_user
import json
import requests
import time
import passcet.models
#author: NsuMicClub-Liguodong
def checkcode(request):
    token = request.GET.get('token')
    phoneNumber = request.GET.get('phone')
    id = request.GET.get('id')
    code = request.GET.get('code')
    if token == 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW' and code != None:
        if (phoneNumber != None):
            return checkPhone(phoneNumber, code)
        elif (id != None):
            return chenkemail(id, code)
    else:
        return HttpResponse('{"status":"error"}')  # 错误的返回值


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
            return HttpResponse('{"status" : "ok"}')
    else:
        print(res.text)
        return HttpResponse('{"status" : "code-error"}')
def chenkemail(id, code):
    #  需要验证id和code是否对应,time是否超时.可能要定期删个库啥的。。
    queryDB = passcet.models.passcet_emailcode.objects.filter(id=id) #通过过滤器查询指定的记录
    print(queryDB.exists()) #  存在值T 不存在F
    if queryDB.exists():
        print('在数据库里查询到了结果')
        for i in queryDB:
            if str(i.code) == str(code) and time.time()-i.time <= 600:
                return HttpResponse('{"status": "ok"}')
            else:
                print(time.time()-i.time)
                return HttpResponse('{"status": "code-error"}')
    else:
        return HttpResponse('{"status":"no-data"}')
