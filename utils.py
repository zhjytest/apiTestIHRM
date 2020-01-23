import pymysql


#公共的断言
def common_assert(test_case,result,status_code=200,success=True,code=10000,message="操作成功"):
    test_case.assertEqual(status_code, result.get('status_code'))
    test_case.assertEqual(success, result.get('success'))
    test_case.assertEqual(code, result.get('code'))
    test_case.assertIn(message, result.get('message'))


#公共的返回json
def get_json(response):
    result = response.json()
    result['status_code'] = response.status_code
    return result


#公共的类
class Mysql(object):

    def __init__(self):
        self.conn = pymysql.connect("182.92.81.159","readuser","iHRM_user_2019","ihrm")


    #查询一条数据
    def get_one(self,sql,pararms=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql,pararms)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

