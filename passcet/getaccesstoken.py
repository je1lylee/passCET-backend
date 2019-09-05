# 定期获取百度的access_token
import requests
def getaccesstoken():
    raw_token =requests.get('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=pZ9gmceDPZB38yOpZuOtZcOt&client_secret=Y4EBwVZvcoVVXVZbgjKVuiNmCyHT9gpD')
    print(type(raw_token))
    print(raw_token.text)
if __name__ == '__main__':
    getaccesstoken()