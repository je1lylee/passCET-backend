from django.contrib import admin
from passcet.models import *
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','leavel','lastimei','logintime','registertime','img_md5')
    search_fields = ['id']
class emailcodeAdmin(admin.ModelAdmin):
    list_display = ('id','code','time')
    search_fields = ['code']
admin.site.register(passcet_user,userAdmin)
admin.site.register(passcet_emailcode,emailcodeAdmin)