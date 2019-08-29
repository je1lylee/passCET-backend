# Powered By Aquarius Engine
# 参数设置
PASSCET_TOKEN = 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW'

# 错误返回
PASSCET_201_TOKEN_ERROR = '{"code":201,"status":"Token错误"}'
PASSCET_202_PARAMETER_ERROR = '{"code":202,"status":"缺少参数或参数错误"}'
PASSCET_203_NEED_LOGIN = '{"code":"203","status":"需要重新登录"}'
PASSCET_204_EMAIL_SEND_FAILED = '{"code":204,"status":"E-MAIL发送失败"}'
PASSCET_205_USER_DOES_NOT_EXIST = '{"code":205,"status":"用户不存在"}'
PASSCET_206_DUPLICATE_USER = '{"code":206,"status":"重复的电话号码或邮箱"}'
PASSCET_207_PHONE_MESSAGE_ERROR = '{"code":207,"status":"短信验证码错误"}'
PASSCET_208_EMAIL_MESSAGE_ERROR = '{"code":208,"status":"邮箱验证码错误"}'
PASSCET_209_PHONE_MESSAGE_ID_ERROR = '{"code":209,"status":"邮箱验证码ID不存在"}'
PASSCET_210_NO_IMG_DATA = '{"code":210,"status":"图片数据不存在"}'
PASSCET_211_WORD_ERROR = '{"code":211,"status":"查询的单词错误或单词不存在"}'
PASSCET_212_SEARCH_ERROR = '{"code":212,"status":"无法在线查询词汇，且数据库内没有缓存数据"}'
PASSCET_213_DB_ERROR = '{"code":213,"status":"数据库异常"}'
PASSCET_214_WORD_EUPLICATE = '{"code":214,"status":"用户生词本中已存在该单词"}'
PASSCET_215_GLOSSARY_NO_DATA = '{"code":215,"status":"用户生词本中不存在该单词"}'
# 正确返回
PASSCET_101_OK = '{"code":101,"status":"成功"}' #仅用作测试
PASSCET_102_SEND_PHONE_MESSAGE_OK = '{"code":102,"status":"成功发送短信验证码"}'
PASSCET_103_SEND_EMAIL_MESSAGE_OK = '{"code":103,"status":"成功发送邮箱验证码验证码","id":"'
PASSCET_104_CHECK_PHONE_MESSAGE_OK = '{"code":104,"status":"短信验证码验证成功"}'
PASSCET_105_CHECK_EMAIL_MESSAGE_OK = '{"code":105,"status":"邮箱验证码验证成功"}'
PASSCET_106_REGISTER_SUCCESS = '{"code":106,"status":"成功注册"}'
PASSCET_107_USERINFO_CHECK_SUCCESS = '{"code":107,"status":"验证成功"}'
PASSCET_108_BIND_PHONE_SUCCESS = '{"code":108,"status":"手机号绑定成功"}'
PASSCET_109_BIND_EMAIL_SUCCESS = '{"code":109,"status":"邮箱绑定成功"}'
PASSCET_110_ADD_GLOSSARY_SUCCESS = '{"code":110,"status":"单词已添加到生词本"}'
PASSCET_111_DEL_GLOSSARY_SUCCESS = '{"code":110,"status":"单词已从生词本中移除"}'