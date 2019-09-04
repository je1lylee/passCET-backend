# 图片转词汇+释义
from django.http import HttpResponse
from passcet import settingfile as SF
from aip import AipOcr
def imagetoword(request):
    token = request.POST.get('token')
    image = request.POST.get('image')  # IMAGE直接传JPG/PNG 由服务器转换为BASE6
    # testFiled = str(image).encode('utf8')
    testFiled = bytes(str(image),encoding='utf8')
    testFiled.decode()
    print(type(testFiled))
    print(testFiled)
    APP_ID= '17173201'
    API_KEY='pZ9gmceDPZB38yOpZuOtZcOt'
    SECRET_KEY='Y4EBwVZvcoVVXVZbgjKVuiNmCyHT9gpD'
    client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
    print(client.basicGeneral(testFiled))
    return HttpResponse(SF.PASSCET_101_OK)