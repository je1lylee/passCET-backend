from django.http import HttpResponse
from passcet import settingfile as SF
from passcet.utils.takeLog import takelog
from passcet.utils import verifiyMailCode,verifiySmsCode
#author: NsuMicClub-Liguodong
def checkcode(request):
    token = request.GET.get('token')
    phoneNumber = request.GET.get('phone')
    id = request.GET.get('id')
    code = request.GET.get('code')
    if token == SF.PASSCET_TOKEN and code != None:
        if (phoneNumber != None):
            return verifiySmsCode(phoneNumber, code)
        elif (id != None):
            return verifiyMailCode(id, code)
    else:
        takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)