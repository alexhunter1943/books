from flask import Flask, jsonify
from books import Book

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


@app.route('/', methods=['GET', 'POST']) # 路由
def hello_world():
    book = Book()
    arrData = book.get_books_infos_limit()
    print("arrData = ", arrData)
    return jsonify(arrData)


if __name__ == '__main__':
    print("__name__ = ", __name__)
    app.run(host='127.0.0.1', port=1943, debug=True)
