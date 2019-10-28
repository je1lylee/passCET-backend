from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import takelog,models
def getranklist(request):
    """
    获取学习时长排行榜
    :param request:
    :return:
    """
    token = request.POST.get('token')
