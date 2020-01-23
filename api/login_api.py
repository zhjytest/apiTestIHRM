#导包
import requests
from app import BASE_URL
from utils import get_json

#创建类
class LoginApi():

    def __init__(self):
        self.login_url = BASE_URL + "/api/sys/login"

    #登录接口
    def login(self,mobile,password):
        #response = None
        result = {}
        login_data = {}
        if mobile:
            login_data['mobile'] = mobile
        if password:
            login_data['password'] = password
        if login_data:
            response = requests.post(self.login_url,json=login_data)
        else:
            response = requests.post(self.login_url)
        # result = response.json()
        # status_code = response.status_code
        # result['status_code'] = status_code
        # return result
        return get_json(response)

