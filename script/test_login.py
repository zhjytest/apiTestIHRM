#导包
import unittest
from api.login_api import LoginApi
import logging
from utils import common_assert
from app import TOKEN,headers_data,BASE_DIR
from parameterized import parameterized
import json

#构造数据方法
#[(),(),(),(),(),()]
#注释
def build_data():
    test_data = []
    with open(BASE_DIR+"/data/login.json",'r',encoding='utf-8') as f:
        datas = json.load(f)
        for data in datas:
            username = data.get('username')
            password = data.get('password')
            status_code = data.get('status_code')
            success = data.get('success')
            code = data.get('code')
            message = data.get('message')
            test_data.append((username,password,status_code,success,code,message))
    return test_data



#创建测试类
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = LoginApi()

    # 登录数据参数化
    @parameterized.expand(build_data)
    def test_login(self,username,password,status_code,success,code,message):
        # 初始化数据
        # username = "13800000002"
        # password = "123456"
        # 请求接口
        result = self.login.login(username, password)
        logging.info(result)
        # 断言
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(True,result.get('success'))
        # self.assertEqual(10000,result.get('code'))
        # self.assertIn("操作成功",result.get('message'))

        common_assert(self, result,status_code,success,code,message)

        # 设置token
        data_str = result.get('data')
        if data_str:
            TOKEN = "Bearer "+ data_str
            headers_data['Authorization'] = TOKEN

    #登录成功
    @unittest.skip
    def test_login_success(self):
        #初始化数据
        username = "13800000002"
        password = "123456"
        #请求接口
        result = self.login.login(username,password)
        logging.info(result)
        #断言
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(True,result.get('success'))
        # self.assertEqual(10000,result.get('code'))
        # self.assertIn("操作成功",result.get('message'))

        common_assert(self,result)

        #设置token
        TOKEN = "Bearer "+result.get('data')
        headers_data['Authorization'] = TOKEN
     


    #用户名不存在
    @unittest.skip
    def test_username_is_not_exist(self):
        #初始化数据
        username = "10800000002"
        password = "123456"
        #请求接口
        result = self.login.login(username,password)
        logging.info(result)
        #断言
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(False,result.get('success'))
        # self.assertEqual(20001,result.get('code'))
        # self.assertIn("用户名或密码错误",result.get('message'))
        common_assert(self,result,200,False,20001,"用户名或密码错误")


    #密码错误
    @unittest.skip
    def test_password_is_error(self):
        #初始化数据
        username = "13800000002"
        password = "error"
        #请求接口
        result = self.login.login(username,password)
        logging.info(result)
        #断言
        common_assert(self,result,200,False,20001,"用户名或密码错误")

    #用户名为空
    @unittest.skip
    def test_username_is_null(self):
        #初始化数据
        username = ""
        password = "123456"
        #请求接口
        result = self.login.login(username,password)
        logging.info(result)
        #断言
        common_assert(self,result,200,False,20001,"用户名或密码错误")

    #密码为空
    @unittest.skip
    def test_password_is_null(self):
        #初始化数据
        username = "13800000002"
        password = ""
        #请求接口
        result = self.login.login(username,password)
        logging.info(result)
        #断言
        common_assert(self,result,200,False,20001,"用户名或密码错误")

    #请求参数为空
    @unittest.skip
    def test_params_is_null(self):
        #初始化数据
        username = None
        password = None
        #请求接口
        result = self.login.login(username,password)
        logging.info(result)
        #断言
        common_assert(self,result,200,False,99999,"系统繁忙")
