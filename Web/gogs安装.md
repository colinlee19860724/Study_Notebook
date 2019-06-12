
# 1. Gogs 安装
Gogs 是一款极易搭建的自助 Git 服务。Gogs 的目标是打造一个最简单、最快速和最轻松的方式搭建自助 Git 服务。使用 Go 语言开发使得 Gogs 能够通过独立的二进制分发，并且支持 Go 语言支持的 所有平台，包括 Linux、Mac OS X、Windows 以及 ARM 平台。

## 1.1. 安装准备
> 以下步骤均在 CentOS 7.6 下测试成功
1. 更新 yum 源

```bash
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

2. 安装 git

```bash
yum install -y git
```

3. 安装数据库
支持 MySQL、Mariadb、PostgreSQL、SQLite 等

```bash
yum install -y mariadb-server
```

## 1.2. 启动数据库
1. 启动数据库

```bash
systemctl start mariadb-server
```

2. 验证数据库启动

```bash
ps aux | grep mariadb  # 检查进程

ss -lanp | grep 3306   # 检查端口
```

2. 基础配置

```bash
# 初始化数据库
mysql_secure_installation
```

按照提示删除 test 库，以及创建数据库的 root 等

## 1.3. 安装 gogs
1. 创建用于运行 gogs 的用户

```python
useradd git   # 创建 git 用户
su - git      # 切换到 git 用户
```

2. 访问 gogs 官网获取 gogs 安装包。
使用 git 用户在 Linux 执行下面命令下载 gogs 软件包

```bash
wget https://dl.gogs.io/0.11.86/gogs_0.11.86_linux_386.tar.gz
```

或者访问官方网站下载对应的软件包，然后手动上传

```bash
https://www.zhihu.com/question/313766183
```

![gogs](https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/gogs.png)
3. 解压软件包
在软件包所在目录，执行如下命令解压 gogs

```bash
tar xf gogs_0.11.86_linux_amd64.tar.gz
```

4. 导入数据库信息
进入解压完毕的 gogs 目录的 scripts 目录中去，导入数据库初始化数据

```bash
cd gogs/scripts
mysql -u root -p 123456 < mysql.sql
```

这里使用 mysql 的 root 用户导入
5. 创建程序访问数据库的用户名密码
在数据库中配置 gogs 连接数据库时使用的账号和密码

```bash
# bash
mysql -u root -p 123456

# sql
grant all on gogs.* to 'gogs'@'%' identified by '123456'   # 创建授权账户 gogs，密码为 123456, 可以登录的原地址是 %（表示任意地址）
flush privileges;  # 刷新用户权限
```

5. 创建 gogs 配置文件
官方建议在 gogs 的根目录下，创建一个 custom/conf 目录用于存放配置文件，在 gogs 解压好的目录 gogs 中执行如下命令

```bash
mkdir -p custom/conf

# 编写或者上传初始化的配置文件
vi app.ini
```

文件内容如下：

```bash
# 基础部分
APP_NAME = daxinGitServer
RUN_USER = git
RUN_MODE = dev

# 服务器部分
[server]
HTTP_ADDR = 0.0.0.0
HTTP_PORT = 3000

# 数据库部分
[database]
DB_TYPE = mysql
HOST = 127.0.0.1:3306
NAME = gogs
USER = gogs
PASSWD = 123456

# 安全部分
[security]
INSTALL_LOCK = false  # 首次访问时是否显示配置页面
SECRET_KEY = daxinGitServer:gogs
```

基础部分配置含义如下:  

名称 | 描述
----|----
`APP_NAME`| 应用名称，可以改成您的组织或公司名称
`RUN_USER`| 运行应用的用户名称，我们建议您使用 `git`，但如果您在个人计算机上运行 Gogs，请修改为您的系统用户名称。如果没有正确设置这个值，很可能导致您的应用崩溃
`RUN_MODE`| 鉴于性能和其它考虑，建议在部署环境下修改为 `prod` 模式。在您完成安装操作时，该值也会被设置为 `prod`  

服务器 (`server`) 部分配置含义如下：  

名称 | 描述
----|----
`HTTP_ADDR`| 应用 HTTP 监听地址
`HTTP_PORT`| 应用 HTTP 监听端口号  

数据库 (`database`) 部分配置含义如下：  

名称 | 描述
----|----
`DB_TYPE`| 数据库类型，可以是 `mysql`、`postgres`、`mssql` 或 `sqlite3`
`HOST`| 数据库主机地址与端口
`NAME`| 数据库名称
`USER`| 数据库用户名
`PASSWD`| 数据库用户密码  

安全 (`security`) 部分配置含义如下:

名称 | 描述
----|----
`INSTALL_LOCK`| 用于指示是否允许访问安装页面（该页面可以设置管理员帐号，因此该选项非常重要）
`SECRET_KEY`| 全局的加密密钥，** 务必修改该值以确保您的服务器安全 **（会在每次安装时自动生成随机字符串）  

[更多配置信息请点击这里哦](https://github.com/gogs/docs/blob/master/zh-CN/advanced/configuration_cheat_sheet.md)

## 1.4. 启动 gogs
在 gogs 的安装目录下运行下列命令

```bash
./gogs web 
```

使用 systemd 管理 gogs 的方法

```bash
# 拷贝 gogs 提供的 systemd 管理脚本至管理目录
cp gogs/scripts/systemd/gogs.service  /lib/systemd/system

# 启动服务
systemctl start gogs.service  

# 开机启动
systemctl enable gogs.service
```

## 1.5. 访问
利用浏览器访问服务区的 3000 端口即可，注意如果服务器开启了防火墙可以先关闭，或者添加访问策略

```bash
# 关闭防火墙
systemctl stop firewalld

# 关闭开机启动
systemctl disable firewalld
```

