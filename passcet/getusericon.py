from django.http import HttpResponse
from passcet import models
def getusericon(request):
    """
    通过POST获取用户的id号并返回一张图片
    """
    id = request.POST.get('id')
    imageid = models.passcet_user.objects(id=id)
    return HttpResponse('success')