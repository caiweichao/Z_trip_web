import pymysql
from pymysql.cursors import DictCursor
from utils.Config import ConfigLoader
from utils.Logs import log


# 连接数据库建立游标，执行sql，关闭数据库

class Mysql_Util:

    def __init__(self):
        config = ConfigLoader()
        host = config.get('mysql', 'host')
        user = config.get('mysql', 'user')
        pwd = config.get('mysql', 'pwd')
        port = config.getint('mysql', 'port')
        try:
            self.db = pymysql.connect(host=host, user=user, password=pwd, database=None, port=port, charset='utf8')
        except TimeoutError as e:
            log.error('数据库链接超时请检查，地址{0}，用户名{1}，密码{2}，端口号{3} \n {4}'.format(host, user, pwd, port, e))
            raise e
        except IndentationError as e:
            log.error('数据库链接用户名不存在请检查 用户名：{0} \n {1}'.format(user, e))
        except pymysql.err.OperationalError as e:
            log.error('用户名或密码错误请检查 用户名：{0} 密码：{1} \n {2}'.format(user, pwd, e))

    # 查询单条数据并且返回 可以通过sql查询指定的值 也可以通过索引去选择指定的值
    def fetch_one(self, sql, name=None):
        # 修改返回值为数组键值对 cursor=pymysql.cursors.DictCursor
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

        try:
            # 按照sql进行查询
            cursor.execute(sql)
            if name == None:
                # 返回一条数据 还有 all size（自己控制）
                data = cursor.fetchone()
                return data
            elif name != None:
                data = cursor.fetchone()
                return data[name]
        except pymysql.err.ProgrammingError as e:
            log.error("请检查sql是否正确 sql={}".format(sql))
            raise e

    def fetch_all(self, sql):  # 查询多条数据并且返回
        # 修改返回值为数组键值对 cursor=pymysql.cursors.DictCursor
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            # 返回一条数据 还有 all size（自己控制）
            data = cursor.fetchall()
        except pymysql.err.ProgrammingError as e:
            log.error("请检查sql是否正确 sql={}".format(sql))
            raise e
        return data

    def close_connect(self):
        # 关闭数据库链接
        self.db.close()


if __name__ == '__main__':
    sql = '''SELECT * FROM tem_flight_test.otaf_intl_order WHERE ID=173523283357824'''
    a = Mysql_Util()
    data = a.fetch_one(sql)
    print(data)
    # A =0
    # x=A+data["ID"]
    # print(x)
