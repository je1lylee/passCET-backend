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
    :param request:
    :return:
    """
    token = request.POST.get('token')
    word = request.POST.get('word')
    if token is not None and token == SF.PASSCET_TOKEN:
        if word is not None:
            try:
                testString = ''
                resource_json = requests.get(
                    'http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=' + word)
                json_res = json.loads(resource_json.text)  # 转换为dictionary
                print(json_res)
                # noinspection PyBroadException
                try:  # 提前测试返回的json是否正常
                    print(json_res['baesInfo']['word_name'])
                    print(json_res['baesInfo']['symbols'][0]['ph_en']) #音标
                    print(json_res['baesInfo']['symbols'][0]['ph_am'])
                    print(json_res['baesInfo']['symbols'][0]['ph_en_mp3'])# 读音
                    print(json_res['baesInfo']['symbols'][0]['ph_am_mp3'])
                    # print(json_res['baesInfo']['symbols'][0]['parts'][0]) # 遍历List
                    demoString = json.dumps(json_res['baesInfo']['symbols'][0])
                    print('测试字符串' + demoString)
                    for i in json_res['baesInfo']['symbols'][0]['parts']:
                        testString = testString + json.dumps(i) + ','
                        # print(i)  释义
                    print(testString)
                    print(json.dumps(json_res['sentence']))  # 例句
                except:
                    traceback.print_exc()
                    takelog(__file__, SF.PASSCET_211_WORD_ERROR)
                    return SF.PASSCET_211_WORD_ERROR
            except:
                # 读取数据库中的缓存信息
                traceback.print_exc()
                try:
                    QuerySett = models.passcet_word.objects.filter(word=str(word))
                    print(QuerySett)
                    takelog(__file__, SF.PASSCET_101_OK)
                    return json.dumps(list(QuerySett.values()))
                except:
                    takelog(__file__, SF.PASSCET_212_SEARCH_ERROR)
                    return SF.PASSCET_212_SEARCH_ERROR
        else:
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    return HttpResponse(SF.PASSCET_101_OK)