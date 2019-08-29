from django.contrib import admin
from passcet.models import *
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','leavel','lastimei','logintime','registertime','img_md5')
    search_fields = ['id']
class emailcodeAdmin(admin.ModelAdmin):
    list_display = ('id','code','time')
    search_fields = ['code']
class wordAdmin(admin.ModelAdmin):
    list_display = ('id','word','ph_en','ph_am','ph_en_mp3','ph_am_mp3','description','sentence','cet4','cet6')
    search_fields = ['word']
class glossaryAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','word','description')
    search_fields = ['word']
admin.site.register(passcet_user,userAdmin)
admin.site.register(passcet_emailcode,emailcodeAdmin)
admin.site.register(passcet_word,wordAdmin)
admin.site.register(passcet_glossary,glossaryAdmin)