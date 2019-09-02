from django.http import HttpResponse
import time
import random
import passcet.models
import os
import hashlib
import filetype
from django.conf import settings
from passcet import settingfile as SF
from passcet import takelog
# Author:NsuMicClub-Liguodong

# 只有在验证码验证成功的时候才可以调用，这个方法就直接往数据库里写信息了
# 这里还没登录 所以不着急写入最后一次登录时间和设备的IMEI码
def addaccount(request):
    name = request.POST.get('name')
    token = request.POST.get('token')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    image = request.FILES.get('image')
    leavel = request.POST.get('leavel')
    if leavel == None:
        leavel = 0
    if token == SF.PASSCET_TOKEN and (phone != None or email != None) and name != None and image != None:
        rtime = time.time()  # Unix时间戳
        print(leavel)
        md5 = storagePic(request)
        if (phone != None):
            return viaPhone(phone, leavel, rtime,name,md5)
        else:
            return viaEmail(email, leavel, rtime,name,md5)
    else:
        take_log(SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
def viaPhone(phone, leavel, registerTime,name,md5):
    if len(passcet.models.passcet_user.objects.filter(phone__exact=phone)) == 0: #判断库里是不是已经有了相同的信息
        passcet.models.passcet_user.objects.create(phone=phone,leavel=leavel,registertime=registerTime,name=name,img_md5=md5)
        take_log(SF.PASSCET_106_REGISTER_SUCCESS)
        return HttpResponse(SF.PASSCET_106_REGISTER_SUCCESS)
    else:
        take_log(SF.PASSCET_206_DUPLICATE_USER)
        return HttpResponse(SF.PASSCET_206_DUPLICATE_USER)

def viaEmail(email, leavel, registerTime,name,md5):
    if len(passcet.models.passcet_user.objects.filter(email__exact=email)) == 0: #判断库里是不是已经有了相同的信息
        passcet.models.passcet_user.objects.create(email=email,leavel=leavel,registertime=registerTime,name=name,img_md5=md5)
        take_log(SF.PASSCET_106_REGISTER_SUCCESS)
        return HttpResponse(SF.PASSCET_106_REGISTER_SUCCESS)
    else:
        take_log(SF.PASSCET_206_DUPLICATE_USER)
        return HttpResponse(SF.PASSCET_206_DUPLICATE_USER)

def storagePic(request): # 存储头像 写文件的时候需要进行异常处理！
    img_file = request.FILES.get('image')
    md5ob = hashlib.md5()
    for chunk in img_file.chunks():#计算md5
        md5ob.update(chunk)
    md5 = md5ob.hexdigest()
    # 在数据库中完全匹配搜索MD5
    if len(passcet.models.passcet_user.objects.filter(img_md5__exact=md5)) ==0:
        print('直接写磁盘，并返回MD5')
        fname = settings.IMG_ROOT+md5+'.jpeg'
        with open(fname,'wb') as pic:
            for c in img_file.chunks():
                pic.write(c)
    else:
        print('数据库里有，直接写库')
    return md5
def take_log(status):
    takelog.takelog('addaccount',status)