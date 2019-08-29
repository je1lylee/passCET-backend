# 从生词本中删除单词
from passcet import settingfile as SF
from django.http import HttpResponse
from passcet import models
def delwordlist(request):
    token = request.POST.get('token')
    user_id = request.POST.get('userid')
    word = request.POST.get('word')
    if token != SF.PASSCET_TOKEN or token == None:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif user_id == None or word == None:
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        if models.passcet_glossary.objects.filter(user_id = user_id,word = word).count():
            models.passcet_glossary.objects.filter(user_id= user_id,word=word).delete()
            return HttpResponse(SF.PASSCET_111_DEL_GLOSSARY_SUCCESS)
        else:
            return HttpResponse(SF.PASSCET_215_GLOSSARY_NO_DATA)
    return HttpResponse(SF.PASSCET_101_OK)