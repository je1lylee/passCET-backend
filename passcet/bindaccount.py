from django.http import HttpResponse
from passcet import settingfile as SF
# 检查账号是否存在，如果存在检查将要绑定的手机或邮箱是不是已经被绑定过了
def bindaccount(request):
    token = request.POST.get('token')
    type = request.POST.get('type')
    # 0:已经绑定邮箱，需要绑定手机号；1：已经绑定手机需要绑定邮箱
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    id = request.POST.get('id')
    code = request.POST.get('code')
    #验证TOKEN
    if token != None and token == SF.PASSCET_TOKEN:
        print('')
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)