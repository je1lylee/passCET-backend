import json
import traceback

import requests
from django.http import HttpResponse
from passcet.utils import *
from passcet import settingfile as SF, models
from passcet.utils.takeLog import takelog


def getbriefword(request):
    """
    调用此接口来获得单词的音标，读音和相关释义。
    此接口是getword的简化版本
    此部分接口获取到的数据暂时不在数据库中进行缓存
    :param request:
    :return:
    """
    token = request.POST.get('token')
    word = request.POST.get('word')
    if token is not None and token == SF.PASSCET_TOKEN:
        if word is not None:
            testString = ''
            responseDirc = {}
            resource_json = requests.get(
                'http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=' + word)
            json_res = json.loads(resource_json.text)  # 转换为dictionary
            print(json_res)
            # except需指定异常类型，加上面这句话可以忽略
            try:  # 提前测试返回的json是否正常
                print(json_res['baesInfo']['word_name']) #单词
                print(json_res['baesInfo']['symbols'][0]['ph_en'])  # 音标
                print(json_res['baesInfo']['symbols'][0]['ph_am'])
                print(json_res['baesInfo']['symbols'][0]['ph_en_mp3'])  # 读音
                print(json_res['baesInfo']['symbols'][0]['ph_am_mp3'])
                demoString = json.dumps(json_res['baesInfo']['symbols'][0])
                print('测试字符串' + demoString)
                for i in json_res['baesInfo']['symbols'][0]['parts']:
                    testString = testString + json.dumps(i) + ','
                print('TESTSTRING///'+testString)
            except:
                traceback.print_exc()
                takelog(__file__, SF.PASSCET_211_WORD_ERROR)
                return SF.PASSCET_211_WORD_ERROR
        else:
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    return HttpResponse(SF.PASSCET_101_OK)
