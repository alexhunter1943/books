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


@app.route('/', methods=['GET', 'POST']) # 路由
def hello_world():
    book = Book()
    arrData = book.get_books_infos_limit()
    print("arrData = ", arrData)
    return jsonify(arrData)


if __name__ == '__main__':
    print("__name__ = ", __name__)
    app.run(host='127.0.0.1', port=1943, debug=True)
