import urllib

import requests
from django.http import HttpResponse
from passcet.utils import *
from passcet.utils.takeLog import takelog
from passcet import settingfile as SF, models
import json, re  # JSON和正则


def imagetopaper(request):
    """
    通过识别图片来对数据库进行模糊查询以获取题目和相应释义
    :param request:
    :return:
    """
    token = request.POST.get('token')
    image = request.POST.get('image')  # BASE64
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
                'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic/?access_token=24.76322b8bb87c553728bffbf0baa19c8e.2592000.1577497316.282335-17173201',
                data=sendData, headers=headers)
            LoJson = json.loads(res.text)
            count = LoJson.get("words_result_num")
            # print(LoJson.get("words_result")[0~count])
            result_list = []
            modelss = ['in', 'on', 'with', 'by', 'for', 'at', 'about', 'under', 'of', 'a', 'an', '-', 'Directions',
                       'For', 'this', 'that', 'part', 'you']  # 这里可继续优化以提高准确性
            comp = re.compile('[^A-Z^a-z^0-9^]')
            # result_list.append(LoJson.get("words_result")[i].get('words'))
            # 从result中取出关键词，过滤方法：过滤长度小于5的单词和常见的英语介词（in，on，with，by，for，at，about，under，of）和标点符号
            for i in range(count):  # 取出百度的结果集
                resultSet = LoJson.get("words_result")[i].get('words')  # 获取到百度返回的一段话
                resultSet = comp.sub(' ', resultSet)
                resultSet = resultSet.split()
                for i in resultSet:
                    if i not in modelss and len(i) > 5:
                        result_list.append(i)
            print(result_list)
            print(cetype)
            for i in range(len(result_list)):  # 遍历
                databaseQ = models.passcet_paper.objects.filter(cetype=cetype, problem__icontains=result_list[i])
                if len(databaseQ) == 1:
                    result = list(databaseQ.values())
                    return HttpResponse(json.dumps(result))
            else:
                return HttpResponse('NO RESULT IN DATABASE!!')
            # QSet = models.passcet_paper.objects.filter(cetype=cetype, problem__icontains=result_list[2])
            # print(json.dumps(list(QSet.values())))
        else:
            print("TOKEN ERROR")
            takelog(__file__, SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        print("TOKEN?")
        takelog(__file__, SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
