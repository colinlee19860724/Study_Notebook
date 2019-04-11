
- [1. Linux 入门](#1-linux-入门)
    - [1.1. 开源 Open](#11-开源-open)
    - [1.2. Linux 哲学思想](#12-linux-哲学思想)
    - [1.3. 开发接口标准](#13-开发接口标准)
    - [1.4. 用户和内核空间](#14-用户和内核空间)
    - [1.5. Linux 版本](#15-linux-版本)
        - [1.5.1. 内核版本](#151-内核版本)
        - [1.5.2. 发行版本](#152-发行版本)
    - [1.6. systemd 初始化进程](#16-systemd-初始化进程)
        - [1.6.1. systemd 初始化进程服务](#161-systemd-初始化进程服务)
        - [1.6.2. System V init 运行级别](#162-system-v-init-运行级别)
        - [1.6.3. 运行级别](#163-运行级别)
    - [1.7. 用户登录](#17-用户登录)
    - [1.8. 什么是 Shell](#18-什么是-shell)
        - [1.8.1. bash shell](#181-bash-shell)
        - [1.8.2. 命令提示符](#182-命令提示符)
        - [1.8.3. 命令分类](#183-命令分类)
        - [1.8.4. bash 中常用快捷键](#184-bash-中常用快捷键)
    - [1.9. 必知必会命令](#19-必知必会命令)
    - [1.10. 如何获取帮助](#110-如何获取帮助)
        - [1.10.1. 通过本地文档获取帮助](#1101-通过本地文档获取帮助)
        - [1.10.2. 通过在线文档获取帮助](#1102-通过在线文档获取帮助)
        - [1.10.3. 其它网站和搜索](#1103-其它网站和搜索)

# 1. Linux 入门

## 1.1. 开源 Open 
- __软件分类__：  
  1. 商业  
  2. 共享  
  3. 自由 free  

- __开源__： 把软件程序与源代码文件一起打包提供给用户，让用户在不受限制地使用某个软件功能的基础上还可以按需进行修改，或编制成衍生产品再发布出去。用户具有使用自由、修改自由、重新发布自由以及创建衍生品的自由。开源软件最重要的特性有下面这些。  
  1. __低风险__：使用闭源软件无疑把命运交付给他人，一旦封闭的源代码没有人来维护，你将进退维谷；而且相较于商业软件公司，开源社区很少存在倒闭的问题。  
  2. __高品质__：相较于闭源软件产品，开源项目通常是由开源社区来研发及维护的，参与编写、维护、测试的用户量众多，一般的 bug 还没有等爆发就已经被修补。
  3. __低成本__：开源工作者都是在幕后默默且无偿地付出劳动成果，为美好的世界贡献一份力量，因此使用开源社区推动的软件项目可以节省大量的人力、物力和财力。
  4. __更透明__：没有哪个笨蛋会把木马、后门等放到开放的源代码中，这样无疑是把自己的罪行暴露在阳光之下。  
  
&emsp;&emsp;世界上的开源许可证，大概有上百种，常用的有 6 个，下面一图读懂主要的开源协议：  

<img alt="一图读懂主要的开源协议" src="https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/openSourceLicenses.png" width="700" align=middle />

-----------------------------------------------------
## 1.2. Linux 哲学思想
- 一切皆文件（包括硬件）
- 小型，单一用途的程序
- 链接程序，共同完成复杂的任务
- 避免令人困惑的用户界面
- 配置数据存储在文本中

-----------------------------------------------------
## 1.3. 开发接口标准
- __ABI（应用程序二进制接口）: Application Binary Interface__  
&emsp;&emsp;ABI 描述了应用程序与 OS 之间的底层接口，允许编译好的目标代码在使用兼容 ABI 的系统中无需改动就能运行  
- __API（应用程序编程接口）：Application Programming Interface__  
&emsp;&emsp;API 定义了源代码和库之间的接口，因此同样的源代码可以在支持这个 API 的任何系统中编译  
- __POSIX（可移植性操作系统接口）: Portable Operating System Interface__  
&emsp;&emsp;IEEE 在操作系统上定义的一系列 API 标准  
&emsp;&emsp;POSIX 兼容的程序可在其它 POSIXX 操作系统编译执行  
- __运行程序格式：__  
&emsp;&emsp;Windows: EXE, .dll (dynamic link library), .lib  
&emsp;&emsp;Linux: ELF, .so (shared object), .a  

-----------------------------------------------------
## 1.4. 用户和内核空间
- __用户空间：User space__  
&emsp;&emsp;用户程序的运行空间。为了安全，它们是隔离的，即使用户的程序崩溃，内核也不受影响，只能执行简单的运算，不能直接调用系统资源，必须通过系统接口（ system call），才能向内核发出指令。  
- __内核空间：Kernel space__  
&emsp;&emsp;是 Linux 内核的运行空间，可以执行任意命令，调用系统的一切资源。  

<img alt="用户和内核空间" src="https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/kernelSpaceAndUserSpaces.png" width="500" align=middle />

示例：
```c
str = "www.magedu.com" // 用户空间
x = x + 100            // 用户空间
file.write(str)        // 切换到内核空间
y = x + 200            // 切换回用户空间
```

&emsp;&emsp;第一行和第二行都是简单的赋值运算，在 User space 执行。第三行需要写入文件，就要切换到 Kernel space ，因为用户不能直接写文件，必须通过内核安排。第四行又是赋值运算，就切换回 User space 。  

-----------------------------------------------------
## 1.5. Linux 版本
### 1.5.1. 内核版本
&emsp;&emsp;查看内核 (kernel) 版本命令：`uname -r` 或 `cat /proc/version`  
&emsp;&emsp;linux 内核版本有两种：__稳定版__（次版本为偶数）和 __开发版__（次版本为奇数）。  
&emsp;&emsp;版本号：__[主版本].[次版本].[释出版本]-[修改版本]__  
&emsp;&emsp;如：__3.10.0-957.el7.x86_64__  
> __注：__  
> __主版本、次版本__：一般用头两个数字描述内核系列，主版本号和次版本号标志着重要的功能变动  
> __释出版本__：在主次版本架构不变的情况下，新增的功能累积到一定程度后释出的内核版本  
> __修改版本__：表示较小的功能变更，修改一些 bug 等  
> __el__ 表示 Enterprise Linux，7 表示 Centos7  
> __x86_64__ 表示 CPU 结构，即 64 位  

&emsp;&emsp;Linux 内核版本发布网站（The Linux Kernel Archives）：[https://www.kernel.org/](https://www.kernel.org/)

### 1.5.2. 发行版本
&emsp;&emsp;查看 RedHat 系列发行（distribution）版本命令：`cat /etc/redhat-release`  
&emsp;&emsp;Linux 发行版的名称和版本号是由发行版的维护者决定的  
&emsp;&emsp;主要的 Linux 发行版如下：  

- __slackware__：SUSE Linux Enterprise Server (SLES)  
&emsp;&emsp;&emsp;&emsp;&emsp;OpenSuse 桌面  
- __debian__：ubuntu，mint  
- __RedHat__：RHEL: RedHat Enterprise Linux&emsp; 每 18 个月发行一个新版本  
&emsp;&emsp;&emsp;&emsp;CentOS：兼容 RHEL 的格式，国内下载源  
&emsp;&emsp;&emsp;&emsp;中标麒麟：中标软件  
&emsp;&emsp;&emsp;&emsp;Fedora：每 6 个月发行一个新版本  
- __ArchLinux__：轻量简洁  
- __Gentoo__：极致性能，不提供传统意义的安装程序  
- __LFS__：Linux From scratch 自制 Linux  
- __Android__：kernel+busybox（工具集）+java 虚拟机  
- __Linux 分支参考网站__：[http://futurist.se/gldt/](http://futurist.se/gldt/)  
- __阿里巴巴开源镜像站__：[https://opsx.alibaba.com/mirror](https://opsx.alibaba.com/mirror)
- __网易开源镜像站__：[http://mirrors.163.com/](http://mirrors.163.com/)

-----------------------------------------------------
## 1.6. systemd 初始化进程
&emsp;&emsp;Linux 操作系统的开机过程是这样的，即从 BIOS 开始，然后进入 Boot Loader，再加载系统内核，然后内核进行初始化，最后启动初始化进程。初始化进程作为 Linux 系统的第一个进程，它需要完成 Linux 系统中相关的初始化工作，为用户提供合适的工作环境。红帽 RHEL 7 系统已经替换掉了熟悉的初始化进程服务 System V init，正式采用全新的 systemd 初始化进程服务。systemd 初始化进程服务采用了并发启动机制，开机速度得到了不小的提升。  
 
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__systemd 与 System V init 的区别以及作用__

System V init 运行级别 | systemd 目标名称  | 作用
:------------------:|:---------------|:-----
0|runlevel0.target, poweroff.target  | 关机
1|runlevel1.target, rescue.target    | 单用户模式
2|runlevel2.target, multi-user.target | 等同于级别 3
3|runlevel3.target, multi-user.target | 多用户的文本界面
4|runlevel4.target, multi-user.target | 等同于级别 3
5|runlevel5.target, graphical.target | 多用户的图形界面
6|runlevel6.target, reboot.target    | 重启
emergency|emergency.target           | 紧急 Shell

### 1.6.1. systemd 初始化进程服务
&emsp;&emsp;如果想要将系统默认的运行目标修改为 “多用户，无图形” 模式，可直接用 ln 命令把多用户模式目标文件连接到 /etc/systemd/system/default.target：

```bash 
ln -sf /lib/systemd/system/multi-user.target/etc/systemd/system/default.target 
```

### 1.6.2. System V init 运行级别
&emsp;&emsp;init 命令是 Linux 下的进程初始化工具，init 进程是所有 Linux 进程的父进程，它的进程号为 1。init 命令是 Linux 操作系统中不可缺少的程序之一，init 进程是 Linux 内核引导运行的，是系统中的第一个进程。  
&emsp;&emsp;使用 init 命令很简单。直接输入 `init + 你想要的模式` 回车就行。   
比如输入:   
```bash
init 0  # 就是关机  
init 3  # 就是切换到多用户 - 命令行模式  
init 5  # 就是切换到图形化界面  
init 6  # 就是重启  
```

### 1.6.3. 运行级别
&emsp;&emsp;到底什么是运行级呢？简单的说，运行级就是操作系统当前正在运行的功能级别。这个级别从 0 到 6 ，具有不同的功能。你也可以用 `cat /etc/inittab` 查看它的英文介绍。

-----------------------------------------------------
## 1.7. 用户登录
- __root 用户__（即 UID 为 0 的用户）：   
&emsp;&emsp;一个特殊的管理帐户  
&emsp;&emsp;也被称为超级用户  
&emsp;&emsp;root 已接近完整的系统控制  
&emsp;&emsp;对系统损害几乎有无限的能力  
&emsp;&emsp;除非必要，不要登录为 root  
- __普通（ 非特权 ）用户__：   
&emsp;&emsp;权限有限  
&emsp;&emsp;造成损害的能力比较有限  

-----------------------------------------------------
## 1.8. 什么是 Shell
- Shell 是 Linux 系统的用户界面，提供了用户与内核进行交互操作的一种接口。它接收用户输入的命令并把它送入内核去执行
- Shell 也被称为 LINUX 的命令解释器（command interpreter）
- Shell 是一种高级程序设计语言

<img alt="用户和内核空间" src="https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/whatIsShelll.png" width="350" align=middle />

### 1.8.1. bash shell
- GNU Bourne-Again Shell (bash) 是 GNU 计划中重要的工具软件之一，目前也是 Linux 标准的 shell，与 sh 兼容
- CentOS 默认使用

### 1.8.2. 命令提示符
- 命令提示符：prompt  
```bash
[root@localhost ~]#  
# 管理员  

[lxl@centos7 ~]$
$ 普通用户
```

- 显示提示符格式：`echo $PS1`
- 修改提示符格式：
```bash
# [当前用户的账号名称@主机名的第一个名字 工作目录的最后一层目录名]命令提示符 
PS1='[\u@\h \W]\$ '
# 不停闪烁的提示符样式
PS1="\[\e[1;5;41;33m\][\u@\h \W]\\$ \[\e[0m\]"
# 黄字红底([\e[31;40m])，依次显示24小时格式时间(\t)、当前用户的账号名称(\u)、主机的第一个名字(\h)、完整的当前工作目录名称(\w)、
PS1="\[\e[1;2;41;33m\][\t \u@\h \w]\\$ \[\e[0m\]"
```

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__在 PS1 中设置的参数与含义对照表__  

参数|含义
:---:|:---
\d|可显示出『星期 月 日』的日期格式，如："Mon Feb 2"
\H|完整的主机名。
\h|仅取主机名在第一个小数点之前的名字
\t|显示时间，为 24 小时格式的『HH:MM:SS』
\T|显示时间，为 12 小时格式的『HH:MM:SS』
\A|显示时间，为 24 小时格式的『HH:MM』
\@|显示时间，为 12 小时格式的『am/pm』样式
\u|目前使用者的账号名称，如『root』
\v|BASH 的主版本信息
\w|完整的工作目录名称，由根目录写起的目录名称，但家目录会以 ~ 取代
\W|利用 basename 函数取得工作目录名称，所以仅会列出最后一个目录名
\!|命令历史数
\#|开机后命令历史数
\$|提示字符，如果是 root 时，提示字符为 # ，否则就是 $ 

&emsp;&emsp;在 PS1 中设置字符颜色的格式为：[\e [F;Bm]，其中 “F“为字体颜色，编号为 30-37，“B” 为背景颜色，编号为 40-47。  

&emsp;&emsp;__颜色对照表__

F   |B   |颜色
:---:|:---:|:---:
30|40|黑色
31|41|红色
32|42|绿色
33|43|黄色
34|44|蓝色
35|45|紫红色
36|46|青蓝色
37|47|白色

&emsp;&emsp;这行配置可以写到 `/etc/profile` 下（写完记得 `source /etc/profile` 一下，让配置生效），也可以写到个人用户的环境变量配置文件中。  

### 1.8.3. 命令分类
&emsp;&emsp;在shell中可执行的命令有两类:  
- **内部命令**：由shell自带的，而且通过某命令形式提供
```bash
help          # 内部命令列表
enable CMD    # 启用内部命令
enable –n CMD # 禁用内部命令
enable –n     # 查看所有禁用的内部命令
```
- **外部命令**：在文件系统路径下有对应的可执行程序文件  
查看路径：`which -a |--skip-alias ; whereis`

### 1.8.4. bash 中常用快捷键

快捷键|作用
:---:|:---
Ctrl + L |清屏，相当于 clear 命令。
Ctrl + A |光标移到命令行首，相当于 Home 键。
Ctrl + E |光标移到命令行尾，相当于 End 键。
Ctrl + U |从光标处删除⾄命令行首。
Ctrl + K |从光标处删除⾄命令行尾。
Ctrl + C |终止命令。
Ctrl + W |从光标处删除至词首（往左删除，以空格分隔）。
Ctrl + Y |粘贴 ctrl+U 或 ctrl+K 剪切的内容。
Ctrl + 左方向键 |光标左移一个单词（以空格分隔）。
Ctrl + 右方向键 |光标右移一个单词（以空格分隔）。

-----------------------------------------------------
## 1.9. 必知必会命令
1. 如何查看当前使用的 shell：`echo ${SHELL}`
```bash
[root@CentOS7 ~]# echo ${SHELL}  
/bin/bash
```

2. 如何查看本机所有的 shell：`cat /etc/shells`
```bash
[root@centos7 ~]# cat /etc/shells 
/bin/sh
/bin/bash
/usr/bin/sh
/usr/bin/bash
/bin/tcsh
/bin/csh
```

3. 判断内部还是外部命令：`tpye COMMAND`
```bash
[root@centos7 ~]# type man
man is /bin/man           # 这是一个外部命令
[root@centos7 ~]# type cd
cd is a shell builtin     # 这是一个内部命令
[root@centos7 ~]# type ls
ls is aliased to `ls --color=
`  # 这是一个别名命令
```

4. 查看登陆当前系统的用户：`whoami`
```bash
[root@centos7 ~]# whoami
root
```

5. 查看当前所有系统登录的用户：`who`
```bash
[root@centos7 ~]# who
lxl      pts/0        2019-03-21 14:46 (192.168.20.1)
```

6. 显示系统当前使用登录会话及所做操作：`w`
```bash
[root@centos7 ~]# w
 20:53:48 up  6:08,  2 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
lxl      pts/0    192.168.20.1     14:46    4.00s  0.41s  0.29s sshd: lxl [priv]
```

7. 通过用户名查看用户的 UID、GID：`id`
```bash
[root@centos7 ~]# id root
uid=0 (root) gid=0 (root) groups=0 (root)
```

8. 查看文件的具体存储信息和时间等信息：`stat FILENAME`
```bash
[root@centos7 ~]# stat anaconda-ks.cfg 
  File: ‘anaconda-ks.cfg’
  Size: 1959      	Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d	Inode: 201326658   Links: 1
Access: (0600/-rw-------)  Uid: (0/    root)   Gid: (0/    root)
Context: system_u:object_r:admin_home_t:s0
Access: 2019-03-19 00:58:06.037999203 +0800
Modify: 2019-03-19 00:56:19.553934247 +0800
Change: 2019-03-19 00:56:19.553934247 +0800
 Birth: -
```

9. 长时间执行远程终端窗口，不退出连接的命令（可在会话间自由切换）：`screen`
  - 创建新screen会话：`screen –S [SESSION]`  
  - 加入screen会话：`screen –x [SESSION]`   
  - 退出并关闭screen会话：`exit`  
  - 剥离当前screen会话：`Ctrl+A+D`  
  - 显示所有已经打开的screen会话：`screen -ls`  
  - 恢复某screen会话：`screen -r [SESSION]`  

10. `hexdump`命令一般用来查看“二进制”文件的十六进制编码，但实际上它能查看任何文件，而不只限于二进制文件。  

-----------------------------------------------------
## 1.10. 如何获取帮助
&emsp;&emsp;获取帮助的能力决定了技术的能力！可从以下几个方面获取多层次的帮助：  
- `whatis`  
- `COMMAND --help`  
- `man` 和 `info`  
- 通过本地文档获取帮助：`/usr/share/doc/`  
- 通过在线文档获取帮助  
- 其它网站和搜索

### 1.10.1. 通过本地文档获取帮助
- /usr/share/doc目录
  - 多数安装了的软件包的子目录,包括了这些软件的相关原理说明
  - 常见文档：README INSTALL CHANGES
  - 不适合其它地方的文档的位置
    - 配置文件范例
    - HTML/PDF/PS 格式的文档
    - 授权书详情

### 1.10.2. 通过在线文档获取帮助
- 第三方应用官方文档
  - http://www.nginx.org
  - http://tomcat.apache.org
  - http://httpd.apache.org
  - http://www.python.org
  - https://dev.mysql.com/doc/
- 通过发行版官方的文档光盘或网站可以获得
  - 安装指南、部署指南、虚拟化指南等
  - 红帽知识库和官方在线文档
    - http://kbase.redhat.com
    - http://www.redhat.com/docs
    - http://access.redhat.com

### 1.10.3. 其它网站和搜索
- http://tldp.org
- http://www.slideshare.net
- http://www.google.com
- Openstack filetype:pdf
- rhca site:redhat.com/docs