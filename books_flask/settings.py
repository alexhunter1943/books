MYSQL_HOST = '43.248.8.18'
MYSQL_PORT = 3306
MYSQL_USER = 'alex1943_read_books'
MYSQL_PASSWORD = 'QWEqwe123!@#'
MYSQL_DATABASE = 'books'

BOOK_LIST = [
    'xuanhuan',
    'xiuzhen',
    'dushi',
    'lishi',
    'wangyou',
    'kehuan',
    'yanqing',
    'qita',
    'quanben'
]

RSA_1024_PRIV_KEY = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCwPEDLQr/zC \
nXfX+W+9hpihoSKCn4blouwznrzmH7+1KDGXBj3vEDloM4w8+eZgQs/jS1VAaOexfWkxV0hGNzQyJc \
7FF5BfXuoPNnWwapU50iU55fyWqaWLcfNkE3hN3Ayf8XvqDnnpfyi8SGaYXeFr3zy4+SupDKs2QY+t \
99jZwIDAQABAoGAf3PT2Cv57abPADC2UphhFIf8KmjUMtd5RvDM8oaCsYDMlSfd1qwKswbMl5KN \
F/K/U8Kh2ixJTHYV5IfnhhwY9KEScpUJ7hcA02/1dgOqTsHiQf+ReGnDa9nVF0hdXOjAIKox1Kc \
u9hYMsDDFzR9/GIVT0XajwpbEschRqzmjB+ECQQDm1rlRbrTrmfObMEgvdLubQNCUnsBMbVOt+PR \
5vFjsdiwD9apXc0Y0Woxbhzv0IcC0dn/7jTDxG6IxDX7EnHp9AkEAw3HjLp0AFnqHD9gP7929LqRM \
FNFxKyHfzMhAnMbIRqvvvhAvZwJ95dqo/rOX7uDtrra7cc8cw9aBAQJ5f9sWswJAQOXTWgK \
O2MICi/nKAZWG/QH+4hmzpIkEAqBAU01RjsE2ZLKXfliJP0TJux3NDDjFDbdXCejK/q4vLi1GG4 \
6GnQJATHOsTnuToTdkxcna0hWG/0u9hxc2kYy6orxiqfEIPrzbFxn1sPHElbknChruf770urc4M \
5i0w9aQt/hj1qO5CQJBAMu6UybGgYCFP7g033oVuWOSnibNiRF1cLWSBj7p3PbUkYxEcmUpc+W8q \
CjP62Q6zLi7Mz3j5rDGXhk73LnPwvQ=\n-----END RSA PRIVATE KEY-----'

REQUSET_LISTS = [
    'book.alexhunter1943.com',
    'www.baidu.com'
]

"""
表1字段：    1、 id
            2、域名

表2字段：    1、di
            2、标识

表3字段      1、id
            2、表1_id
            3、表2_id
            3、title
            4、keywords
            5、descriptions
"""

TITLES = {
    'book.alexhunter1943.com':{
        "index":['风华绝代的alexhunter首页标题', '风华绝代的alexhunter首页关键词','风华绝代的alexhunter首页描述'],
        "xiuzhen":['风华绝代的alexhunter修真分类页标题', '风华绝代的alexhunter修真分类页关键词','风华绝代的alexhunter修真分类页描述'],
        "xuanhuan":['风华绝代的alexhunter玄幻分类页标题', '风华绝代的alexhunter玄幻分类页关键词','风华绝代的alexhunter玄幻分类页描述'],
        "dushi":['风华绝代的alexhunter都市分类页标题', '风华绝代的alexhunter都市分类页关键词','风华绝代的alexhunter都市分类页描述'],
        "lishi":['风华绝代的alexhunter历史分类页标题', '风华绝代的alexhunter历史分类页关键词','风华绝代的alexhunter历史分类页描述'],
        "wangyou":['风华绝代的alexhunter网游分类页标题', '风华绝代的alexhunter网游分类页关键词','风华绝代的alexhunter网游分类页描述'],
        "kehuan":['风华绝代的alexhunter科幻分类页标题', '风华绝代的alexhunter科幻分类页关键词','风华绝代的alexhunter科幻分类页描述'],
        "yanqing":['风华绝代的alexhunter言情分类页标题', '风华绝代的alexhunter言情分类页关键词','风华绝代的alexhunter言情分类页描述'],
        "qita":['风华绝代的alexhunter其他分类页标题', '风华绝代的alexhunter其他分类页关键词','风华绝代的alexhunter其他分类页描述'],
        "quanben":['风华绝代的alexhunter全本分类页标题', '风华绝代的alexhunter全本分类页关键词','风华绝代的alexhunter全本分类页描述'],
        "bookindex":['风华绝代的alexhunter_bookindex_标题', '风华绝代的alexhunter_bookindex_关键词','风华绝代的alexhunter_bookindex_描述'],
        "bookdetail":['风华绝代的alexhunter_bookdetail_标题', '风华绝代的alexhunter_bookdetail_关键词','风华绝代的alexhunter_bookdetail_描述'],
    },
    'www.baidu.com':{
        "index":['风华绝代的alexhunter首页标题', '风华绝代的alexhunter首页关键词','风华绝代的alexhunter首页描述'],
        "xiuzhen":['风华绝代的alexhunter修真分类页标题', '风华绝代的alexhunter修真分类页关键词','风华绝代的alexhunter修真分类页描述'],
        "xuanhuan":['风华绝代的alexhunter玄幻分类页标题', '风华绝代的alexhunter玄幻分类页关键词','风华绝代的alexhunter玄幻分类页描述'],
        "dushi":['风华绝代的alexhunter都市分类页标题', '风华绝代的alexhunter都市分类页关键词','风华绝代的alexhunter都市分类页描述'],
        "lishi":['风华绝代的alexhunter历史分类页标题', '风华绝代的alexhunter历史分类页关键词','风华绝代的alexhunter历史分类页描述'],
        "wangyou":['风华绝代的alexhunter网游分类页标题', '风华绝代的alexhunter网游分类页关键词','风华绝代的alexhunter网游分类页描述'],
        "kehuan":['风华绝代的alexhunter科幻分类页标题', '风华绝代的alexhunter科幻分类页关键词','风华绝代的alexhunter科幻分类页描述'],
        "yanqing":['风华绝代的alexhunter言情分类页标题', '风华绝代的alexhunter言情分类页关键词','风华绝代的alexhunter言情分类页描述'],
        "qita":['风华绝代的alexhunter其他分类页标题', '风华绝代的alexhunter其他分类页关键词','风华绝代的alexhunter其他分类页描述'],
        "quanben":['风华绝代的alexhunter全本分类页标题', '风华绝代的alexhunter全本分类页关键词','风华绝代的alexhunter全本分类页描述'],
        "bookindex":['风华绝代的alexhunter_bookindex_标题', '风华绝代的alexhunter_bookindex_关键词','风华绝代的alexhunter_bookindex_描述'],
        "bookdetail":['风华绝代的alexhunter_bookdetail_标题', '风华绝代的alexhunter_bookdetail_关键词','风华绝代的alexhunter_bookdetail_描述'],
    },
}


PHONE_ADS = [
    {
        "url":"http://jidcy.com/",
        "img_path":"https://i.loli.net/2020/07/01/LYOu8yNXT93E4H1.jpg",
        "alt": "!@#$%^&"
    },
    {
        "url":"http://www.baidu.com/",
        "img_path":"https://i.loli.net/2020/07/01/LYOu8yNXT93E4H1.jpg",
        "alt": "百度"
    }
]

PC_ADS = [
    {
        "url":"http://jidcy.com/",
        "img_path":"https://i.loli.net/2020/06/11/MLPaI12eFsyRXck.jpg",
        "alt": "!@#$%^&"
    },
    {
        "url":"http://www.baidu.com/",
        "img_path":"https://i.loli.net/2020/06/11/MLPaI12eFsyRXck.jpg",
        "alt": "百度"
    }
]

COL_ADS = [
    {
        "url":"http://jidcy.com/",
        "img_path":"https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg",
        "alt": "!@#$%^&"
    },
    {
        "url":"http://www.163.com/",
        "img_path":"https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg",
        "alt": "!@#$%^&"
    },
    {
        "url":"http://www.taoba.com/",
        "img_path":"https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg",
        "alt": "!@#$%^&"
    },
    {
        "url":"http://www.qq.com/",
        "img_path":"https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg",
        "alt": "!@#$%^&"
    },
    {
        "url":"http://www.baidu.com/",
        "img_path":"https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg",
        "alt": "百度"
    }
]
