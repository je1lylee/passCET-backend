from django.http import HttpResponse
from passcet.models import passcet_user
from django.core.mail import send_mail
import passcet.models
from passcet import settingfile as SF
from passcet.utils.takeLog import takelog
import traceback


def sendFeedBackViaMail(mailaddress, feedbackcontent):
    try:
        print(mailaddress, feedbackcontent)
        passcet.models.passcet_feedback.objects.create(email=mailaddress, feedback=feedbackcontent)
    except:
        traceback.print_exc()
        takelog(__file__, SF.PASSCET_213_DB_ERROR)
        return HttpResponse(SF.PASSCET_213_DB_ERROR)
    try:
        send_mail('PassCET-用户反馈信息', '邮箱地址为' + mailaddress + '的用户提交了内容为[' + feedbackcontent + ']的反馈，请及时处理并向用户反馈！',
                  'passcetapp@163.com',
                  [SF.PASSCET_ADMIN_EMAIL_LIGUODONG, SF.PASSCET_ADMIN_MAIL_LIANJIE],
                  fail_silently=False)  # Fail silently 错误是否要提示？
        takelog(__file__, SF.PASSCET_112_FEED_BACK_EMAIL_SEND_SUCCESS)
        return HttpResponse(SF.PASSCET_112_FEED_BACK_EMAIL_SEND_SUCCESS)
    except:
        traceback.print_exc()  # console输出错误信息
        takelog(__file__, SF.PASSCET_216_FEED_BACK_EAMIL_SEND_ERROR)
        return HttpResponse(SF.PASSCET_216_FEED_BACK_EAMIL_SEND_ERROR)


def sendFeedBackViaPhone(phonenumber, feedbackcontent):
    try:
        print(phonenumber, feedbackcontent)
        passcet.models.passcet_feedback.objects.create(phone=phonenumber, feedback=feedbackcontent)
    except:
        traceback.print_exc()
        takelog(__file__, SF.PASSCET_213_DB_ERROR)
        return HttpResponse(SF.PASSCET_213_DB_ERROR)
    try:
        send_mail('PassCET-用户反馈信息', '手机号码为' + phonenumber + '的用户提交了内容为[' + feedbackcontent + ']的反馈，请及时处理并向用户反馈！',
                  'passcetapp@163.com',
                  [SF.PASSCET_ADMIN_EMAIL_LIGUODONG, SF.PASSCET_ADMIN_EMAIL_LIANJIE],
                  fail_silently=False)  # Fail silently 错误是否要提示？
        takelog(__file__, SF.PASSCET_112_FEED_BACK_EMAIL_SEND_SUCCESS)
        return HttpResponse(SF.PASSCET_112_FEED_BACK_EMAIL_SEND_SUCCESS)
    except:
        traceback.print_exc()  # console输出错误信息
        takelog(__file__, SF.PASSCET_216_FEED_BACK_EAMIL_SEND_ERROR)
        return HttpResponse(SF.PASSCET_216_FEED_BACK_EAMIL_SEND_ERROR)
