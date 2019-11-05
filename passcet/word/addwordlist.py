import json

from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import models
from passcet.word import getword
from passcet.utils.takeLog import takelog
# 添加单词到生词本
def addwordlist(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    word = request.POST.get('word')
    #description 通过getword从网络或数据库获取
    if token == None or token != SF.PASSCET_TOKEN:
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif userid == None or word == None:
        takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        if models.passcet_user.objects.filter(id=userid).count():
            if models.passcet_glossary.objects.filter(user_id=userid,word=word).count():
                takelog(__file__,SF.PASSCET_214_WORD_EUPLICATE)
                return HttpResponse(SF.PASSCET_214_WORD_EUPLICATE)
            else:
                try:
                    models.passcet_glossary.objects.create(user_id=userid, word=word, description=json.loads(str(
                        getword.mainMethod(word)))[0]['description'])
                    takelog(__file__,SF.PASSCET_110_ADD_GLOSSARY_SUCCESS)
                    return HttpResponse(SF.PASSCET_110_ADD_GLOSSARY_SUCCESS)
                except:
                    takelog(__file__,SF.PASSCET_213_DB_ERROR)
                    return HttpResponse(SF.PASSCET_213_DB_ERROR)

        else:
            takelog(__file__,SF.PASSCET_205_USER_DOES_NOT_EXIST)
            return HttpResponse(SF.PASSCET_205_USER_DOES_NOT_EXIST)