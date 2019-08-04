from django.http import HttpResponse
from passcet import models
from passcet import settingfile as SF
def getusericon(request):
    # Author: NsuMicClub:Liguodong
    """
    通过POST获取用户的id号并返回一张图片
    """
    if(request.POST.get('token')!= None and request.POST.get('token') == SF.PASSCET_TOKEN):
        id = request.POST.get('id')
        imageid = models.passcet_user.objects.filter(id=id)
        if len(imageid) != 0:
            imagedata = open('static/img/'+imageid[0].img_md5+'.jpeg','rb').read()
            return HttpResponse(imagedata,content_type='image/jpeg')
        else:
            return HttpResponse('{"status":"no-data"}')
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)