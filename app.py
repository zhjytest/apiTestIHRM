
import logging.handlers
import os

#定义基础url：
BASE_URL = "http://182.92.81.159/"

CUR_PWD = os.path.abspath(__file__)
print(CUR_PWD)
BASE_DIR = os.path.dirname(CUR_PWD)
print(BASE_DIR)

TOKEN = "29520f86-e79d-4b6b-a6e3-843d0325dc5a"
headers_data = {"Content-Type":"application/json","Authorization":TOKEN}


#新建日志方法
def init_my_log():
    #创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #创建控制器输出器
    sh = logging.StreamHandler()
    #创建文件输出器
    file_log = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(file_log,when="midnight",interval=1,backupCount=7,encoding='utf-8')
    #创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formater = logging.Formatter(fmt)
    #把格式化加入输出器中
    sh.setFormatter(formater)
    fh.setFormatter(formater)
    #把输出器加入日志器
    logger.addHandler(sh)
    logger.addHandler(fh)