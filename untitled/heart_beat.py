from django.http import HttpResponse
def home(request):
    tips = request.GET.get('tips')
    return HttpResponse('您输入的参数为:'+tips)