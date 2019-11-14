from django.db import models


# 用户
class passcet_user(models.Model):
    name = models.CharField(max_length=30)  # 昵称 可以为空？
    email = models.CharField(max_length=60, null=True)  # email 电话和邮件有一个即可
    phone = models.IntegerField(null=True)  # 电话号码
    img_md5 = models.CharField(max_length=128, default=0)  # 头像的MD5
    leavel = models.IntegerField(null=False, default=0)  # 学习等级 0为未设置 4是band4 6是band6
    logintime = models.IntegerField(null=False, default=0)  # 最后一次登录时间，为了保持登录状态
    registertime = models.IntegerField(null=False, default=0)  # 注册时间
    lastimei = models.IntegerField(null=True, default=0)  # 最后一次登录的设备特征号

    def __str__(self):
        return self.name


# 邮箱验证码
class passcet_emailcode(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    time = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


# 单词
class passcet_word(models.Model):
    word = models.CharField(max_length=128, null=False)  # 单词名字
    ph_en = models.CharField(max_length=128, default=0)  # 英式音标
    ph_am = models.CharField(max_length=128, default=0)  # 美式音标
    ph_en_mp3 = models.CharField(max_length=128, default=0)  # 英式发音
    ph_am_mp3 = models.CharField(max_length=128, default=0)  # 美式发音
    description = models.TextField(default=0)  # 单词释义
    sentence = models.TextField(default=0)  # 单词例句
    cet4 = models.TextField(default=0)  # 四级词频
    cet6 = models.TextField(default=0)  # 六级词频

    def __str__(self):
        return str(self.word)


# 用户生词本
class passcet_glossary(models.Model):
    user_id = models.IntegerField(null=False)  # 用户id
    word = models.CharField(max_length=128, null=False)  # 单词内容
    description = models.TextField(max_length=128, null=False)  # 单词的简单释义

    def __str__(self):
        return str(self.user_id) + '\'s' + str(self.word)


# 学习时长
class passcet_time(models.Model):
    userid = models.IntegerField(null=False)  # 用户的ID号
    learningtime = models.IntegerField(null=False)  # 用户的本次学习时长
    datetime = models.IntegerField(null=False)  # 用户的学习日期，通过UNIX时间戳存储

    def __str__(self):
        return str(self.userid) + '\'s' + str(self.learningtime)


# 用户排行榜
class passcet_ranklist(models.Model):
    userid = models.IntegerField(null=False)
    username = models.CharField(max_length=128, null=False)
    totaltime = models.IntegerField(null=False)

    def __str__(self):
        return str(self.userid) + '\'s' + str(self.totaltime)


# 日志系统
class passcet_log(models.Model):
    api_part = models.TextField(max_length=128, null=False)  # 调用API的名字
    status = models.TextField(max_length=128, null=False)
    time = models.TextField(max_length=128, null=False)

    def __str__(self):
        return str(self.api_part) + '##' + str(self.status)

# 用户反馈系统
class passcet_feedback(models.Model):
    phone = models.IntegerField(default=-1)
    #用户常用的phone/email
    email = models.CharField(max_length=128, default=-1)
    feedback = models.TextField(max_length=256, null=False)
    isChecked = models.BooleanField(default=False)
    def __str__(self):
        if self.phone == -1:
            return str(self.email)+str(self.feedback)
        else:
            return str(self.phone)+str(self.feedback)
