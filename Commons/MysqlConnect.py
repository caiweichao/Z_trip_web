import pymysql
from Commons.Config import ConfigLoader
from Commons.Logs import log

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

    def fetch_one(self, sql):  # 查询单条数据并且返回
        cursor = self.db.cursor()
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            # 返回一条数据 还有 all size（自己控制）
            data = cursor.fetchone()
        except pymysql.err.ProgrammingError as e:
            log.info("请检查sql是否正确 sql={}".format(sql))
            raise e
        return data

    def fetch_all(self, sql):  # 查询多条数据并且返回
        cursor = self.db.cursor()
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            # 返回一条数据 还有 all size（自己控制）
            data = cursor.fetchall()
        except pymysql.err.ProgrammingError as e:
            log.info("请检查sql是否正确 sql={}".format(sql))
            raise e
        return data


if __name__ == '__main__':
    sql = 'SELECT * from tem_platform.ipe_user where ID = 3130'
    a = Mysql_Util()

    print(a.fetch_one(sql)['id'])
