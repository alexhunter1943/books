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
            # print(temp)
            data.append(temp)
        return data

    def get_cates_newst_books_30(self, book_cate):
        sql = "select id, book_name,book_id,book_last_update_time, \
        book_newest_name,book_newest_url from book_infos \
        where book_cate='{}' order by book_last_update_time desc limit 30;".format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print(temp)
            data.append(temp)
        return data

    def get_cates_most_books_30(self, book_cate):
        sql = "select id,book_id,book_name,book_author,book_newest_url from book_infos where book_cate='{}' order by book_newest_url desc limit 35;".format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print(temp)
            data.append(temp)
        return data

    def get_book_infos_by_book_id(self,book_id):
        sql = "select * from book_infos where book_id ='{}'".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data

    def get_book_all_caps_by_book_id(self,book_id):
        sql = "select id,book_id,sort_id,detail_title from book_details where book_id='{}' order by sort_id".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data

    def get_book_newest_20_caps_by_book_id(self,book_id):
        sql = "select id,book_id,sort_id,detail_title from book_details where book_id='{}' order by sort_id desc limit 20".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data
