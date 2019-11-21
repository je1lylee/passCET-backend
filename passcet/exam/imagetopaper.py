import urllib

import requests
from django.http import HttpResponse
from passcet.utils import *
from passcet.utils.takeLog import takelog
from passcet import settingfile as SF,models
import json,re #JSON和正则
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
            sendData = {
                'image': image
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            sendData = urllib.parse.urlencode(sendData).encode('utf-8')
            res = requests.post(
                'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic/?access_token=24.bc474b328d8b28ecd81caa80044fa343.2592000.1574841349.282335-17173201',
                data=sendData, headers=headers)
            LoJson = json.loads(res.text)
            count = LoJson.get("words_result_num")
            # print(LoJson.get("words_result")[0~count])
            result_list = []
            for i in range(count):
                result_list.append(LoJson.get("words_result")[i].get('words'))  
            print(result_list[2]) # 存储str
            QSet = models.passcet_paper.objects.filter(cetype=cetype,problem__contains='of')
            print(list(QSet.values()))
            return HttpResponse(SF.PASSCET_101_OK)
        else:
            print("TOKEN ERROR")
            takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        print("TOKEN?")
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)