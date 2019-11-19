from django.http import HttpResponse
from passcet.utils import *
from passcet import settingfile as SF


def checkversion(request):
    """
    检查应用程序的版本
    :param request:
    :return:如果版本为最新返回对应的返回码。
    如果需要更新则返回对应的返回码，
    """
    token = request.POST.get('token')
    version = request.POST.get('version')
    if token is not None and token == SF.PASSCET_TOKEN:
        if version is not None:
            # 开始执行逻辑
            if version == SF.PASSCET_VERSION:
                return HttpResponse(SF.PASSCET_113_VERSION_CHECK_OK)
            else:
                return HttpResponse(SF.PASSCET_217_VERSION_CHECK_FAILED)
        else:
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
