import traceback
from django.http import HttpResponse
import requests
import json
from passcet import settingfile as SF
from passcet import models
from passcet.utils.takeLog import takelog

# http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=ambition&_=1565436821302
# 直接请求上面儿的网址即可返回一个标准的json

def getword(request):
    token = request.POST.get('token')
    QueryWord = request.POST.get('word')
    if token!= SF.PASSCET_TOKEN or token == None:
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif QueryWord == None:
        takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        return HttpResponse(mainMethod(QueryWord))
def mainMethod(QueryWord):
    try:
        testString = ''
        resource_json = requests.get(
            'http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=' + QueryWord)
        json_res = json.loads(resource_json.text)  # 转换为dictionary
        print(json_res)
        try:  # 提前测试返回的json是否正常
            print(json_res['baesInfo']['word_name'])
            print(json_res['baesInfo']['symbols'][0]['ph_en'])
            print(json_res['baesInfo']['symbols'][0]['ph_am'])
            print(json_res['baesInfo']['symbols'][0]['ph_en_mp3'])
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
            takelog(__file__,SF.PASSCET_211_WORD_ERROR)
            return SF.PASSCET_211_WORD_ERROR
        # 开始存储数据
        if models.passcet_word.objects.filter(word=str(QueryWord)).count():
            models.passcet_word.objects.filter(word=str(QueryWord)).delete()
        # if 'cetFour' and 'cetSix' in json_res:
        if json_res.get('cetFour') and json_res.get('cetSix'):
            print('46都存在')
            models.passcet_word.objects.create(word=json_res['baesInfo']['word_name'],
                                               ph_en=json_res['baesInfo']['symbols'][0]['ph_en'],
                                               ph_am=json_res['baesInfo']['symbols'][0]['ph_am'],
                                               ph_en_mp3=json_res['baesInfo']['symbols'][0]['ph_en_mp3'],
                                               ph_am_mp3=json_res['baesInfo']['symbols'][0]['ph_am_mp3'],
                                               description=json.dumps(json_res['baesInfo']['symbols'][0]['parts']),
                                               sentence=json.dumps(json_res['sentence']),
                                               cet4=json.dumps(json_res['cetFour']['count']),
                                               cet6=json.dumps(json_res['cetSix']['count']))
        elif json_res.get('cetFour'):
            print(json_res['cetFour']['count'])
            models.passcet_word.objects.create(word=json_res['baesInfo']['word_name'],
                                               ph_en=json_res['baesInfo']['symbols'][0]['ph_en'],
                                               ph_am=json_res['baesInfo']['symbols'][0]['ph_am'],
                                               ph_en_mp3=json_res['baesInfo']['symbols'][0]['ph_en_mp3'],
                                               ph_am_mp3=json_res['baesInfo']['symbols'][0]['ph_am_mp3'],
                                               description=json.dumps(json_res['baesInfo']['symbols'][0]['parts']),
                                               sentence=json.dumps(json_res['sentence']),
                                               cet4=json.dumps(json_res['cetFour']['count']))
        elif json_res.get('cetSix'):
            print(json_res['cetSix']['count'])
            models.passcet_word.objects.create(word=json_res['baesInfo']['word_name'],
                                               ph_en=json_res['baesInfo']['symbols'][0]['ph_en'],
                                               ph_am=json_res['baesInfo']['symbols'][0]['ph_am'],
                                               ph_en_mp3=json_res['baesInfo']['symbols'][0]['ph_en_mp3'],
                                               ph_am_mp3=json_res['baesInfo']['symbols'][0]['ph_am_mp3'],
                                               description=json.dumps(json_res['baesInfo']['symbols'][0]['parts']),
                                               sentence=json.dumps(json_res['sentence']),
                                               cet4=json.dumps(json_res['cetSix']['count']))
        else:
            print('46都不存在')
            models.passcet_word.objects.create(word=json_res['baesInfo']['word_name'],
                                               ph_en=json_res['baesInfo']['symbols'][0]['ph_en'],
                                               ph_am=json_res['baesInfo']['symbols'][0]['ph_am'],
                                               ph_en_mp3=json_res['baesInfo']['symbols'][0]['ph_en_mp3'],
                                               ph_am_mp3=json_res['baesInfo']['symbols'][0]['ph_am_mp3'],
                                               description=json.dumps(json_res['baesInfo']['symbols'][0]['parts']),
                                               sentence=json.dumps(json_res['sentence']))
        # 数据存储结束
        # 开始检索数据库
        QuerySett = models.passcet_word.objects.filter(word=str(QueryWord))
        print(QuerySett)
        takelog(__file__,SF.PASSCET_101_OK)
        return json.dumps(list(QuerySett.values()))
    except:
        # 读取数据库中的缓存信息
        traceback.print_exc()
        try:
            QuerySett = models.passcet_word.objects.filter(word=str(QueryWord))
            print(QuerySett)
            takelog(__file__,SF.PASSCET_101_OK)
            return json.dumps(list(QuerySett.values()))
        except:
            takelog(__file__,SF.PASSCET_212_SEARCH_ERROR)
            return SF.PASSCET_212_SEARCH_ERROR