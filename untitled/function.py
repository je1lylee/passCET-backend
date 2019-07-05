from django.http import *
import json
from django.http import HttpResponse

def home(request):
    result = {"status": "错误", "data": "", "city": "北京"}
    # json返回为中文
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")
    #设置content_type后中文乱码问题解决