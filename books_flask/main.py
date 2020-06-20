from flask import Flask, jsonify, request
from books import Book
import json
from settings import BOOK_LIST

"""
接口说明：
1.返回的是json数据
2.结构如下
{
    resCode： 0, # 非0即错误 1
    data： # 数据位置，一般为数组
    message： '对本次请求的说明'
}
"""

app = Flask(__name__)

# 1. 你直接执行这个文件：那么__name__= __main__
# 2. __name__ = 当前文件的名字

app.config['JSON_AS_ASCII'] = False


@app.route('/books_cates', methods=['GET'])
def get_books_cates():
    resData = {
        "resCode": 0, # 非0即错误 1
        "data": [
            {"id":0, "text": '首页', "url":'/'},
            {"id":1, "text": '玄幻', "url":'/xuanhuan'},
            {"id":2, "text": '修真', "url":'/xiuzhen'},
            {"id":3, "text": '都市', "url":'/dushi'},
            {"id":4, "text": '历史', "url":'/lishi'},
            {"id":5, "text": '网游', "url":'/wangyou'},
            {"id":6, "text": '科幻', "url":'/kehuan'},
            {"id":7, "text": '言情', "url":'/yanqing'},
            {"id":8, "text": '其他', "url":'/qita'},
            {"id":9, "text": '完本', "url":'/wanben'},
        ],# 数据位置，一般为数组
        "message": '对本次请求的说明'
    }
    return jsonify(resData)

# post man
@app.route('/<string:book_cate>', methods=['POST'])
def get_cates_infos(book_cate):
    if request.method == 'POST':
        print("捕获到了post请求 book_cate", book_cate)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        print("key = ", key)
        secretKey = get_data['secretKey']
        if book_cate in BOOK_LIST:
            print(key, " is in BOOK_LIST")
            print(key, secretKey)
            if key == 'newest':
                # select * from book_infos where book_cate='xiuzhen' order by book_last_update_time desc limit 3
                print("newest")
                book = Book()
                sql_data = book.get_cates_newst_books_30(book_cate)
                resData = {
                    "resCode": 0, # 非0即错误 1
                    "data": sql_data,# 数据位置，一般为数组
                    "message": '最新的30本图书信息查询结果'
                }
                return jsonify(resData)
            elif key == 'most':
                print("most")
                pass
            else:
                resData = {
                    "resCode": 2, # 非0即错误 1
                    "data": [],# 数据位置，一般为数组
                    "message": '参数有误'
                }
                return jsonify(resData)
        else:
            print("key is not BOOK_LIST")
            return 404
    else:
        resData = {
            "resCode": 1, # 非0即错误 1
            "data": [],# 数据位置，一般为数组
            "message": '请求方法错误'
        }
        return jsonify(resData)






@app.route('/', methods=['GET', 'POST']) # 路由
def hello_world():
    book = Book()
    arrData = book.get_books_infos_limit()
    print("arrData = ", arrData)
    return jsonify(arrData)


if __name__ == '__main__':
    print("__name__ = ", __name__)
    app.run(host='127.0.0.1', port=1943, debug=True)
