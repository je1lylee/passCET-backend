from passcet import models
import time
def takelog(api_part,status):
    models.passcet_log.objects.create(api_part=api_part, status=status,
                                              time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))