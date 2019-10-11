# 图片转词汇+释义
import urllib

from django.http import HttpResponse
from passcet import settingfile as SF
import requests
import json

def imagetoword(request):
    token = request.POST.get('token')
    image = request.POST.get('image')
    # testFiled = str(image).encode('utf8')
    sendData = {
        'image': image
    }
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    sendData = urllib.parse.urlencode(sendData).encode('utf-8')
    res = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic/?access_token=24.871b8e9b927215274362407024f7a450.2592000.1570160796.282335-17173201', data=sendData, headers=headers)
    print(res.text)
    return HttpResponse(process_json(res))

def process_json(json_string):
    # 去掉特殊符号 大写字母 空格 //考虑正则完成
    wordlist = []
    json_res = json.loads(json_string.text)
    word_list = json_res['words_result']
    test = '''dasd'''
    for i in word_list:
        word = i['words']
        word = word[2:]
        word = ''.join(word.split())
        print(word)
        wordlist.append(word)
    return json.dumps(wordlist)