from django.http import HttpResponse
import time
import random
import passcet.models
import os
# Author:NsuMicClub-Liguodong

# 只有在验证码验证成功的时候才可以调用，这个方法就直接往数据库里写信息了
# 这里还没登录 所以不着急写入最后一次登录时间和设备的IMEI码
def addaccount(request):
    name = request.POST.get('name')
    token = request.POST.get('token')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    leavel = 0
    if token == 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW' and (phone != None or email != None) and name != None:
        rtime = time.time()  # Unix时间戳
        if (phone != None):
            return viaPhone(phone, leavel, rtime,name)
        else:
            return viaEmail(email, leavel, rtime,name)
    else:
        return HttpResponse('{"status":"error"}')


def viaPhone(phone, leavel, registerTime,name):
    if len(passcet.models.passcet_user.objects.filter(phone__exact=phone)) == 0: #判断库里是不是已经有了相同的信息
        passcet.models.passcet_user.objects.create(phone=phone,leavel=leavel,registertime=registerTime,name=name)
        return HttpResponse('{"status": "rigister_success"}')
    else:
        return HttpResponse('{"status":"already_exists"}')

def viaEmail(email, leavel, registerTime,name):
    if len(passcet.models.passcet_user.objects.filter(email__exact=email)) == 0: #判断库里是不是已经有了相同的信息
        passcet.models.passcet_user.objects.create(email=email,leavel=leavel,registertime=registerTime,name=name)
        return HttpResponse('{"status": "rigister_success"}')
    else:
        return HttpResponse('{"status":"already_exists"}')

def storagePic(request,phone,email):
    img_file = request.FILES.get('image')
    if email == None:
        file_name = phone+time.time()+''
    else:
        file_name = email+time.time()+''
    f = open(os.path.join('img/',file_name),'wb')
    for chunk in img_file.chunks(chunk_size=1024):
        f.write(chunk)