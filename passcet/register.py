from django.http import HttpResponse
from passcet.models import passcet_user
from passcet import settingfile as SF
from passcet.utils.takeLog import takelog
from passcet.utils import sendMail,sendSms


# Author :NsuMicClub-Liguodong
# URL register/?token= & phone = & email = //token必填 phone和email任选一个即可
# 传入参数 email或者是phone 判断如果email或者是phone重复就返回错误
# 如果没毛病就调用“请求短信验证码”返回一个验证码并返回成功的验证码
def register(request):
    # 处理登录的请求
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    token = request.GET.get('token')
    if phone == None and email == None:
        takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    elif token == SF.PASSCET_TOKEN:  # 对token进行验证 如果正确才执行逻辑
        if phone == None:
            phone = 0
        elif email == None:
            email = 0
        username = passcet_user.objects.all()  # 从数据库中拿到集合
        for usernames in username:  # 轮询没问题后再执行发送相关的逻辑
            print(usernames.email)
            print(usernames.phone)
            if email == usernames.email or phone == str(usernames.phone):
                takelog(__file__,SF.PASSCET_206_DUPLICATE_USER)
                return HttpResponse(SF.PASSCET_206_DUPLICATE_USER)  # 出现重复的手机号或密码时进行检测
        if phone != 0:  # 如果phone里传过来了参数就发送短信
            return sendSms(phone)
        if email != 0:  # 如果email里传过来了参数就发送电子邮件
            return sendMail(email)
    else:
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)  # token错误