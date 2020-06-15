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

## mysql的安装(centOS)
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
grep ‘temporary password‘ /var/log/mysqld.log
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

# day002 VUE创建、FLASK创建


## day002。1

## day002。2
