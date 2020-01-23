#导包
import json
import unittest
from api.employee_api import EmployeeApi
import logging
from utils import common_assert,Mysql
from parameterized import parameterized
from app import BASE_DIR

#获取新增数据的构造器
[(),()]
def add_build_data():
    test_data = []
    with open(BASE_DIR+"/data/employee.json",encoding='utf-8') as f:
        datas = json.load(f)
        add_emp_data = datas.get('add_emp_data')
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        work_number = add_emp_data.get('work_number')
        status_code = add_emp_data.get('status_code')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')
        test_data.append((username,mobile,work_number,status_code,success,code,message))
    return test_data

#获取查询数据
def search_build_data():
    test_data = []
    with open(BASE_DIR+"/data/employee.json","r",encoding="utf-8") as f:
        datas = json.load(f)
        search_emp_data = datas.get('search_emp_data')
        status_code = search_emp_data.get('status_code')
        success = search_emp_data.get('success')
        code = search_emp_data.get('code')
        message = search_emp_data.get('message')
        test_data.append((status_code,success,code,message))
    return test_data

#获取修改数据
def update_build_data():
    test_data = []
    with open(BASE_DIR + "/data/employee.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        update_emp_data = datas.get('update_emp_data')
        username = update_emp_data.get('username')
        status_code = update_emp_data.get('status_code')
        success = update_emp_data.get('success')
        code = update_emp_data.get('code')
        message = update_emp_data.get('message')
        test_data.append((username,status_code, success, code, message))
    return test_data

#获取删除数据
def delete_build_data():
    test_data = []
    with open(BASE_DIR + "/data/employee.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        delete_emp_data = datas.get('delete_emp_data')
        status_code = delete_emp_data.get('status_code')
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')
        test_data.append((status_code,success,code,message))
    return test_data

#新建类
class TestEmployee(unittest.TestCase):

    emp_id = ""

    @classmethod
    def setUpClass(cls):
        cls.emp = EmployeeApi()


    #新增
    @parameterized.expand(add_build_data)
    def test01_add_emp(self,username,mobile,work_number,status_code,success,code,message):
        #初始化数据
        # username= 'tom_10'
        # mobile = "17010001010"
        # work_number = "1010"
        #请求接口
        result = self.emp.add_emp(username,mobile,work_number)
        logging.info("新增：{}".format(result))
        #断言
        common_assert(self,result,status_code,success,code,message)

        #获取员工id
        TestEmployee.emp_id = result.get('data').get('id')

    #查询
    @parameterized.expand(search_build_data)
    def test02_search_emp(self,status_code,success,code,message):
        #初始化数据
        #请求接口
        result = self.emp.search_emp(TestEmployee.emp_id)
        logging.info("查询：{}".format(result))
        #断言
        common_assert(self,result,status_code,success,code,message)

    #修改
    @parameterized.expand(update_build_data)
    def test03_update_emp(self,username,status_code, success, code, message):
        #初始化数据
        #username = "tom_new"
        #请求接口
        result = self.emp.update_emp(TestEmployee.emp_id,username)
        logging.info("修改：{}".format(result))
        #断言
        common_assert(self,result,status_code, success, code, message)
        # #导包
        # import pymysql
        # #创建数据库连接
        # conn = pymysql.connect("182.92.81.159","readuser","iHRM_user_2019","ihrm")
        # #创建游标
        # cursor = conn.cursor()
        # #执行操作
        # sql = "select username from bs_user where id = %s"
        # cursor.execute(sql,TestEmployee.emp_id)
        # one = cursor.fetchone()
        # logging.info("one:{}".format(one))
        # uname = one[0]
        # self.assertEqual(username,uname)
        # #关闭游标
        # cursor.close()
        # #关闭数据库连接
        # conn.close()
        sql = "select username from bs_user where id = %s"
        mysql = Mysql()
        one = mysql.get_one(sql,TestEmployee.emp_id)
        uname = one[0]
        self.assertEqual(username, uname)

    #删除
    @parameterized.expand(delete_build_data)
    def test04_delete_emp(self,status_code,success,code,message):
        #初始化数据
        #请求接口
        result = self.emp.delete_emp(TestEmployee.emp_id)
        logging.info("删除：{}".format(result))
        #断言
        common_assert(self,result,status_code,success,code,message)