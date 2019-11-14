from django.http import HttpResponse
from passcet.utils import *
from passcet import settingfile as SF


def checkversion(request):
    """
    检查应用程序的版本
    :param request:
    :return:如果版本为最新返回对应的返回码。
    如果需要更新则返回对应的返回码，
    """
    token = request.POST.get('token')
    version = request.POST.get('version')
    pass
