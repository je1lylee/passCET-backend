from django.http import HttpResponse
def loginstatuscheck(request):
    id = request.POST.get('id')
    time = request.POST.get('time') #从安卓本地的存储中返回上一次验证登录的时间
    imei = request.POST.get('imei')
    return HttpResponse('success')