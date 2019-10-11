from django.http import HttpResponse
from passcet import models
from passcet import settingfile as SF
from passcet import takelog
def getusericon(request):
    # Author: NsuMicClub:Liguodong
    """
    通过POST获取用户的id号并返回一张图片
    """
    if(request.POST.get('token')!= None and request.POST.get('token') == SF.PASSCET_TOKEN):
        id = request.POST.get('id')
        imageid = models.passcet_user.objects.filter(id=id) #此处即判断用户ID是否存在
        if len(imageid) != 0:#此处即判断用户ID是否存在
            imagedata = open('static/img/'+imageid[0].img_md5+'.jpeg','rb').read()
            take_log(SF.PASSCET_101_OK)
            return HttpResponse(imagedata,content_type='image/jpeg')
        else:
            take_log(SF.PASSCET_210_NO_IMG_DATA)
            return HttpResponse(SF.PASSCET_210_NO_IMG_DATA)
    else:
        take_log(SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)

def take_log(status):
    takelog.takelog('getusericon',status)