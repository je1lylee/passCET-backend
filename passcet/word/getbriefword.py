from django.http import HttpResponse
from passcet.utils import *
from passcet import settingfile as SF


def getbriefword(request):
    """
    调用此接口来获得单词的音标，读音和相关释义。
    :param request:
    :return:
    """
    return HttpResponse(SF.PASSCET_101_OK)