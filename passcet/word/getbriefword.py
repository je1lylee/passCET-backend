from django.http import HttpResponse
from passcet.utils import *
from passcet import settingfile as SF


def getbriefword(request):
    """
    调用此接口来获得单词的音标，读音和相关释义。
    :param request:
    :return:
    """
    token = request.POST.get('token')
    word = request.POST.get('word')
    if token is not None and token == SF.PASSCET_TOKEN:
        if word is not None:
            #开始执行逻辑
            pass
        else:
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    return HttpResponse(SF.PASSCET_101_OK)