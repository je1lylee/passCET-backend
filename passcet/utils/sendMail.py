from django.http import HttpResponse
from passcet.models import passcet_user
from django.core.mail import send_mail
import time
import random
import passcet.models
from passcet import settingfile as SF
from passcet import takelog
import traceback
def sendMail(emailAddress):
    # 处理发邮件的逻辑 返回发送状态
    # 生成两个随机数，一个作为ID一个作为Code 加上时间戳 10min 就是10*60=600 sec
    # 这里可能需要编写一个经常运行的程序来保证验证码表在凌晨两点进行清空
    curlTime = time.time()
    id = random.randint(100000, 999999)
    code = random.randint(100000, 999999)
    # 需要存入数据库并在验证方法中进行验证
    try:
        passcet.models.passcet_emailcode.objects.create(id=id, code=code, time=curlTime)
        send_mail('PassCET-验证邮件', '您的验证码是[' + str(code) + ']，有效期10分钟。如非本人操作,请忽略。', 'passcetapp@163.com', [emailAddress],
                  fail_silently=False)
        take_log(SF.PASSCET_103_SEND_EMAIL_MESSAGE_OK + str(id) + '"}')
        return HttpResponse(SF.PASSCET_103_SEND_EMAIL_MESSAGE_OK + str(id) + '"}')
    except:
        traceback.print_exc()  # console输出错误信息
        take_log(SF.PASSCET_204_EMAIL_SEND_FAILED)
        return HttpResponse(SF.PASSCET_204_EMAIL_SEND_FAILED)

def take_log(filename,status):
    takelog.takelog(__file__, status)