from django.http import HttpResponse
import time
import random
import passcet.models


# 只有在验证码验证成功的时候才可以调用，这个方法就直接往数据库里写信息了
# 这里还没登录 所以不着急写入最后一次登录时间和设备的IMEI码
def addaccount(request):
    token = request.POST.get('token')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    # leavel = request.POST.get('leavel')
    leavel = 0
    #  id由随机数生成，8位数字 如果重复了可能会报错？
    if token == 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW' and (phone != None or email != None):
        rtime = time.time()  # Unix时间戳
        if (phone != None):
            return viaPhone(phone, leavel, rtime)
        else:
            return viaEmail(phone, leavel, rtime)
    else:
        return HttpResponse('{"status":"error"}')


def viaPhone(phone, leavel, registerTime):
    if passcet.models.passcet_user.objects.get(phone=phone) == None: #判断库里是不是已经有了相同的信息
        passcet.models.passcet_user.objects.create(phone=phone,leavel=leavel,registertime=registerTime)
        return HttpResponse('{"status": "rigister_success"}')
    else:
        return HttpResponse('{"status":"already_exists"}')

def viaEmail(email, leavel, registerTime):
    return HttpResponse('viaEmail')
    print('b')
