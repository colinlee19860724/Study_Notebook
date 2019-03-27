- [1. CentOS7 系统简单 Python 环境使用](#1-centos7-系统简单-python-环境使用)
    - [1.1. 查看当前系统 Python 版本](#11-查看当前系统-python-版本)
    - [1.2. 使用 CentOS7 系统中的 Python3 版本](#12-使用-centos7-系统中的-python3-版本)
    - [1.3. CentOS7 系统中 Pycharm 环境使用](#13-centos7-系统中-pycharm-环境使用)
    - [1.4. Pycharm 中安装 Jupyter](#14-pycharm-中安装-jupyter)

# 1. CentOS7 系统简单 Python 环境使用

## 1.1. 查看当前系统 Python 版本

&emsp;&emsp;Python在CentOS7.6系统中默认已经安装完成，我们经常使用的 yum 包管理工具就是用Python语言实现的。我们可以使用 `python -V` 命令查看当前系统python的版本信息：  
```bash
[root@localhost ~]# python -V
Python 2.7.5
[root@localhost ~]#
```

&emsp;&emsp;如上图所示，系统中默认使用的python版本为 2.7.5  

&emsp;&emsp;要想运行python程序，我们可以使用python的交互解释运行环境，终端中直接输入 `python` 命令即可：  
```bash
[root@localhost ~]# python
Python 2.7.5 (default, Apr 11 2018, 07:36:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world")
hello world
>>> 
>>> exit()
[root@localhost ~]#
```

&emsp;&emsp;上图中进入交互解释运行环境，显示了 python 环境的相关信息。然后尝试执行了第一行代码 `print("hello world)`，成功运行并打印了 hello world 内容；接着我们执行了退出交互环境的函数 `exit()`，成功退出python交互解释环境。  

&emsp;&emsp;除了使用 python 交互解释环境，我们还可以直接编写 python 源代码文件使用 vim 编辑器编写一个简单的 hello.py ，然后使用 python 命令直接运行它，如图：
```bash
[root@localhost ~]# cat hello.py 
print("hello world")
[root@localhost ~]# python hello.py 
hello world
[root@localhost ~]# 
```

## 1.2. 使用 CentOS7 系统中的 Python3 版本

&emsp;&emsp;默认情况下 CentOS7 系统中自带的 Python 版本是2.7版本。我们当前学习的 Python 版本为 Python3 版本，所以我们可以通过 yum 软件包管理工具安装 python3 版本, 不过由于 CentOS7 的 Base 软件包仓库默认没有 Python3版本 ，因此查找失败，如下图:
```bash
[root@localhost ~]# yum list "*python3*"
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: centos.ustc.edu.cn
 * extras: mirrors.163.com
 * updates: mirrors.163.com
Error: No matching Packages to list
[root@localhost ~]# 
```

&emsp;&emsp;除了 Base 仓库，我们还可以使用 epel 仓库，要想使用 epel 仓库，我们需要先安装一下 epel 仓库，安装过程如下:
```bash
[root@localhost ~]# yum install epel-release -y
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirrors.njupt.edu.cn
 * extras: mirrors.163.com
 * updates: mirrors.163.com
Resolving Dependencies
--> Running transaction check
---> Package epel-release.noarch 0:7-11 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                Arch             Version         Repository        Size
================================================================================
Installing:
 epel-release           noarch           7-11            extras            15 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 15 k
Installed size: 24 k
Downloading packages:
warning: /var/cache/yum/x86_64/7/extras/packages/epel-release-7-11.noarch.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
Public key for epel-release-7-11.noarch.rpm is not installed
epel-release-7-11.noarch.rpm                               |  15 kB   00:00     
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Importing GPG key 0xF4A80EB5:
 Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>"
 Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
 Package    : centos-release-7-5.1804.el7.centos.x86_64 (@anaconda)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : epel-release-7-11.noarch                                     1/1 
  Verifying  : epel-release-7-11.noarch                                     1/1 

Installed:
  epel-release.noarch 0:7-11                                                    

Complete!
[root@localhost ~]# 
```

&emsp;&emsp;epel 仓库安装完毕后，我们使用 yum 命令再次查询 python3 ，发现有多个不同版本的 python3 软件包。这里我节选了一部分内容，如下图:
```bash
root@localhost ~]# yum list "*python3*"
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                     | 7.1 kB     00:00     
 * base: centos.ustc.edu.cn
 * epel: mirrors.yun-idc.com
 * extras: mirrors.163.com
 * updates: centos.ustc.edu.cn
epel                                                     | 4.7 kB     00:00     
(1/3): epel/x86_64/group_gz                                |  88 kB   00:00     
(2/3): epel/x86_64/updateinfo                              | 1.0 MB   00:03     
(3/3): epel/x86_64/primary_db                              | 6.6 MB   00:05     
Available Packages
abrt-addon-python3.noarch                2.1.11-49.el7                      epel
boost-python34.x86_64                    1.53.0-28.el7                      epel
boost-python34-devel.x86_64              1.53.0-28.el7                      epel
python3-urjtag.x86_64                    2017.10-2.el7                      epel
python3-virtualenv-doc.noarch            15.1.0-2.el7                       epel
python34.x86_64                          3.4.9-2.el7                        epel
python34-Cython.x86_64                   0.23.5-1.el7                       epel
python34-PyMySQL.noarch                  0.9.2-1.el7                        epel
python34-PyYAML.x86_64                   3.11-3.el7                         epel
·
·省略部分软件包信息.......
·
python34-aiosmtpd.noarch                 1.0-2.el7                          epel
python34-zope-interface.x86_64           4.3.3-1.el7                        epel
python34-zope-schema.noarch              4.4.1-2.el7                        epel
python34-zope-testing.noarch             4.1.2-2.el7                        epel
python36.x86_64                          3.6.6-2.el7                        epel
python36-PyYAML.x86_64                   3.11-3.el7                         epel
python36-asn1crypto.noarch               0.24.0-6.el7                       epel
python36-blosc.x86_64                    1.2.8-4.el7                        epel
python36-bsddb3.x86_64                   6.2.6-3.el7                        epel
python36-chardet.noarch                  2.3.0-4.el7                        epel
uwsgi-plugin-python34-gevent.x86_64      2.0.17.1-1.el7                     epel
uwsgi-plugin-python34-tornado.x86_64     2.0.17.1-1.el7                     epel
uwsgi-plugin-python36.x86_64             2.0.17.1-1.el7                     epel
uwsgi-plugin-python36-gevent.x86_64      2.0.17.1-1.el7                     epel
[root@localhost ~]# 
```

&emsp;&emsp; 根据上图中的 epel 仓库 python3 软件包信息，我们选择 python36.x86_64 版本进行安装，如图:
```bash
[root@localhost ~]# yum install python36 -y
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirrors.njupt.edu.cn
 * epel: mirrors.yun-idc.com
 * extras: mirrors.163.com
 * updates: mirrors.163.com
Resolving Dependencies
--> Running transaction check
---> Package python36.x86_64 0:3.6.6-2.el7 will be installed
--> Processing Dependency: python36-libs(x86-64) = 3.6.6-2.el7 for package: python36-3.6.6-2.el7.x86_64
--> Processing Dependency: libpython3.6m.so.1.0()(64bit) for package: python36-3.6.6-2.el7.x86_64
--> Running transaction check
---> Package python36-libs.x86_64 0:3.6.6-2.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package               Arch           Version                Repository    Size
================================================================================
Installing:
 python36              x86_64         3.6.6-2.el7            epel          66 k
Installing for dependencies:
 python36-libs         x86_64         3.6.6-2.el7            epel         8.6 M

Transaction Summary
================================================================================
Install  1 Package (+1 Dependent package)

Total download size: 8.6 M
Installed size: 36 M
Downloading packages:
warning: /var/cache/yum/x86_64/7/epel/packages/python36-3.6.6-2.el7.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID 352c64e5: NOKEY
Public key for python36-3.6.6-2.el7.x86_64.rpm is not installed
(1/2): python36-3.6.6-2.el7.x86_64.rpm                     |  66 kB   00:01     
(2/2): python36-libs-3.6.6-2.el7.x86_64.rpm                | 8.6 MB   00:29     
--------------------------------------------------------------------------------
Total                                              297 kB/s | 8.6 MB  00:29     
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
Importing GPG key 0x352C64E5:
 Userid     : "Fedora EPEL (7) <epel@fedoraproject.org>"
 Fingerprint: 91e9 7d7c 4a5e 96f1 7f3e 888f 6a2f aea2 352c 64e5
 Package    : epel-release-7-11.noarch (@extras)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : python36-libs-3.6.6-2.el7.x86_64                             1/2 
  Installing : python36-3.6.6-2.el7.x86_64                                  2/2 
  Verifying  : python36-3.6.6-2.el7.x86_64                                  1/2 
  Verifying  : python36-libs-3.6.6-2.el7.x86_64                             2/2 

Installed:
  python36.x86_64 0:3.6.6-2.el7                                                 

Dependency Installed:
  python36-libs.x86_64 0:3.6.6-2.el7                                            

Complete!
[root@localhost ~]#
```

&emsp;&emsp; python36 安装成功后，我们可以使用 rpm 命令查看一下 python36 具体包含哪些命令和文件，如图:
```bash
root@localhost ~]# rpm -ql python36
/usr/bin/pydoc3.6
/usr/bin/python3.6
/usr/bin/python3.6m
/usr/bin/python36
/usr/bin/pyvenv-3.6
/usr/share/doc/python36-3.6.6
/usr/share/doc/python36-3.6.6/README.rst
/usr/share/licenses/python36-3.6.6
/usr/share/licenses/python36-3.6.6/LICENSE
/usr/share/man/man1/python3.6.1.gz
[root@localhost ~]# 
```

&emsp;&emsp;与 python2.7 版本一样，python36 依旧可以使用交互解释环境和 python 命令模式运行代码，这里我就不演示交互解释环境，我们直接使用 python36 命令运行之前编写好的 hello.py 程序 如下图：
```bash
[root@localhost ~]# python36 -V
Python 3.6.6
[root@localhost ~]# python36 hello.py 
hello world
[root@localhost ~]# 
```

## 1.3. CentOS7 系统中 Pycharm 环境使用

&emsp;&emsp;之前演示的 hello.py 程序非常简单，属于演示测试。正常的 Python 项目根据业务需求和功能通常包含众多 python 源文件，再使用传统的 vim 进行编写和管理就不是和方便了。下面给大家在 Linux 环境下安装一款专业的集成开发工具 (IDE) Pycharm 。

&emsp;&emsp;安装 Pycharm 之前，我们现在 CentOS 系统中创建一个专门用来学习 Python 开发的用户，比如，我们创建一个用户叫 python、devops，ai 等，然后再退出 root 用户，使用新建的用户登录系统，如下图:
```bash
[root@localhost ~]# passwd python
Changing password for user python.
New password: 
BAD PASSWORD: The password fails the dictionary check - it is based on a dictionary word
Retype new password: 
passwd: all authentication tokens updated successfully.
[root@localhost ~]# 
```

&emsp;&emsp;使用刚才创建的 python 用户登录后，打开命令行终端，我们使用 wget 命令下载 pycharm 官网的`免费开源版`安装包 pycharm-community-2018.3.5.tar.gz ，如下图:
```bash
[python@localhost ~]$ wget https://download.jetbrains.com/python/pycharm-community-2018.3.5.tar.gz
--2019-03-25 17:27:00--  https://download.jetbrains.com/python/pycharm-community-2018.3.5.tar.gz
Resolving download.jetbrains.com (download.jetbrains.com)... 54.72.98.183, 52.18.241.155, 2a05:d018:93b:d103:524e:e6ed:6592:1823, ...
Connecting to download.jetbrains.com (download.jetbrains.com)|54.72.98.183|:443... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: https://download.jetbrains.8686c.com/python/pycharm-community-2018.3.5.tar.gz [following]
--2019-03-25 17:27:02--  https://download.jetbrains.8686c.com/python/pycharm-community-2018.3.5.tar.gz
Resolving download.jetbrains.8686c.com (download.jetbrains.8686c.com)... 60.221.21.254, 2408:876c:0:100::25
Connecting to download.jetbrains.8686c.com (download.jetbrains.8686c.com)|60.221.21.254|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 311914955 (297M) [application/octet-stream]
Saving to: ‘pycharm-community-2018.3.5.tar.gz’

100%[=================================================================================================>] 311,914,955 1.22MB/s   in 7m 53s 

2019-03-25 17:34:55 (644 KB/s) - ‘pycharm-community-2018.3.5.tar.gz’ saved [311914955/311914955]

[python@localhost ~]$
[python@localhost ~]$ ll
total 304644
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Desktop
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Documents
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Downloads
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Music
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Pictures
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Public
-rw-rw-r--. 1 python python 311914955 Feb 27 19:15 pycharm-community-2018.3.5.tar.gz
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Templates
drwxr-xr-x. 2 python python      4096 Mar 25 17:02 Videos
[python@localhost ~]$
```

&emsp;&emsp;上图中，下载软件包过程比较慢，建议提前下载好对应的软件包，方便后续安装操作。安装过程比较简单，直接解压开就可以使用:
```bash
[python@localhost ~]$ mkdir software
[python@localhost ~]$ cd software/
[python@localhost software]$ cd ..
[python@localhost ~]$ tar xf pycharm-community-2018.3.5.tar.gz -C software/
[python@localhost ~]$ cd software
[python@localhost software]$ mv pycharm-community-2018.3.5 pycharm180305
[python@localhost software]$ cd pycharm180305/
[python@localhost pycharm180305]$ cd bin
[python@localhost bin]$ ls
format.sh     fsnotifier-arm   libdbm64.so  pycharm64.vmoptions  pycharm.svg
fsnotifier    idea.properties  log.xml      pycharm.png          pycharm.vmoptions
fsnotifier64  inspect.sh       printenv.py  pycharm.sh           restart.py
[python@localhost bin]$ ./pycharm.sh 
Mar 25, 2019 5:45:20 PM java.util.prefs.FileSystemPreferences$1 run
INFO: Created user preferences directory.
Mar 25, 2019 5:45:20 PM java.util.prefs.FileSystemPreferences$6 run
WARNING: Prefs file removed in background /home/python/.java/.userPrefs/prefs.xml
[python@localhost bin]$ 
```

&emsp;&emsp;上图中直接可以在 pycharm 的bin目录下运行 pycharm.sh 但是当前的终端被占用了。  
&emsp;&emsp;下面我们设置一个 pycharm 的桌面快捷方程式，避免在终端中使用命令开启，具体步骤如下图:
```bash
[python@localhost ~]$ cd Desktop/
[python@localhost Desktop]$ touch pycharm.desktop 
[python@localhost Desktop]$ vi pycharm.desktop 
[python@localhost Desktop]$ cat pycharm.desktop 
[Desktop Entry]
Name=pycharm
Exec=/home/python/software/pycharm180305/bin/pycharm.sh
Type=Application
Icon=/home/python/software/pycharm180305/bin/pycharm.png
Terminal=false
[python@localhost Desktop]$ 
```

## 1.4. Pycharm 中安装 Jupyter

&emsp;&emsp;我们通过 CentOS7 系统桌面中创建的 pycharm 快捷方程式打开 pycharm ，创建一个 test 项目然后点击 pycharm中的控制台，进行 pip 的跟新和 jupyter 的安装，如图：
```bash
(venv) [python@localhost test]$ pip install --upgrade pip
(venv) [python@localhost test]$ pip install jupyter
(venv) [python@localhost test]$ jupyter notebook --ip=0.0.0.0 --port=8000
[I 18:25:00.814 NotebookApp] Serving notebooks from local directory: /home/python/PycharmProjects/test
[I 18:25:00.815 NotebookApp] The Jupyter Notebook is running at:
[I 18:25:00.815 NotebookApp] http://(localhost.localdomain or 127.0.0.1):8000/?token=f7d20e19f9abf2cd8323034c6a60e6bf0a3c30a98f866fbc
[I 18:25:00.815 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 18:25:00.833 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///run/user/1001/jupyter/nbserver-8326-open.html
    Or copy and paste one of these URLs:
        http://(localhost.localdomain or 127.0.0.1):8000/?token=f7d20e19f9abf2cd8323034c6a60e6bf0a3c30a98f866fbc
^C[I 18:25:14.249 NotebookApp] interrupted
Serving notebooks from local directory: /home/python/PycharmProjects/test
0 active kernels
The Jupyter Notebook is running at:
http://(localhost.localdomain or 127.0.0.1):8000/?token=f7d20e19f9abf2cd8323034c6a60e6bf0a3c30a98f866fbc
Shutdown this notebook server (y/[n])? y
[C 18:25:16.200 NotebookApp] Shutdown confirmed
[I 18:25:16.210 NotebookApp] Shutting down 0 kernels
(venv) [python@localhost test]$
```