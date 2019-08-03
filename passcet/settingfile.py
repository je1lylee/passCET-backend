# 参数设置
PASSCET_TOKEN = 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW'

# 错误返回
PASSCET_201_TOKEN_ERROR = '{"code":201,"status":"Token错误"}'
PASSCET_202_PARAMETER_ERROR = '{"code":202,"status":"缺少参数"}'
PASSCET_204_EMAIL_SEND_FAILED = '{"code":204,"status":"E-MAIL发送失败"}'
PASSCET_205_USER_DOES_NOT_EXIST = '{"code":205,"status":"用户不存在"}'
PASSCET_206_DUPLICATE_USER = '{"code":206,"status":"重复的电话号码或邮箱"}'
# 正确返回
PASSCET_102_SEND_PHONE_MESSAGE_OK = '{"code":102,"status":"成功发送短信验证码"}'
PASSCET_103_SEND_EMAIL_MESSAGE_OK = '{"code":103,"status":"成功发送邮箱验证码验证码","id":"'
PASSCET_104_CHECK_EMAIL_MESSAGE_OK = '{"code":104,"status":"邮箱验证码验证成功"}'