# Linux入门

## Linux发行版
* __slackware__：SUSE Linux Enterprise Server (SLES)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;OpenSuse桌面  
* __debian__：ubuntu，mint  
* __RedHat__：RHEL: RedHat Enterprise Linux&emsp;每18个月发行一个新版本  
&emsp;&emsp;&emsp;&emsp;&emsp;CentOS：兼容RHEL的格式  
&emsp;&emsp;&emsp;&emsp;&emsp;中标麒麟：中标软件  
&emsp;&emsp;&emsp;&emsp;&emsp;Fedora：每6个月发行一个新版本  
* __ArchLinux__：轻量简洁  
* __Gentoo__：极致性能，不提供传统意义的安装程序  
* __LFS__：Linux From scratch 自制Linux  
* __Android__：kernel+busybox（工具集）+java虚拟机  
* __Linux分支参考网站__：[http://futurist.se/gldt/](http://futurist.se/gldt/)  

## 如何获取帮助
&emsp;&emsp;获取帮助的能力决定了技术的能力！可从以下几个方面获取多层次的帮助：  
* whatis  
* command --help  
* man and info  
* /usr/share/doc/  
* Red Hat documentation  
* 其它网站和搜索  


## systemd初始化进程
&emsp;&emsp;Linux操作系统的开机过程是这样的，即从BIOS开始，然后进入Boot Loader，再加载系统内核，然后内核进行初始化，最后启动初始化进程。初始化进程作为Linux系统的第一个进程，它需要完成Linux系统中相关的初始化工作，为用户提供合适的工作环境。红帽RHEL 7系统已经替换掉了熟悉的初始化进程服务System V init，正式采用全新的systemd初始化进程服务。systemd初始化进程服务采用了并发启动机制，开机速度得到了不小的提升。  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**systemd与System V init的区别以及作用**

System V init运行级别|systemd目标名称  |作用
:------------------:|:---------------|:-----
0|runlevel0.target, poweroff.target  |关机
1|runlevel1.target, rescue.target    |单用户模式
2|runlevel2.target, multi-user.target|等同于级别3
3|runlevel3.target, multi-user.target|多用户的文本界面
4|runlevel4.target, multi-user.target|等同于级别3
5|runlevel5.target, graphical.target |多用户的图形界面
6|runlevel6.target, reboot.target    |重启
emergency|emergency.target           |紧急Shell

### systemd初始化进程服务
&emsp;&emsp;如果想要将系统默认的运行目标修改为“多用户，无图形”模式，可直接用ln命令把多用户模式目标文件连接到/etc/systemd/system/目录：

```bash 
[root@centos7 ~]# ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target 
```

### System V init运行级别
&emsp;&emsp;init命令是Linux下的进程初始化工具，init进程是所有Linux进程的父进程，它的进程号为1。init命令是Linux操作系统中不可缺少的程序之一，init进程是Linux内核引导运行的，是系统中的第一个进程。  
&emsp;&emsp;使用init命令很简单。直接输入 `init + 你想要的模式` 回车就行。   
比如输入:   
`init 0` 就是关机  
`init 3` 就是切换到多用户-命令行模式  
`init 5` 就是切换到图形化界面  
`init 6` 就是重启  

### 运行级别

&emsp;&emsp;到底什么是运行级呢？简单的说，运行级就是操作系统当前正在运行的功能级别。这个级别从0到6 ，具有不同的功能。你也可以在/etc/inittab中查看它的英文介绍。

## 必知必会的命令
1. 如何查看当前使用的shell:
```bash
[root@CentOS7 ~]# echo ${SHELL}  
/bin/bash
```

2. 如何查看本机所有的shell：`cat /etc/shells`  
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
man is /bin/man  # 这是一个外部命令
[root@centos7 ~]# type ls
ls is aliased to `ls --color=auto`  # 这是一个别名命令
[root@centos7 ~]# type cd
cd is a shell builtin  #这是一个内部命令
```
4. 查看登陆当前系统的用户：`whoami`
```bash
[root@centos7 ~]# whoami
root
```

5. 查看当前所有系统登录的⽤户：`who`
```bash
[root@centos7 ~]# who
lxl      pts/0        2019-03-21 14:46 (192.168.20.1)
```

6. 显⽰系统当前使⽤登录会话及所做操作：`w`
```bash
[root@centos7 ~]# w
 20:53:48 up  6:08,  2 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
lxl      pts/0    192.168.20.1     14:46    4.00s  0.41s  0.29s sshd: lxl [priv]
```
