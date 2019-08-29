import json

from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import models
from passcet import getword
# 添加单词到生词本
def addwordlist(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    word = request.POST.get('word')
    #description 通过getword从网络或数据库获取
    if token == None or token != SF.PASSCET_TOKEN:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif userid == None or word == None:
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        if models.passcet_user.objects.filter(id=userid).count():
            if models.passcet_glossary.objects.filter(user_id=userid,word=word).count():
                print('已存在！')
            else:
                # models.passcet_glossary.objects.create(user_id=userid,word=word,description=)
                finalQuery = str(getword.mainMethod(word))
                print(finalQuery)
        else:
            return HttpResponse(SF.PASSCET_205_USER_DOES_NOT_EXIST)

    return HttpResponse(SF.PASSCET_101_OK)