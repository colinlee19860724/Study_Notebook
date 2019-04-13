- [1. CentOS7 系统编译安装 Python3 环境](#1-centos7-系统编译安装-python3-环境)
    - [1.1. 准备编译环境](#11-准备编译环境)
    - [1.2. 获取 Python3 源码包](#12-获取-python3-源码包)
    - [1.3. 编译安装 Python3.7.3](#13-编译安装-python373)
    - [1.4. 配置环境变量](#14-配置环境变量)
    - [1.5. 再次编译其他 Python 版本](#15-再次编译其他-python-版本)

# 1. CentOS 7 系统编译安装 Python 3 环境

## 1.1. 准备编译环境

&emsp;&emsp;编译安装 Python之前，我们还需要准备好编译环境。下面我们在CentOS7 系统中安装具体编译软件和 Python 依赖的软件包，如下：
```bash
[root@localhost ~]# yum install -y gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel ncurses-devel libffi-devel
.
.省略安装过程
.
[root@localhost bin]# yum install -y gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel ncurses-devel libffi-devel
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirrors.huaweicloud.com
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Package gcc-4.8.5-36.el7_6.1.x86_64 already installed and latest version
Package 1:make-3.82-23.el7.x86_64 already installed and latest version
Package patch-2.7.1-10.el7_5.x86_64 already installed and latest version
Package gdbm-devel-1.10-8.el7.x86_64 already installed and latest version
Package 1:openssl-devel-1.0.2k-16.el7_6.1.x86_64 already installed and latest version
Package sqlite-devel-3.7.17-8.el7.x86_64 already installed and latest version
Package readline-devel-6.2-10.el7.x86_64 already installed and latest version
Package zlib-devel-1.2.7-18.el7.x86_64 already installed and latest version
Package bzip2-devel-1.0.6-13.el7.x86_64 already installed and latest version
Package ncurses-devel-5.9-14.20130511.el7_4.x86_64 already installed and latest version
Package libffi-devel-3.0.13-18.el7.x86_64 already installed and latest version
Nothing to do
[root@localhost bin]# 
```

## 1.2. 获取 Python3 源码包

&emsp;&emsp;访问 [Python](https://www.python.org) 官方网站，下载指定版本的源代码包, 在网站 Download 导航栏中选择 Source code ，然后在跳转的页面中选择自己想要的 Python 版本，这里我们复制下载地址，使用 wget 命令下载 Python3.7.3，如图：
```bash
[root@localhost ~]# wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
--2019-03-27 16:44:04--  https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
Resolving www.python.org (www.python.org)... 151.101.228.223, 2a04:4e42:1a::223
Connecting to www.python.org (www.python.org)|151.101.228.223|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 22973527 (22M) [application/octet-stream]
Saving to: ‘Python-3.7.3.tgz’

100%[=========================================================>] 22,973,527   158KB/s   in 2m 42s 

2019-03-26 16:46:49 (139 KB/s) - ‘Python-3.7.3.tgz’ saved [22973527/22973527]

[root@localhost ~]# ll
total 22476
-rw-------. 1 root root     1866 Jan  4 22:24 anaconda-ks.cfg
-rw-r--r--. 1 root root 22973527 Mar 26 04:59 Python-3.7.3.tgz
[root@localhost ~]# 
```

## 1.3. 编译安装 Python3.7.3

&emsp;&emsp;编译安装首先解压源码包，然后进入解压目录，配置编译选项，编译，最后安装，如图:
```bash
[root@localhost ~]# tar xvf Python-3.7.3.tgz 
[root@localhost ~]# cd Python-3.7.3/
[root@localhost Python-3.7.3]# ls
aclocal.m4           config.sub    Doc      install-sh  m4               Misc     Parser   Programs       README.rst
CODE_OF_CONDUCT.rst  configure     Grammar  Lib         Mac              Modules  PC       pyconfig.h.in  setup.py
config.guess         configure.ac  Include  LICENSE     Makefile.pre.in  Objects  PCbuild  Python         Tools
[root@localhost Python-3.7.3]#
[root@localhost Python-3.7.3]# ./configure --prefix=/usr/local/python37
[root@localhost Python-3.7.3]# make
[root@localhost Python-3.7.3]# make install
[root@localhost Python-3.7.3]# cd /usr/local/python37/bin
[root@localhost bin]# ./python3.7 -V
Python 3.7.3
[root@localhost bin]# 
```

## 1.4. 配置环境变量

&emsp;&emsp;配置环境变量，在 `/etc/profile.d` 目录里创建配置文件，如图:
```bash
[root@localhost ~]# cd /etc/profile.d/
[root@localhost profile.d]# ls
256term.csh                   bash_completion.sh  colorls.csh  flatpak.sh  less.csh       sh.local  vte.sh
256term.sh                    colorgrep.csh       colorls.sh   lang.csh    less.sh        vim.csh   which2.csh
abrt-console-notification.sh  colorgrep.sh        csh.local    lang.sh     PackageKit.sh  vim.sh    which2.sh
[root@localhost profile.d]# vi python3.7.sh
[root@localhost profile.d]# cat python3.7.sh 
#!/bin/bash
export PATH=$PATH:/usr/local/python37/bin
[root@localhost profile.d]# source ./python3.7.sh 
[root@localhost profile.d]# python3.7 -V
Python 3.7.3
```

## 1.5. 再次编译其他 Python 版本

&emsp;&emsp;完成上面的编译安装过程后，可以再次尝试编译安装其他版本的 Python。  

Python-3.6.6 源码下载地址：[https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz](https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz)