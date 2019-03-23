[TOC]

# Linux 入门

## 开源 Open Source
* __软件分类__：  
  1. 商业  
  2. 共享  
  3. 自由 free  

* __开源__： 把软件程序与源代码文件一起打包提供给用户，让用户在不受限制地使用某个软件功能的基础上还可以按需进行修改，或编制成衍生产品再发布出去。用户具有使用自由、修改自由、重新发布自由以及创建衍生品的自由。开源软件最重要的特性有下面这些。  
  1. __低风险__：使用闭源软件无疑把命运交付给他人，一旦封闭的源代码没有人来维护，你将进退维谷；而且相较于商业软件公司，开源社区很少存在倒闭的问题。  
  2. __高品质__：相较于闭源软件产品，开源项目通常是由开源社区来研发及维护的，参与编写、维护、测试的用户量众多，一般的bug还没有等爆发就已经被修补。
  3. __低成本__：开源工作者都是在幕后默默且无偿地付出劳动成果，为美好的世界贡献一份力量，因此使用开源社区推动的软件项目可以节省大量的人力、物力和财力。
  4. __更透明__：没有哪个笨蛋会把木马、后门等放到开放的源代码中，这样无疑是把自己的罪行暴露在阳光之下。  
  
&emsp;&emsp; 世界上的开源许可证，大概有上百种，常用的有 6 个，下面一图读懂主要的开源协议：  

<img alt="一图读懂主要的开源协议" src="https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/一图读懂主要的开源协议.png" width="700" align=middle />

---
## Linux 哲学思想
* 一切皆文件（包括硬件）
* 小型，单一用途的程序
* 链接程序，共同完成复杂的任务
* 避免令人困惑的用户界面
* 配置数据存储在文本中

---
## 开发接口标准
* __ABI: Application Binary Interface__  
&emsp;&emsp;ABI 描述了应用程序与 OS 之间的底层接口，允许编译好的目标代码在使用兼容 ABI 的系统中无需改动就能运行  
* __API：Application Programming Interface__  
&emsp;&emsp;API 定义了源代码和库之间的接口，因此同样的源代码可以在支持这个 API 的任何系统中编译  
* __POSIX: Portable Operating System Interface__  
&emsp;&emsp;IEEE 在操作系统上定义的一系列 API 标准  
&emsp;&emsp;POSIX 兼容的程序可在其它 POSIXX 操作系统编译执行  
* __运行程序格式：__  
&emsp;&emsp;Windows: EXE, .dll (dynamic link library), .lib  
&emsp;&emsp;Linux: ELF, .so (shared object), .a  

---
## 用户和内核空间
* __用户空间：User space__  
&emsp;&emsp; 用户程序的运行空间。为了安全，它们是隔离的，即使用户的程序崩溃，内核也不受影响，只能执行简单的运算，不能直接调用系统资源，必须通过系统接口（ system call），才能向内核发出指令。  
* __内核空间：Kernel space__  
&emsp;&emsp; 是 Linux 内核的运行空间，可以执行任意命令，调用系统的一切资源。  

<img alt="用户和内核空间" src="https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/用户和内核空间.png" width="500" align=middle />

示例：
```c
str = "www.magedu.com" // 用户空间
x = x + 100            // 用户空间
y = x + 200            // 切换回用户空间
```
&emsp;&emsp; 第一行和第二行都是简单的赋值运算，在 User space 执行。第三行需要写入文件，就要切换到 Kernel space ，因为用户不能直接写文件，必须通过内核安排。第四行又是赋值运算，就切换回 User space 。  

---
## Linux 版本
### 内核版本
&emsp;&emsp; 查看内核 (kernel) 版本命令：`uname -r` 或 `cat /proc/version`  
&emsp;&emsp;linux 内核版本有两种：__稳定版__（次版本为偶数）和 __开发版__（次版本为奇数）。  
&emsp;&emsp; 版本号：__主版本。次版本。释出版本 - 修改版本__  
&emsp;&emsp; 如：__3.10.0-957.el7.x86_64__  
> __注：__  
> __主版本、次版本__：一般用头两个数字描述内核系列，主版本号和次版本号标志着重要的功能变动  
> __释出版本__：在主次版本架构不变的情况下，新增的功能累积到一定程度后释出的内核版本  
> __修改版本__：表示较小的功能变更，修改一些 bug 等  
> __el__ 表示 Enterprise Linux，7 表示 Centos7  
> __x86_64__ 表示 CPU 结构，即 64 位  

&emsp;&emsp;Linux 内核版本发布网站（The Linux Kernel Archives）：[https://www.kernel.org/](https://www.kernel.org/)

### 发行版本
&emsp;&emsp; 查看 RedHat 系列发行（distribution）版本命令：`cat /etc/redhat-release`  
&emsp;&emsp;Linux 发行版的名称和版本号是由发行版的维护者决定的  
&emsp;&emsp; 主要的 Linux 发行版如下：  

* __slackware__：SUSE Linux Enterprise Server (SLES)  
&emsp;&emsp;&emsp;&emsp;&emsp;OpenSuse 桌面  
* __debian__：ubuntu，mint  
* __RedHat__：RHEL: RedHat Enterprise Linux&emsp; 每 18 个月发行一个新版本  
&emsp;&emsp;&emsp;&emsp;CentOS：兼容 RHEL 的格式，国内下载源  
&emsp;&emsp;&emsp;&emsp; 中标麒麟：中标软件  
&emsp;&emsp;&emsp;&emsp;Fedora：每 6 个月发行一个新版本  
* __ArchLinux__：轻量简洁  
* __Gentoo__：极致性能，不提供传统意义的安装程序  
* __LFS__：Linux From scratch 自制 Linux  
* __Android__：kernel+busybox（工具集）+java 虚拟机  
* __Linux 分支参考网站__：[http://futurist.se/gldt/](http://futurist.se/gldt/)  
* __阿里巴巴开源镜像站__：[https://opsx.alibaba.com/mirror](https://opsx.alibaba.com/mirror)
* __网易开源镜像站__：[http://mirrors.163.com/](http://mirrors.163.com/)

---
## systemd 初始化进程
&emsp;&emsp;Linux 操作系统的开机过程是这样的，即从 BIOS 开始，然后进入 Boot Loader，再加载系统内核，然后内核进行初始化，最后启动初始化进程。初始化进程作为 Linux 系统的第一个进程，它需要完成 Linux 系统中相关的初始化工作，为用户提供合适的工作环境。红帽 RHEL 7 系统已经替换掉了熟悉的初始化进程服务 System V init，正式采用全新的 systemd 初始化进程服务。systemd 初始化进程服务采用了并发启动机制，开机速度得到了不小的提升。  
 
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**systemd 与 System V init 的区别以及作用 **

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

### systemd 初始化进程服务
&emsp;&emsp; 如果想要将系统默认的运行目标修改为 “多用户，无图形” 模式，可直接用 ln 命令把多用户模式目标文件连接到 /etc/systemd/system/default.target：

```bash 
ln -sf /lib/systemd/system/multi-user.target/etc/systemd/system/default.target 
```

### System V init 运行级别
&emsp;&emsp;init 命令是 Linux 下的进程初始化工具，init 进程是所有 Linux 进程的父进程，它的进程号为 1。init 命令是 Linux 操作系统中不可缺少的程序之一，init 进程是 Linux 内核引导运行的，是系统中的第一个进程。  
&emsp;&emsp; 使用 init 命令很简单。直接输入 `init + 你想要的模式` 回车就行。   
比如输入:   
&emsp;&emsp;`init 0` 就是关机  
&emsp;&emsp;`init 3` 就是切换到多用户 - 命令行模式  
&emsp;&emsp;`init 5` 就是切换到图形化界面  
&emsp;&emsp;`init 6` 就是重启  

### 运行级别
&emsp;&emsp; 到底什么是运行级呢？简单的说，运行级就是操作系统当前正在运行的功能级别。这个级别从 0 到 6 ，具有不同的功能。你也可以用 `cat /etc/inittab` 查看它的英文介绍。

---
## 用户登录
* __root 用户__（即 UID 为 0 的用户）：   
&emsp;&emsp; 一个特殊的管理帐户  
&emsp;&emsp; 也被称为超级用户  
&emsp;&emsp;root 已接近完整的系统控制  
&emsp;&emsp; 对系统损害几乎有无限的能力  
&emsp;&emsp; 除非必要，不要登录为 root  
* __普通（ 非特权 ）用户__：   
&emsp;&emsp; 权限有限  
&emsp;&emsp; 造成损害的能力比较有限  

---
## 简单命令
1. 如何查看当前使用的 shell：`echo ${SHELL}`
```bash
[root@CentOS7 ~]# echo ${SHELL}  
/bin/bash
```2. 如何查看本机所有的 shell：`cat /etc/shells````bash
[root@centos7 ~]# cat /etc/shells 
/bin/sh
/bin/bash
/usr/bin/sh
/usr/bin/bash
/bin/tcsh
/bin/csh
```3. 判断内部还是外部命令：`tpye COMMAND````bash
[root@centos7 ~]# type man
man is /bin/man                     # 这是一个外部命令
[root@centos7 ~]# type ls
ls is aliased to `ls --color=auto`  # 这是一个别名命令
[root@centos7 ~]# type cd
cd is a shell builtin               # 这是一个内部命令
```4. 查看登陆当前系统的用户：`whoami````bash
[root@centos7 ~]# whoami
root
```5. 查看当前所有系统登录的？户：`who````bash
[root@centos7 ~]# who
lxl      pts/0        2019-03-21 14:46 (192.168.20.1)
```6. 显？系统当前使？登录会话及所做操作：`w````bash
[root@centos7 ~]# w
 20:53:48 up  6:08,  2 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
lxl      pts/0    192.168.20.1     14:46    4.00s  0.41s  0.29s sshd: lxl [priv]
```7. 通过用户名查看用户的 UID、GID：`id````bash
[root@centos7 ~]# id root
uid=0 (root) gid=0 (root) groups=0 (root)
```8. 查看文件的具体存储信息和时间等信息：`stat FILENAME````bash
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
```8.`hexdump - display file contents in ascii, decimal, hexadecimal, or octal`


---
## 如何获取帮助
&emsp;&emsp; 获取帮助的能力决定了技术的能力！可从以下几个方面获取多层次的帮助：  
* `whatis`  
* `COMMAND --help`  
* `man` 和 `info`  
* `/usr/share/doc/`  
* Red Hat documentation  
* 其它网站和搜索