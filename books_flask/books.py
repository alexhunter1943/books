from pymysql import connect
from pymysql.cursors import DictCursor # 为了返回字典形式
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

# 类和对象
# 对象是类的实例
# 类是抽象的
# 对象是具像的

class Book(object):
    def __init__(self):  # 创建对象同时要执行的代码
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor=self.conn.cursor(DictCursor)  # 这个可以让他返回字典的形式

    def __del__(self):  # 释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()


    def get_books_infos_limit(self):
        sql = 'select * from book_infos limit 3'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)
        return data

    def get_cates_newst_books_30(self, book_cate):
        sql = "select id, book_name,book_id,book_last_update_time, \
        book_newest_name,book_newest_url from book_infos \
        where book_cate='{}' order by book_last_update_time desc limit 30;".format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)
        return data
