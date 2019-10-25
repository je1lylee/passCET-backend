from passcet import models
import time
import os


def takelog(api_part, status):
    """
    在数据库中记录日志信息
    :param api_part: api的模块名，使用__file__直接传入模块的文件名。
    :param status:
    :return:空
    :action:写数据库
    """
    api_part = os.path.basename(api_part)[:-3]  # 切掉 .py
    models.passcet_log.objects.create(api_part=api_part, status=status,
                                      time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
