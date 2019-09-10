from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import takelog,models
def getranklist(request):
    token = request.POST.get('token')
