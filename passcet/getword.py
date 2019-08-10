from django.http import HttpResponse



# 获取单词
# 通过向金山词霸的网址请求 返回json字符串，需要切掉前面的jQueryID(和字符串最后的')'
# 即可解析出json
# 需要忽略前41个字符和最后的一个字符
# http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C15%2C18%2C21%2C22%2C24%2C3003%2C3004%2C3005&word=ambition&_=1565436821302
# 直接请求上面儿的网址即可返回一个标准的json

def getword(request):
    return HttpResponse()