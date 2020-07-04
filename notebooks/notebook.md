# day000 起源、整体设计思路
小说站：前端vue3.0+后端flask+数据库mysql

## 起源

## 项目构思 前后端分离
- 前端： react、vue、jquery+ajax： vue3.0
- 后端： flask、 fastAPI ： flask
- 数据库选择： mysql、 mongodb（不用建表）： 1000本书，100W章节内容： mysql
- 数据采集： requests、scrapy：
## git和github的简单使用
- 创建github账户
- 创建github代码仓库
- 电脑安装git： apt-get install git 或者sudo apt-get install git
- git clone 'url'
- git status (ls -a 能看到.git文件夹)
- git add .
- git commit -m '添加你需要的注释'
- git pull
- git push (填写你的账户和密码)


### 前端vue3.0 优点
- 前后端分离
- 部署简单（哪怕你不懂怎么写代码也可以部署）

用处： 从后端读取数据， 展示页面
### 后端：flask

- 简单

用处： 给前端提供API接口，从数据库读取数据

### 数据库：mysql

用处： 保存数据

### scrapy 采集数据

- requests， 耗时：10天
- scrapy： 10小时

## 项目展示

## 环境配置 ： 统一的环境，能让你获得更好的观看体验
### 题外话： windows VS linux VS Mac OS

#### windows： 鼠标电脑（闭源）
- 桌面无敌
- 使用简单
- 非常适合一般用户
- 没有window就没有现在如此繁华的市场

#### linux系： 键盘电脑（开源）
- 服务器无敌
- 使用不难
- 非常适合开发者
- 没有linux就算有如此繁华的市场，服务器也支撑不了

#### mac OS： 软硬件结合的典范（闭源）

#### 总结：

都只是工具而已，哪个方便就用哪个

### 推荐系统： ubuntu、MacOS

huawei matebook 14 16G （）

### 推荐编辑器： pycharm、 sublime text、 atom、 vs code、 vim或者vi

个人习惯：

- atom或者pycharm写python
- vs code 写其他




# day001 数据库的安装、迁移、权限分配，磁盘挂载，大文件的上传

## .md文件生成html（前提需要安装node，后面再说）
- npm install -g i5ting_toc
- i5ting_toc -f yourfile.md

## 服务器购买

- 阿里云、腾讯云、华为云： 公司用户、学生用户（比较便宜）
- jidcy.com  ： 虎背狼腰

## 获取数据的方式
- wget book.alexhunter1943.com/static/imgs/books.zip  （可以直接在服务器上操作）
- 百度网盘：链接: https://pan.baidu.com/s/1qAvSQ_nIDCtHOw74ysSDEQ 提取码: y1ki （我没测试）
- 压缩命令： zip -q -r 你想压缩的文件
- 解压命令： unzip 你想解压的文件
- md5值： 6f7fbadd48a4b1fa6ecda76cd1d5a625 （这个是.sql结尾的md5值）
- 安装解压工具（在centos上）： yum install unzip

## 登录服务器

ssh --help

- ssh username@IP
- ssh username@IP -P port


## mysql的安装(centOS7)
```python
# 下载rpm包
wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
# 对repo进行安装
rpm -ivh mysql57-community-release-el7-9.noarch.rpm
# 进入 /etc/yum.repos.d目录
# 查看是否有 mysql-community.repo 和mysql-community-source.repo 文件
# 安装
yum install mysql-server
# 启动
systemctl start mysqld
# 查看是否启动
ps aux | grep mysql
# 查看生成临时密码
grep 'temporary password' /var/log/mysqld.log
# 进入mysql
mysql -uroot -p  # 然后回车，输入上面提供的临时密码
# 设置新的密码
ALTER USER USER() IDENTIFIED BY '你自己设置的密码'; # MySQL版本5.7.6版本 开始的的版本
# 或者
SET PASSWORD = PASSWORD('你自己设置的密码'); # MySQL版本5.7.6版本以前的版本
# 关闭服务
systemctl stop mysqld
# 启动服务
systemctl start mysqld
# 登录你的mysql
mysql -u root -p # 回车输入你的新密码
```

## 挂载新的磁盘到/www文件夹下

```python
yum install wget -y && wget -O auto_disk.sh http://download.bt.cn/tools/auto_disk.sh && bash auto_disk.sh

```
## 修改mysql数据库文件存放位置（前提是你要把上面的磁盘挂载完毕）
```python
# 进入/www文件夹
cd /www
# 创建data目录
mkdir data
# 查看当前mysql数据存放目录
cat /etc/my.cnf  # 如果你都是按照上面安装的话，应该是/var/lib/mysql
# 先停止mysql服务
systemctl stop mysqld
# 修改/etc/my.cnf
# 用vim或者vi打开
vim /etc/my.cnf
"""
datadir=/www/data/mysql
socket=/www/data/mysql/mysql.sock
"""
# 移动/var/lib/mysql整个目录到新的文件夹/www/data/
mv /var/lib/mysql /www/data/
# 启动mysqld服务
service mysqld start
# 如果提示 Redirecting to /bin/systemctl start mysqld.service
# 进行如下操作 这是因为没有关闭selinux导致的，关闭selinux然后重新启动mysqld服务
setenforce 0
getenforce
service mysqld start # 这条必须不报错
# 登录mysql
mysql -u root -p # 输入你在上面修改之后的密码
# 报错如下 ：ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)
# 用vim或者vi打开配置文件
vim /etc/my.cnf
# 添加如下内容
"""
[client]
socket=/www/data/mysql/mysql.sock
"""
# 再次登录mysql
mysql -u root -p # 输入你在上面修改之后的密码，应该会成功了
# 重启服务器
reboot
# 再次登录mysql
mysql -u root -p # 输入你在上面修改之后的密码，应该会成功了
# 如果还是登录不上
# 查看错误原因
service mysqld status
# 如果显示如下开头内容
"""
Redirecting to /bin/systemctl status mysqld.service
● mysqld.service - MySQL Server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled;
"""
# 修改selinux配置文件/etc/selinux/config，让selinux永久工作在permissive模式下
vi /etc/selinux/config
"""
SELINUX=permissive
SELINUXTYPE=targeted
"""
# 再次重启，并尝试登录
reboot

mysql -u root -p # 输入你在上面修改之后的密码，应该会成功了

```

## 大文件传输

- github，不行 ： github上最大的单个文件是100M
- 直接用scp，不行： scp传送的最大文件不能超过4G
- nc， 速度快，但是直接传送4G文件中途会断开; 目前我还不知道如何一次性批量传送多个文件： 没有成功

如果有更好的办法，请告诉我！！！

```python
# 直接在服务器上运行这条命令
mysqldump -u root -p books > books.sql
# 等他运行结束以后，会生成一个book.sql的文件
# 接下来的问题就是通过scp从服务器上把这个文件弄到你想要的地方了
# 简单

md5sum books.sql
# 这条命令会生成一个hash值，保存一下

cat books.sql | split -b 512M - sql.books.
# 在服务器上运行上面这个命令会把原来的books.sql 分隔成若干个以sql.books.开头的文件

# 下面这条命令，在本地电脑上运行
scp root@服务器IP:/path/to/books.sql/sql.books.* ./
# 把服务器上所有分割好的文件下载到本地

cat sql.books.* > books.sql
# 把所有已经下载好的、分割好的文件，再次合成同一个文件
md5sum books.sql
# 在本地生成的hash值和服务器上生成的hash值对比一下，如果完全一样，备份结束

```

## 数据恢复 （恢复到本地）


```python
mysql -u root -p
# 登录本地的mysql数据库
create database books;
# 创建一个名为books的数据库
exit;
# 退出数据库

# 下面真的在本地开始恢复数据库
mysql -h localhost -u root -p 本地数据库的名字 < .sql文件的路径

mysql -h localhost -u root -p books< ./books.sql

```


## 创建权限适当，并允许远程登录的账户

```python
# 登录mysql
mysql -u root -p
mysql 正确的使用方式（永远，永远不要让root可以远程登录）
# 这个命令会让你创建一个能在本地登录的alex1943_read_books的帐号，密码为qwe123，并且允许远程登录
CREATE USER 'alex1943_read_books'@'%' IDENTIFIED BY 'qwe123';
# 把这个数据库的所有权限赋予给这个alex1943_read_books这个账户
GRANT ALL PRIVILEGES ON books.* TO 'alex1943_read_books'@'%';
# 这条命令会让alex1943_read_books这个账户会有和root一样的权限
GRANT ALL PRIVILEGES ON *.* TO 'alex1943_read_books'@'%';
# 这条是正确的打开方式
GRANT select ON books.* TO 'alex1943_read_books'@'%';
#刷新权限
FLUSH PRIVILEGES;

# 测试远程登录，如果不成功，请检查centos的防火墙，以及3306端口

systemctl stop firewalld.service             #停止firewall

systemctl start firewalld.service             #开启firewall
systemctl disable firewalld.service        #禁止firewall开机启动

firewall-cmd --state                           ##查看防火墙状态，是否是running



#开启  :
systemctl start firewalld.service


#打开3306端口
firewall-cmd --zone=public --add-port=3306/tcp --permanent
"""
多一句嘴，如果以后你要修改默认端口，直接在/etc/my.cnf添加一行
port=3308
然后重启mysql
systemctl restart mysqld
最后也是要在防火墙这边放行的
firewall-cmd --zone=public --add-port=3308/tcp --permanent
"""

```


# 3 day002_python3_pip3_virtualenv_flask创建_pymysql

 万物一类

## python2 VS python3

- 安装python3
- 安装pip3 ： apt-get install python3-pip

## virtualenv

- 为什么需要virtualenv
- 怎么安装virtualenv： pip3 install virtualenv
- 怎么使用virtualenv:
-- 创建虚拟环境：virtualenv -p python3 yourEnvName
-- 进入虚拟环境： source /yourEnvName/bin/activate
-- 推出虚拟环境： deactive

## 命名规则（PEP8）

- 大写字母开头的：一般是类
- 小写字母开头的：一般是方法或者变量或者库、模块
- 方法尽量用蛇型命名法： get_books_infos()
- 不允许双下划线开头和结尾的命名：双下划线开头和结尾（python自己留着用的）
- 单下划线（一个类内部的成员变量或者方法）

## 你如何使用git上拉下来的python项目

- 在你自己的电脑上创建一个虚拟环境
- 进入你自己的虚拟环境
- pip install -r requirements.txt

## flask

- 安装在虚拟环境中

最简单的falsk
```python
from flask import Flask


# 创建flask的应用对象
app = Flask(__name__)
# __name__:表示当前模块名字
# 模块名作用：flask以这个模块所在的目录为总目录
# 默认这个目录中的static为静态文件目录
# 默认这个目录中的templates为模板文件目录

'''
__name__的具体名字：
如果作为启动模块（就是你直接运行当前磨矿）：__name__ =__main__:(python定死的)
如果你从别的地方导入一个模块，而导入的模块中也使用__name__,那么导入模块中的__name__=模块的名字（文件名）
结合 if __name__ == '__main__':来理解，这也就是为什么这个==可以作为入口函数的原因
app = Flask(
    __name__,
    static_url_path="/python",  # 修改静态资源url前缀，默认为/static
    static_folder="static",  # 修改静态文件目录，默认就是static
    template_folder="templates"  # 模板文件目录，默认是templates
)
'''

@app.route("/")
def index():
    """定义视图函数"""
    return "Hello Flask"

if __name__ == '__main__':
    # 启动flask程序
    app.run()
    # app.run(host='', port=5555, DEBUG=True)
    # 绑定端口和IP，设定模式为DEBUG模式（代码有更新，直接刷新就好了）
# 在终端输入：python 你为这个文件命名的.py文件
```

## pymysql

- 安装在虚拟环境中


# day003_VUE：node+vue+axios+bootstrapvue

## 一个口误、一个错误

- 单下划线
- .gitignore

## 一个简单的问题：一个网站能浏览需要哪些东西？

- html
- js
- css
- 后端服务器
- 或许还有数据库
- 浏览器


## 关于vue的三点你必须知道事情：
- vue是基于javascript的。（潜台词：天生异步）
- vue是数据驱动的。
- vue为什么需要生命周期？

## node的安装

```python
sudo apt-get install npm
sudo npm -g install npm
# -g 全局安装
# pip3 install --upgrade pip
# 还记得上面这个命令吗？
# 这个命令的作用和pip3这个命令类似，自己更新自己
npm -v
# 如果能获得版本信息，那么恭喜你安装对了
sudo npm install npm -g
# npm 更新自己
# 把npm的更新源换成淘宝的
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
# 从此以后cnpm和npm等价
```
- 安装vue-cli

```python
sudo npm install -g @vue/cli
# 先安装npm哈
vue --version
# 如果可以正确输出版本信息，那么恭喜你
vue --help
# 建议你先仔细看一下这些内容，不难的
```

## vue的安装、项目创建

```python
vue create ProjectName
'''
第一步：
用空格选中，回车确认，进入下一步
'''
? Please pick a preset: (Use arrow keys)
❯ default (babel, eslint)  # 采用默认设置
  Manually select features  #采用自定义设置
# 当然选择自定义设置啦

'''
第二步：
'''

? Check the features needed for your project:
# 为你的项目选择属性
(Press <space> to select, <a>
to toggle all, <i> to invert selection)
# 按空格选中或者不选中
# 按回车确认进入下一步
❯◉ Babel  # 编译 es6 to es5 必选
 ◯ TypeScript  # js超集
 ◯ Progressive Web App (PWA) Support # 渐进式的web运用
 ◯ Router  # vue路由，必选
 ◯ Vuex  # vue状态管理， 必选
 ◯ CSS Pre-processors  # css编译器， 必选
 ◉ Linter / Formatter  # 代码检测和格式化， 必选
 ◯ Unit Testing  # 单元测试
 ◯ E2E Testing  # 端对端测试，属于黑盒测试

'''
第三步：
Use history mode for router？
路由是否采用histroy模式？
路由模式有两个： hash、 history
hash： 即url中带有#符号 如http://www.abc.com/#/hello/
history： 利用了HTML5 History Interface中新增的pushState()和replaceState()两个方法，可以去掉这个#，但是需要在nginx和Apache中进行简单配置

选n，偷懒
'''
Vue CLI v4.3.1
? Please pick a preset: Manually select features
? Check the features needed for your project: Babel, Router, Vuex, CSS Pre-p
rocessors, Linter
? Use history mode for router? (Requires proper server setup for index fallb
ack in production) (Y/n)


'''
第四步：选择css编译器
选node-sass编辑器
'''
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are suppor
ted by default): (Use arrow keys)
❯ Sass/SCSS (with dart-sass)
  Sass/SCSS (with node-sass)
  Less
  Stylus

'''
第五步： 选择代码规范
选择最后一个： ESLint + Prettier
'''
? Pick a linter / formatter config: (Use arrow keys)
❯ ESLint with error prevention only
  ESLint + Airbnb config
  ESLint + Standard config
  ESLint + Prettier

'''
第六步： 选择何时进行代码检测
选择： Lint on save
'''

? Pick additional lint features: (Press <space> to select, <a> to toggle all
, <i> to invert selection)
❯◉ Lint on save   # 保存时检测
 ◯ Lint and fix on commit  # 提交时检测


'''
第七步： 你要把你刚才选择的配置文件保存在什么位置？
选择： In dedicated config files
'''

? Where do you prefer placing config for Babel, ESLint, etc.? (Use arrow key
s)
❯ In dedicated config files  # 保存在各自的配置文件中
  In package.json  # 保存在package.json中

'''
第八步： 是否把你当前的配置文件设置成一个随时可以选择的配置文件

选择： n （多来几次，你就记得住了）
'''

? Save this as a preset for future projects? (y/N)

```


## 对当前vue项目的文件做一些调整

- Vue3.0新特性语法

```python

# 安装依赖
sudo npm install @vue/composition-api --save
# 在 ./src/main.js 中添加如下
import VueCompositionApi from '@vue/composition-api';  # 去找这个文件的时候注意文件夹的名字叫“@vue”

Vue.use(VueCompositionApi);
```
- vue axios 安装

```js
npm install axios

```

- vue bootstrapvue 安装

```js
npm install bootstrap-vue

import Vue from 'vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
```

# day004 网站分类页面、图书首页、图书详情页面

## 遗漏的问题： 跨域
- 请求地址：http://localhost:8081/api/books_cates
- 替换“^/api”之前的所有数据“/books_cates”
- 最终的url： http://127.0.0.1:1943/books_cates

## 一个页面的诞生

- 确定访问的路由
- 让无数据的页面能展示
- 确认请求的接口和数据，并确认能发送正确的请求
- 在flask完善接口，并确认能正确返回结果
- 查看数据是否正确显示

## 一个接口的诞生
- 确定请求路径和参数
- 获取参数
- 检测参数
- 查询数据
- 返回结果





# day005 寂静无声的一天


# day006

# day007 RSA

## 生成RSA密钥对

```bash
 // 私钥
 openssl genrsa -out rsa_1024_priv.pem 1024
 // cat rsa_1024_priv.pem 读取私钥内容
 // 公钥
 openssl rsa -pubout -in rsa_1024_priv.pem -out rsa_1024_pub.pem
 // cat rsa_1024_pub.pem 读取公钥内容
```


## 在vue中使用RSA加密
```js
1.安装依赖   npm install jsencrypt  
2.在main.js引入   import { JSEncrypt } from 'jsencrypt'  
3.挂载全局方法
//JSEncrypt加密方法
Vue.prototype.$encryptedData = function(publicKey, data) {
  //new一个对象
  let encrypt = new JSEncrypt()
  //设置公钥
  encrypt.setPublicKey(publicKey)
  //password是要加密的数据,此处不用注意+号,因为rsa自己本身已经base64转码了,不存在+,全部是二进制数据
  let result = encrypt.encrypt(password)
  return result
}
//JSEncrypt解密方法
Vue.prototype.$decryptData = function(privateKey, data) {
  // 新建JSEncrypt对象
  let decrypt = new JSEncrypt()
  // 设置私钥
  decrypt.setPrivateKey(privateKey)
  // 解密数据
  let result = decrypt.decrypt(secretWord)
  return result
}
```

## 在flask中使用RSA解密

```python
import rsa


def get_secret_key(cryptdata):
    # print("cryptdata = ", cryptdata)
    privkey = rsa.PrivateKey.load_pkcs1(RSA_1024_PRIV_KEY)
    msg = rsa.decrypt(base64.b64decode(cryptdata), privkey)
    # msg = rsa.decrypt(base64.b64decode(cryptdata), RSA_1024_PRIV_KEY)
    # print("str(msg) = ", msg.decode().split(":")[1])
    return msg.decode().split(":")[1]
```

## 我们可以用这个来做什么？

### 加密接口的内容

- 时间戳 ： 防止重复使用加密数据。
- 域名 ： 只有我们自己指定的域名可以访问我们的接口
- 其他信息 ： 未来预留

### 可以用来做什么？

- 可以简单的防止别人用API快速爬取数据
- 可以用来判断是否是自己允许的域名来访问接口
- 可以根据不同的域名，给于不同的关键词
- 可以根据不同的域名，投放不同或者相同的广告页面

# day008

- 忘记了requirements.txt
- 数据库的表设计不合理
- secretKey中密码不正确怎么办？并没有处理


## 广告

- https://i.loli.net/2020/07/01/LYOu8yNXT93E4H1.jpg  （电脑版）
- https://i.loli.net/2020/06/11/MLPaI12eFsyRXck.jpg
- https://i.loli.net/2020/06/11/sDlvEWaeSxzpYgb.jpg （电脑版）

## 查询语句优化

- select * from (select * from book_details where sort_id=447867 ) temp where temp.book_id=43443 \G;


# 发布

## 理想状态： 专机专用
- 数据库服务器： N个服务器，根据地域不同，读写分离，做主从服务器。
- flask服务器： N服务器和数据库一一对应
- 后端nginx服务器： 负载均衡
- scrapy服务器
- 前端服务器（vue）

## 一般情况

### 数据库、flask、scrapy服务器

- 挂载磁盘
- 安装mysql、并修改默认保存地址
- 配置scrapy，使用screen让scrapy在后台执行
- 安装、配置gunicorn
- 安装、配置nginx

### 前端服务器
- 安装宝塔
- 配置vue

## 数据库、flask、scrapy服务器配置流程

- 更新服务器
```bash
yum -y update

yum install wget -y && wget -O auto_disk.sh http://download.bt.cn/tools/auto_disk.sh && bash auto_disk.sh


```
- 挂载磁盘
- 安装配置mysql，并修改默认保存文件位置
- 数据库表的建立

```python3
图书基本信息： book_infos表中信息
{
	"id" : 自增,
	"book_id" : 45761,
	"book_cate" : "xiuzhen",
	"book_name" : "九叔的掌门大弟子",
	"image_urls" : "https://www.biquge.com.cn/files/article/image/45/45761/45761s.jpg",
	"book_author" : "作    者：莲花山主",
	"book_status" : "状    态：连载中,",
	"book_last_update_time" : "最后更新：2020-04-21 19:06:40",
	"book_newest_name" : "第八十五章：终于到达",
	"book_newest_url" : "/book/45761/447733.html",
	"book_desc" : "\n                携带可成长空间重生清末，成为九叔的掌门大弟子。不断成长，并开山立派。\n\t\t\t",
	"image_paths" : "full/a2a8fbe4a5c01847fb44293891088e1c171bf135.jpg"
}
图书详情页信息： book_details 表中信息
{
	"_id" : ObjectId("5e9edbb0f16879cb082fcb33"),
	"book_id" : 32748,
	"sort_id" : 131839,
	"detail_title" : "第十九章给上门挑衅",
	"detail_content" : "    第十九章给上门挑衅    “放了两个月暑假你以为自己乌鸦变凤凰了？居然敢跟我们这么说话？.....(字数不定)"
}
1. 在数据库中建立一个数据库： create database books charset=utf8;
2. 建立两张表
    2.1 ： create table book_infos(
                id int unsigned not null auto_increment primary key,
                book_id int unsigned not null,
                book_cate varchar(10),  -- 字符串类型，还记得为什么不用var(10)么？
                book_name varchar(25),  -- 图书名称
                image_urls varchar(255), -- 图片原来位置
                book_author varchar(25), -- 图书作者 （需要经过数据清洗）
                book_status varchar(10), -- 图书状态（其实可以用枚举类型）
                book_last_update_time datetime, -- 最后更新时间，（需要经过数据清洗）
                book_newest_name varchar(50), -- 最新章节名称
                book_newest_url int unsigned, -- 最新章节的地址
                book_desc varchar(350), -- 图书描述
                image_paths varchar(50) -- 图片保存路径
            );
    2.2 : create table book_details(
                id bigint unsigned not null auto_increment primary key,  -- 想一下这里为什么用bigint
                -- 初始化过程中图书大概有450本，假设每本书有3000章：450X3000，但是这仅仅是初始化的过程。
                -- bigint 0-18446744073709551615 祝你好运
                book_id int unsigned not null,
                sort_id int unsigned not null,  -- 排序标记
                detail_title varchar(50),  -- 该章标题
                detail_content mediumtext  -- 保存内容
            );
3. 去写代码吧，因为mysql更加严苛，所以先用正则把需要清洗的数据，修改一下
4. 开始写 BiqugeMysqlPipeline 这个类，并在settings中启用它
```
- 安装python3和virtualenv,创建和安装scrapy的虚拟环境

```bash
yum install -y python36-setuptools
pip3 install virtualenv

virtualenv -p python3 scrapy_env
source scrapy_env/bin/activate

pip install -r requirements.txt
```
- scrapy

- gunicron 和 nginx

```ptyhon3
pip install gunicorn
# 安装
gunicorn -h
# 查看帮助文档
gunicorn -w 4 -b IP:PORT -D --access-logfile  main:app
# -w : worker：表明进程数目
# -b : bind: 绑定IP和端口号（当然你运行在哪个机器上，就是哪个IP）
# -D 表明作为守护进程运行在后台
# --access-logfile ：指定日志文件保存位置（绝对路径）
# ../../main:app ：指定入口函数位置（绝对路径）
# 例：
gunicorn -w 4 -b 222.222.222.222:5000 -D --access-logfile /home/www/YourProgram/log  main:app
# 这个下面会用到



ps aux | grep nginx
# 如果你的服务器中已经存在nginx在运行，
# 那么这条命令会让你看到正在运行的nginx的配置文件的路径
# 找到他，然后用下面的命令复制他（免得你改错了）
sudo cp ../../nginx.conf  ../../nginx.conf.backup
sudo vim ../../nginx.conf
# 开始编辑nginx配置
# 在http{}中的server{}中添加如下内容
location / {
    proxy_pass http://flask;
    # proxy_pass 转发，转发到哪里
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    # 下面这两行的意思是告诉flask或者gunicorn用的IP和路由，不然flask永远获取到的IP信息都是nginx的IP
}
正确内容如下：有些内容来自上面
location / {
    proxy_pass http://222.222.222.222:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}


最终方案：

server{
    listen 80;
    server_name http://bookapi.alexhanter1943.com/;
    location /full/ {
            root /www/scrapy_robot/biquge/BookImages;
            autoindex on;
    }
    location / {
            proxy_pass http://43.248.8.5:6661;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
    }
}



Nginx负载均衡（真实的部署，可能会比上面那个更加真实一点）


http {
    ...
    upstream flasks {
        server 222.222.222.222:5555;
        server 222.222.222.222:6666;
        server 222.222.222.111:7777;
        server 222.222.222.222:7777;
    }
    # flasks 可以是任意名字
    # 仔细看上面的端口号和地址，你会发现一些东西哦
    # 如果你发现了，你就知道什么是负载均衡了
    ...
    server{
        listen  PORT(通常为80);
        servername IP or url;
        ...
        location / {
            proxy_pass http://flasks;
            # 注意这里的flasks，要和上面的upstream后面的名字一样了
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            # 下面这两行的意思是告诉flask或者gunicorn用的IP和路由，不然flask永远获取到的IP信息都是nginx的IP
        }
        ...
    }
    ...

}
```

## 宝塔

```nginx

#跨域请求数据
  	location /api {
  		add_header "Access-Control-Allow-Origin"  *;
  		proxy_pass http://bookapi.alexhanter1943.com/;

  		proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
  	}

  	location @router {
  	  rewrite ^.*$ /index.html last;
  	 }
  	location / {    
  	   try_files $uri $uri/ @router;    
  		index index.html;
  	}


```

## 配置图片

```nginx

location /images/ {
    root  /home/ftpadmin/health/;
    autoindex on;
}  

# 记得修改文件的用户权限

chmod 777 -R /home/ftpadmin

```
# 项目总结

## 总结之前先处理一点小问题

- 发布过程中忘记改flask中的默认地址了
- 去掉flask中不必要的配置

## 没有难的内容，或者说没有无法理解的内容，只是多而杂。

总结起来就是，你要相信你自己，肯定可以。

## 为什么这个视频中没有包含scrapy的内容，以及scrapy如何写的思路

## 如何快速把扩展网站

从1个图书网站，到1000个图书网站！

- 解析域名到宝塔所在的服务器 dns.com
- 修改flask中的settings.py文件，把你的域名加入到允许访问的域名中去
- 修改vue中的read.js的域名
- 编译vue，并上传到宝塔 npm run build
- 在宝塔中新建网站，并配置nginx
- 在浏览器中访问，你自己的域名。

## 配置一个大家可以使用的数据库

mysql -h 43.248.8.5 -u alexhunter1943 -p

QWEqwe123！@#

## todo

- 写一个首页
- 写一个后台管理系统来操作所有的1000个网站
```
1.控制哪些域名可以访问
2.控制不同的域名，可以有不同的关键词
3.控制广告图片，和广告链接（因为肯定会有N多的广告的）
```
- 写一个用户登录系统
- 写一个能够记录某本图书的被查看的次数
- 分析每本图书的词图（数据分析）  --> 一个更好搜索系统
- 写一个用户推荐图书的系统

## 抱歉，没有讲原理

## 技术栈

### vue3.0

- vue3.0特性 ：import VueCompositionApi from "@vue/composition-api";
- 排版： import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
- 请求： axios
- 加密： import { rsaEncrypt } from "../utils/rsa.js";

### flask

- flask
- pymysql


## 人生苦短，道阻且长

江湖再见。  2020.07.05
