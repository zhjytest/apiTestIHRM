#导包
import unittest
from script.test_login import TestLogin
from script.test_employee import TestEmployee
from app import BASE_DIR
from tools.HTMLTestRunner import HTMLTestRunner
#组装测试用例
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))

#生成测试报告
with open(BASE_DIR+"/report/report.html","wb") as f:
    runner = HTMLTestRunner(f,title="ihrm测试报告",description="v1.0")
    runner.run(suite)