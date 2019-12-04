from django.http import HttpResponse
from passcet.utils import *
from passcet import settingfile as SF


def getexamaudio(request):
    """
    通过exam获取发音URL
    :param request:
    :return:
    """
    token = request.POST.get('token')
    exam = request.POST.get('exam')
    print(token)
    if token is not None and token == SF.PASSCET_TOKEN:
        if exam is not None:
            try:
                f = open('static/audio/' + exam + '.mp3', 'rb').read()
                return HttpResponse(f, content_type='audio/mp3')
            except:
                #文件不存在或打开文件异常
                pass
        else:
            return HttpResponse('para')
    else:
        return HttpResponse('token')
