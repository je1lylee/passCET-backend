from django.http import HttpResponse
from passcet.utils import takeLog, sendFeedInfo
from passcet import settingfile as SF, models


def pushfeedback(request):
    """
    用户反馈接口，获取到反馈信息后发送邮件给管理员
    当用户同时输入邮箱地址和电话时，会优先选择邮箱
    :param request:
    :return:
    """
    token = request.POST.get('token')
    mail = request.POST.get('mail')
    phone = request.POST.get('phone')
    content = request.POST.get('content')
    if token is not None and token == SF.PASSCET_TOKEN:
        if mail is not None or phone is not None and content is not None:
            # 开始执行逻辑
            if mail is not None:
                return sendFeedInfo.sendFeedBackViaMail(mail, content)
            else:
                return sendFeedInfo.sendFeedBackViaPhone(phone, content)
        else:
            takeLog.takelog(__file__, SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        takeLog.takelog(__file__, SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
