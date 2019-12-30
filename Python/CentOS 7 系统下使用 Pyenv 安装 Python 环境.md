---

[TOC]

---

# 1. CentOS 7 系统下使用 Pyenv 安装 Python 环境

## 1.1. Pyenv 介绍

&emsp;&emsp;Pyenv 是一款解决 Python 多版本环境使用的管理工具，它源自 rbenv 和 ruby-build 。通过 pyenv 我们可以同时编译安装部署多个 Python 环境，方便多 python 版本开发调试项目。详细介绍可以访问 pyenv 项目主页：[https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)  

## 1.2. Linux 环境下安装 Pyenv

&emsp;&emsp;安装 pyenv 比较简单，仅需将 pyenv 项目下载到当前用户家目录，然后配置指定的环境变量后即可使用。由于 pyenv 项目存放在 github 上，因此我们可以使用 git 命令 clone 到用户家目录。下面我们在 CentOS 7 系统上用 python 用户演示一下安装的具体过程:

```bash
[python@localhost ~]$ su -l root
Password: 
Last login: Tue Apr  2 16:07:47 CST 2019 on pts/0
[root@localhost ~]# yum install git
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirrors.163.com
 * extras: mirrors.cn99.com
 * updates: mirrors.cn99.com
Package git-1.8.3.1-20.el7.x86_64 already installed and latest version
Nothing to do
[root@localhost ~]# exit
logout
[python@localhost ~]$ git clone https://github.com/pyenv/pyenv.git .pyenv
Cloning into '.pyenv'...
remote: Enumerating objects: 81, done.
remote: Counting objects: 100% (81/81), done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 16818 (delta 37), reused 61 (delta 28), pack-reused 16737
Receiving objects: 100% (16818/16818), 3.29 MiB | 463.00 KiB/s, done.
Resolving deltas: 100% (11379/11379), done.
[python@localhost ~]$ ls -adl .pyenv
drwxrwxr-x. 11 python python 4096 Apr  2 16:13 .pyenv
[python@localhost ~]$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
[python@localhost ~]$
[python@localhost ~]$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
[python@localhost ~]$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
[python@localhost ~]$ pyenv
bash: pyenv: command not found...
[python@localhost ~]$
[python@localhost ~]$ source .bashrc 
[python@localhost ~]$ pyenv
pyenv 1.2.9-35-gb610909
Usage: pyenv <command> [<args>]
  Some useful pyenv commands are:
   commands    List all available pyenv commands
   local       Set or show the local application-specific Python version
   global      Set or show the global Python version
   shell       Set or show the shell-specific Python version
   install     Install a Python version using python-build
   uninstall   Uninstall a specific Python version
   rehash      Rehash pyenv shims (run this after installing executables)
   version     Show the current Python version and its origin
   versions    List all Python versions available to pyenv
   which       Display the full path to an executable
   whence      List all Python versions that contain the given executable
  See `pyenv help <command>` for information on a specific command.
For full documentation, see: https://github.com/pyenv/pyenv#readme
```

上图中成功安装完成 Pyenv

## 1.3. 使用 pyenv 编译安装 Python 环境

&emsp;&emsp;pyenv 的基础功能就是安装不同版本的 Python ，具体的选项为 `install` 除了 install 选项以外，还有其他选项，详情可参考 [Pyenv 选项文档](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md) 。使用 `pyenv install --list` 可以列出当前 pyenv 工具支持的 Python 版本，将 --list 改为具体的版本号后，可以完成具体 Python 环境的安装， 下面我们演示一下:  

```bash
[python@localhost ~]$ pyenv install --list
Available versions:
  2.1.3
  ...
  省略部分具体版本
  ...
  3.5.7
  3.6.0
  3.6-dev
  3.6.1
  3.6.2
  3.6.3
  3.6.4
  3.6.5
  3.6.6
  3.6.7
  ...
  省略部分具体版本
  ...
[python@localhost ~]$
[python@localhost ~]$ pyenv install -v 3.6.3
/tmp/python-build.20190402172510.109803 ~
Downloading Python-3.6.3.tar.xz...
-> https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
/tmp/python-build.20190402172510.109803/Python-3.6.3 /tmp/python-build.20190402172510.109803 ~
Installing Python-3.6.3...
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for python3.6... no
checking for python3... no
checking for python... python
checking for --enable-universalsdk... no
checking for --with-universal-archs... no
checking MACHDEP... linux
checking for --without-gcc... no
checking for --with-icc... no
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: in `/tmp/python-build.20190402172510.109803/Python-3.6.3`:
configure: error: no acceptable C compiler found in $PATH
See `config.log` for more details
  BUILD FAILED (CentOS Linux 7 using python-build 1.2.9-35-gb610909)
  Inspect or clean up the working tree at /tmp/python-build.20190402172510.109803
Results logged to /tmp/python-build.20190402172510.109803.log
  Last 10 log lines:
checking for --with-universal-archs... no
checking MACHDEP... linux
checking for --without-gcc... no
checking for --with-icc... no
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: in `/tmp/python-build.20190402172510.109803/Python-3.6.3`:
configure: error: no acceptable C compiler found in $PATH
See `config.log` for more details
```

&emsp;&emsp;上图中使用 `Pyenv install -v 3.6.3` 提示编译安装的错误信息，这是因为 Pyenv 底层安装 Python 环境是通过编译安装实现的，而我的系统中并未提供编译安装所依赖的软件包。那好，下面我们先在系统中安装完成编译 python 所依赖的所有软件包，如图:

```bash
[python@localhost ~]$ su -l root
Password: 
Last login: Tue Apr  2 16:24:02 CST 2019 on :0
[root@localhost ~]#
[root@localhost ~]# yum install -y gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel ncurses-devel libffi-devel
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirrors.163.com
 * extras: mirrors.cn99.com
 * updates: mirrors.cn99.com
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
[root@localhost ~]# exit
logout
[python@localhost ~]$
[python@localhost ~]$ pyenv install -v 3.6.3
/tmp/python-build.20190402174323.1818 ~
Downloading Python-3.6.3.tar.xz...
-> https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
...
省略编译安装具体过程
...
Installing collected packages: setuptools, pip
Successfully installed pip-9.0.1 setuptools-28.8.0
Installed Python-3.6.3 to /home/python/.pyenv/versions/3.6.3
  /tmp/python-build.20190402174323.1818 ~
~
[python@localhost ~]$
```

&emsp;&emsp;上图中顺利完成 python3.6.3 这个版本的安装工作。但是有的时候网络不好，下载源码包比较慢这时我们可以在 .pyenv 目录内创建 cache 文件夹，然后使用内网的 ftp 服务器下载指定的 python版本，然后再使用 pyenv install 安装，这样可以节省时间，如图:

```bash
[python@localhost ~]$ cd .pyenv/
[python@localhost .pyenv]$ ls
bin           completions  LICENSE   pyenv.d    src                  versions
CHANGELOG.md  CONDUCT.md   Makefile  README.md  terminal_output.png
COMMANDS.md   libexec      plugins   shims      test
[python@localhost .pyenv]$ 
[python@localhost .pyenv]$ mkdir cache
[python@localhost .pyenv]$ cd cache/
[python@localhost cache]$ 
[python@localhost cache]$ lftp 172.20.0.1/pub/software
cd ok, cwd=/pub/software
lftp 172.20.0.1:/pub/software> ls
-rw-r--r--    1 0        0        15324736 Mar 18 00:57 Python-3.5.7.tar.xz
-rw-r--r--    1 0        0        22673115 Oct 03  2017 Python-3.6.3.tgz
-rw-r--r--    1 0        0        17212420 Dec 24 03:02 Python-3.6.8.tar.xz
-rw-r--r--    1 0        0        17108364 Mar 25 20:59 Python-3.7.3.tar.xz
-rw-r--r--    1 0        0        332489780 Apr 03 12:38 pycharm-community-2019.1.1.tar.gz
lftp 172.20.0.1:/pub/software> mget Python*
72318635 bytes transferred in 1 second (63.98M/s)           Total 4 files transferred
lftp 172.20.0.1:/pub/software> exit
[python@localhost cache]$ ll
total 70632
-rw-rw-r--. 1 python python 15324736 Mar 18 08:57 Python-3.5.7.tar.xz
-rw-rw-r--. 1 python python 22673115 Oct  3  2017 Python-3.6.3.tgz
-rw-rw-r--. 1 python python 17212420 Dec 24 11:02 Python-3.6.8.tar.xz
-rw-rw-r--. 1 python python 17108364 Mar 26 04:59 Python-3.7.3.tar.xz
[python@localhost cache]$ cd
```

&emsp;&emsp;完成上面的操作后，再次使用 pyenv install 命令安装对应的 python 版本时，会跳过下载软件包的过程，直接使用 cache 路径下的源码包。

&emsp;&emsp;上面我们演示了通过 pyenv 成功的安装了 python3.6.3，那我们如何查看刚安装完成的 python 呢 ？下面介绍一下 Pyenv 的 versions 选项:

```bash
[python@localhost ~]$ pyenv  versions --help
Usage: pyenv versions [--bare] [--skip-aliases]
  Lists all Python versions found in `$PYENV_ROOT/versions/*'.
[python@localhost ~]$
```

&emsp;&emsp;versions 可以列出 pyenv 已安装的所有 python 版本，具体位置在 .pyenv 的 versions 文件夹下，我们可以进入该文件里查看一下，如图:

```bash
[python@localhost ~]$ pwd
/home/python
[python@localhost ~]$ cd .pyenv/
[python@localhost .pyenv]$ ll
total 204
drwxrwxr-x. 2 python python   4096 Apr  2 16:27 bin
-rw-rw-r--. 1 python python  25848 Apr  2 16:27 CHANGELOG.md
-rw-rw-r--. 1 python python   7522 Apr  2 16:27 COMMANDS.md
drwxrwxr-x. 2 python python   4096 Apr  2 16:27 completions
-rw-rw-r--. 1 python python   3390 Apr  2 16:27 CONDUCT.md
drwxrwxr-x. 2 python python   4096 Apr  2 16:27 libexec
-rw-rw-r--. 1 python python   1092 Apr  2 16:27 LICENSE
-rw-rw-r--. 1 python python    406 Apr  2 16:27 Makefile
drwxrwxr-x. 3 python python   4096 Apr  2 16:27 plugins
drwxrwxr-x. 4 python python   4096 Apr  2 16:27 pyenv.d
-rw-rw-r--. 1 python python  15752 Apr  2 16:27 README.md
drwxrwxr-x. 2 python python   4096 Apr  2 17:46 shims
drwxrwxr-x. 2 python python   4096 Apr  2 16:27 src
-rw-rw-r--. 1 python python 104764 Apr  2 16:27 terminal_output.png
drwxrwxr-x. 3 python python   4096 Apr  2 16:27 test
drwxrwxr-x. 3 python python   4096 Apr  2 17:43 versions
[python@localhost .pyenv]$ cd versions/
[python@localhost versions]$ ll
total 4
drwxr-xr-x. 6 python python 4096 Apr  2 17:46 3.6.3
[python@localhost versions]$ cd 3.6.3/
[python@localhost 3.6.3]$ ll
total 16
drwxr-xr-x. 2 python python 4096 Apr  2 17:46 bin
drwxr-xr-x. 3 python python 4096 Apr  2 17:46 include
drwxr-xr-x. 4 python python 4096 Apr  2 17:46 lib
drwxr-xr-x. 3 python python 4096 Apr  2 17:46 share
[python@localhost 3.6.3]$ cd bin/
[python@localhost bin]$ ll
total 24808
lrwxrwxrwx. 1 python python        8 Apr  2 17:46 2to3 -> 2to3-3.6
-rwxrwxr-x. 1 python python      125 Apr  2 17:46 2to3-3.6
lrwxrwxrwx. 1 python python       16 Apr  2 17:46 easy_install -> easy_install-3.6
-rwxrwxr-x. 1 python python      266 Apr  2 17:46 easy_install-3.6
lrwxrwxrwx. 1 python python        7 Apr  2 17:46 idle -> idle3.6
lrwxrwxrwx. 1 python python        7 Apr  2 17:46 idle3 -> idle3.6
-rwxrwxr-x. 1 python python      123 Apr  2 17:46 idle3.6
lrwxrwxrwx. 1 python python        6 Apr  2 17:46 pip -> pip3.6
-rwxrwxr-x. 1 python python      238 Apr  2 17:46 pip3
-rwxrwxr-x. 1 python python      238 Apr  2 17:46 pip3.6
lrwxrwxrwx. 1 python python        8 Apr  2 17:46 pydoc -> pydoc3.6
lrwxrwxrwx. 1 python python        8 Apr  2 17:46 pydoc3 -> pydoc3.6
-rwxrwxr-x. 1 python python      108 Apr  2 17:46 pydoc3.6
lrwxrwxrwx. 1 python python        9 Apr  2 17:46 python -> python3.6
lrwxrwxrwx. 1 python python        9 Apr  2 17:46 python3 -> python3.6
-rwxr-xr-x. 2 python python 12650352 Apr  2 17:45 python3.6
lrwxrwxrwx. 1 python python       17 Apr  2 17:46 python3.6-config -> python3.6m-config
-rwxr-xr-x. 1 python python    63994 Apr  2 17:46 python3.6-gdb.py
-rwxr-xr-x. 2 python python 12650352 Apr  2 17:45 python3.6m
-rwxr-xr-x. 1 python python     3141 Apr  2 17:46 python3.6m-config
lrwxrwxrwx. 1 python python       16 Apr  2 17:46 python3-config -> python3.6-config
lrwxrwxrwx. 1 python python       16 Apr  2 17:46 python-config -> python3.6-config
lrwxrwxrwx. 1 python python       10 Apr  2 17:46 pyvenv -> pyvenv-3.6
-rwxrwxr-x. 1 python python      465 Apr  2 17:46 pyvenv-3.6
[python@localhost bin]$ cd
```

&emsp;&emsp;通过上图，我们发现，pyenv 将编译安装的具体版本 python 程序直接安装到了 pyenv 的versions 目录下。 下面我们使用 pyenv 的 versions 选项命令 查看 pyenv 下都安装了哪些具体的版本，如图:

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
[python@localhost ~]$ python -V
Python 2.7.5
[python@localhost ~]$
```

&emsp;&emsp;上图中 pyenv versions 命令执行后返回了两个 python 版本，system 代表 CentOS 7 系统自带的 python2.7 版本， 3.6.3 代表我们之前通过 pyenv 安装的 python3.6.3 版本。system 前面的 `*` 代表当前 shell 环境生效的 python 版本。  

&emsp;&emsp;现在我们可以方便的使用 pyenv 安装各种版本，当然之后也可以使用 uninstall 选项删除之前安装的具体版本，比如我们先安装一个 python3.6.6 然后再使用 `pyenv uninstall 3.6.3` 卸载 Python3.6.3 版本,演示过程如下:

```bash
[python@localhost ~]$ pyenv install 3.6.6
Downloading Python-3.6.6.tar.xz...
-> https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz
Installing Python-3.6.6...
Installed Python-3.6.6 to /home/python/.pyenv/versions/3.6.6
  [python@localhost ~]$ 
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.6
[python@localhost ~]$ pyenv uninstall 3.6.3
pyenv: remove /home/python/.pyenv/versions/3.6.3? y
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.6
[python@localhost ~]$
```

## 1.4. 使用 pyenv global 指定系统 python 环境

&emsp;&emsp;默认情况下 pyenv 显示的是系统默认的环境变量 2.7.5 版本，我们可以使用 global 选项来指定我们想要 python 版本， 如图：

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ python -V
Python 2.7.5
[python@localhost ~]$ pyenv global 3.6.8
[python@localhost ~]$ pyenv versions
  system
  3.6.3
* 3.6.8 (set by /home/python/.pyenv/version)
  3.7.3
[python@localhost ~]$ python -V
Python 3.6.8
[python@localhost ~]$
```

&emsp;&emsp;通过上面的演示，我们发现，使用 global 选项指定当前 python 版本是通过在 `.pyenv` 目录中的 version 文件指定的，下面我们看一下这个文件:

```bash
[python@localhost ~]$ cd .pyenv/
[python@localhost .pyenv]$ ll
total 208
drwxrwxr-x. 2 python python   4096 Apr  2 20:22 bin
-rw-rw-r--. 1 python python  25848 Apr  2 20:22 CHANGELOG.md
-rw-rw-r--. 1 python python   7522 Apr  2 20:22 COMMANDS.md
drwxrwxr-x. 2 python python   4096 Apr  2 20:22 completions
-rw-rw-r--. 1 python python   3390 Apr  2 20:22 CONDUCT.md
drwxrwxr-x. 2 python python   4096 Apr  2 20:22 libexec
-rw-rw-r--. 1 python python   1092 Apr  2 20:22 LICENSE
-rw-rw-r--. 1 python python    406 Apr  2 20:22 Makefile
drwxrwxr-x. 3 python python   4096 Apr  2 20:22 plugins
drwxrwxr-x. 4 python python   4096 Apr  2 20:22 pyenv.d
-rw-rw-r--. 1 python python  15752 Apr  2 20:22 README.md
drwxrwxr-x. 2 python python   4096 Apr  3 10:38 shims
drwxrwxr-x. 2 python python   4096 Apr  2 20:22 src
-rw-rw-r--. 1 python python 104764 Apr  2 20:22 terminal_output.png
drwxrwxr-x. 3 python python   4096 Apr  2 20:22 test
-rw-rw-r--. 1 python python      6 Apr  3 14:55 version
drwxrwxr-x. 5 python python   4096 Apr  2 20:43 versions
[python@localhost .pyenv]$ cat version
3.6.8
[python@localhost .pyenv]$
```

&emsp;&emsp;通过上图的查看过程，发现 version 就是一个普通文本文件，内部指定了3.6.8这个编号，下面我们将这个文件修改一下，3.6.8 修改为 3.6.3 ，或者把这个文件删除，看看当前的 python 环境有什么变化，如图:  

```bash
[python@localhost .pyenv]$ cd 
[python@localhost ~]$ echo "3.6.3" > .pyenv/version
[python@localhost ~]$ cat .pyenv/version
3.6.3
[python@localhost ~]$ pyenv versions
  system
* 3.6.3 (set by /home/python/.pyenv/version)
  3.6.8
  3.7.3
[python@localhost ~]$ python -V
Python 3.6.3
[python@localhost ~]$ rm -rf .pyenv/version
[python@localhost ~]$ cat .pyenv/version
cat: .pyenv/version: No such file or directory
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ python -V
Python 2.7.5
[python@localhost ~]$
```

&emsp;&emsp;上图的演示过程充分揭示了 global 选项指定当前 python 版本的方法，没有 version 文件的情况下，默认使用系统中自带的 python 版本， 有了 version 文件后，使用 version 文件中指定的 python 版本。  

&emsp;&emsp;之前对 global 的用法已经可以满足通常的使用场景，但是有的时候我们可以使用 global 的高级用法，我们看一下下面的执行过程，可以发现一些新的特性：

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ python -V
Python 2.7.5
[python@localhost ~]$ python2.7 -V
Python 2.7.5
[python@localhost ~]$ python3 -V
pyenv: python3: command not found
  The `python3` command exists in these Python versions:
  3.6.3
  3.6.8
  3.7.3
  [python@localhost ~]$ python3.6 -V
pyenv: python3.6: command not found
  The `python3.6` command exists in these Python versions:
  3.6.3
  3.6.8
  [python@localhost ~]$ python3.6.3 -V
bash: python3.6.3: command not found...
[python@localhost ~]$
```

&emsp;&emsp;上图中没有设置 global 环境，系统默认为 python2.7.5 ，在命令行中执行 python 或者 python2.7 时，最终都使用的是 python2.7.5 ; 当执行 python3 或者 python3.x 时，提示 pyenv 中有对应版本;直接指定对应的系统版本时，若不在 version 文件中，则提示命令找不到，无法使用。因此我们可以使用 global 同时定义多个 python3 系列，然后同时使用多个版本，如下图:

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ cat .pyenv/version
cat: .pyenv/version: No such file or directory
[python@localhost ~]$ pyenv global 3.6.8 3.6.3 3.7.3
[python@localhost ~]$ pyenv versions
  system
* 3.6.3 (set by /home/python/.pyenv/version)
* 3.6.8 (set by /home/python/.pyenv/version)
* 3.7.3 (set by /home/python/.pyenv/version)
[python@localhost ~]$ python -V
Python 3.6.8
[python@localhost ~]$ python3 -V
Python 3.6.8
[python@localhost ~]$ python3.6 -V
Python 3.6.8
[python@localhost ~]$ python3.7 -V
Python 3.7.3
[python@localhost ~]$
```

&emsp;&emsp;上图中我们连续设置了3个 python 版本，发现他们同时生效，但是最终python命令生效的版本是 3.6.8 即我们 global 变量后第一个 python版本 3.6.8 ； python3 和 python3.6 都为 3.6.8；如果直接执行python 3.7，则使用的是 python3.7.3；高级用法大家了解一下就好，尽量不要把自己的 python 环境搞得太复杂。

## 1.5. 使用 pyenv shell 指定系统 python 环境

&emsp;&emsp;除了使用上一小节中的 global 选项外，我们还可以通过 shell 选项设置当前系统的环境变量，和 global 用法相仿，下面我们演示一下:

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ pyenv shell 3.6.3
[python@localhost ~]$ pyenv versions
  system
* 3.6.3 (set by PYENV_VERSION environment variable)
  3.6.8
  3.7.3
[python@localhost ~]$ echo  $PYENV_VERSION
3.6.3
[python@localhost ~]$ PYENV_VERSION=3.6.8
[python@localhost ~]$
[python@localhost ~]$ pyenv versions
  system
  3.6.3
* 3.6.8 (set by PYENV_VERSION environment variable)
  3.7.3
[python@localhost ~]$ unset PYENV_VERSION
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$
[python@localhost ~]$ export PYENV_VERSION=3.7.3
[python@localhost ~]$ pyenv versions
  system
  3.6.3
  3.6.8
* 3.7.3 (set by PYENV_VERSION environment variable)
[python@localhost ~]$
```

&emsp;&emsp;通过上图的演示过程，我们可以使用 shell 选项指定当前系统的 python 版本， 我们发现 shell 选项方式和 global 不同，他将 python 的版本信息放到当前 shell 环境变量 PYENV_VERSION 中， 我们可以直接操作该变量，通过改变他的值实现 python 不同版本的切换，也可以直接使用 Linux 中的 unset 命令删除这个变量。删除后，pyenv 恢复到 global 所指定的 python 版本，这也说明 shell 选项设置的 python 版本优先级高于 global 设置的。虽然大家了解了 shell 选项的实现原理，但是还是建议大家使用 pyenv 命令来维护系统中的 python 版本，不建议直接操作对应的系统变量。比如，我们可以使用 --unset 来取消 shell 选项设置的 python 版本，如图：

```bash
[python@localhost ~]$ pyenv global 3.7.3
[python@localhost ~]$ pyenv versions
  system
  3.6.3
  3.6.8
* 3.7.3 (set by /home/python/.pyenv/version)
[python@localhost ~]$ pyenv shell 3.6.8
[python@localhost ~]$ pyenv versions
  system
  3.6.3
* 3.6.8 (set by PYENV_VERSION environment variable)
  3.7.3
[python@localhost ~]$ pyenv shell --unset
[python@localhost ~]$ pyenv versions
  system
  3.6.3
  3.6.8
* 3.7.3 (set by /home/python/.pyenv/version)
[python@localhost ~]$
```

&emsp;&emsp;shell 选项和 global 选项类似， 也可以同时制定多个 python 版本， 具体实现是在 `PYENV_VERSION`环境变量中用 `:` 分隔多个 Python 版本号，如下图:

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ pyenv shell 3.6.3 3.6.8 3.7.3
[python@localhost ~]$
[python@localhost ~]$ pyenv versions
  system
* 3.6.3 (set by PYENV_VERSION environment variable)
* 3.6.8 (set by PYENV_VERSION environment variable)
* 3.7.3 (set by PYENV_VERSION environment variable)
[python@localhost ~]$
[python@localhost ~]$ echo $PYENV_VERSION
3.6.3:3.6.8:3.7.3
[python@localhost ~]$ python -V
Python 3.6.3
[python@localhost ~]$ python3.6 -V
Python 3.6.3
[python@localhost ~]$ python3.7 -V
Python 3.7.3
[python@localhost ~]$ pyenv shell --unset
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$
```

## 1.6. 使用 pyenv local 指定系统 python 环境

&emsp;&emsp;下面给大家介绍最后一个可以改变系统环境变量的 pyenv 选项 local ，该选项可以指定当前路径和其子目录下的 Python 版本，即在指定目录内执行 python 时才有效的 python 版本。演示如下:

```bash
[python@localhost ~]$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
[python@localhost ~]$ mkdir MyProject
[python@localhost ~]$ cd MyProject/
[python@localhost MyProject]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost MyProject]$ pyenv local 3.6.8
[python@localhost MyProject]$ pyenv versions
  system
  3.6.3
* 3.6.8 (set by /home/python/MyProject/.python-version)
  3.7.3
[python@localhost MyProject]$ ls -al
total 12
drwxrwxr-x.  2 python python 4096 Apr  4 10:18 .
drwx------. 18 python python 4096 Apr  4 10:17 ..
-rw-rw-r--.  1 python python    6 Apr  4 10:18 .python-version
[python@localhost MyProject]$ cat .python-version 
3.6.8
[python@localhost MyProject]$ cd
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$
```

&emsp;&emsp;现在我们演示一下 global shell local 三种选项同时使用，观察一下哪种的优先级最高:

```bash
[python@localhost ~]$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.6.3
  3.6.8
  3.7.3
[python@localhost ~]$ pyenv global 3.6.3
[python@localhost ~]$ pyenv versions
  system
* 3.6.3 (set by /home/python/.pyenv/version)
  3.6.8
  3.7.3
[python@localhost ~]$ pyenv shell 3.6.8
[python@localhost ~]$ pyenv versions
  system
  3.6.3
* 3.6.8 (set by PYENV_VERSION environment variable)
  3.7.3
[python@localhost ~]$ cd MyProject/
[python@localhost MyProject]$ pyenv local 3.7.3
[python@localhost MyProject]$ pyenv versions
  system
  3.6.3
* 3.6.8 (set by PYENV_VERSION environment variable)
  3.7.3
[python@localhost MyProject]$ pyenv shell --unset
[python@localhost MyProject]$ pyenv versions
  system
  3.6.3
  3.6.8
* 3.7.3 (set by /home/python/MyProject/.python-version)
[python@localhost MyProject]$ cd 
[python@localhost ~]$ pyenv versions
  system
* 3.6.3 (set by /home/python/.pyenv/version)
  3.6.8
  3.7.3
[python@localhost ~]$
```

&emsp;&emsp;通过上面的演示，我们发现 shell 选项定义的 python 版本优先级最高，他会覆盖 local 选项指定的python 版本，然后 local 选项的优先级高于 global 选项的优先级。

&emsp;&emsp;我们可以在 pycharm 中直接使用在 .pyenv/versions 中安装的各种 python 版本。