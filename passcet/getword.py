from django.http import HttpResponse
import requests
import json
from passcet import settingfile as SF
from passcet import models

# http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=ambition&_=1565436821302
# 直接请求上面儿的网址即可返回一个标准的json

def getword(request):
    testString = ''
    resource_json = requests.get('http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=ambition&_=1565436821302')
    json_res = json.loads(resource_json.text) #转换为dictionary
    print(json_res['baesInfo']['word_name'])
    print(json_res['baesInfo']['symbols'][0]['ph_en'])
    print(json_res['baesInfo']['symbols'][0]['ph_am'])
    print(json_res['baesInfo']['symbols'][0]['ph_en_mp3'])
    print(json_res['baesInfo']['symbols'][0]['ph_am_mp3'])
    print(json_res['baesInfo']['symbols'][0]['parts'][0]) # 遍历List
    for i in json_res['baesInfo']['symbols'][0]['parts']:
        testString = testString+i
        # print(i)  释义
    print(testString)
    print(json_res['sentence']) #例句
    if 'cetFour' in json_res:
        print(json_res['cetFour']['count'])
    if 'cetSix' in json_res:
        print(json_res['cetSix']['count'])
    return HttpResponse(SF.PASSCET_101_OK)