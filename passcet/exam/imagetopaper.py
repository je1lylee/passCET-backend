import urllib

import requests
from django.http import HttpResponse
from passcet.utils import *
from passcet.utils.takeLog import takelog
from passcet import settingfile as SF,models
import json
def imagetopaper(request):
    """
    通过识别图片来对数据库进行模糊查询以获取题目和相应释义
    :param request:
    :return:
    """
    token = request.POST.get('token')
    image = request.POST.get('image') # BASE64
    cetype = request.POST.get('cetype')
    if token is not None and token == SF.PASSCET_TOKEN:
        if image is not None and cetype is not None:
            #开始执行逻辑
            pass
        else:
            print("TOKEN ERROR")
            takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        print("TOKEN?")
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)