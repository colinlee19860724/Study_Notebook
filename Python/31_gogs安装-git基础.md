**31 - gogs安装-git基础**

---

[TOC]

---

# 1. Gogs 安装
参考这篇博文:[Gogs 安装](https://github.com/dachenzi/StudyNotes/blob/master/SoftwareDep/gogs% E5% AE%89% E8% A3%85.md)

# 2. Git 介绍
Git 是分布式版本控制系统，** 集中式 VS 分布式(SVN VS Git)**，SVN 和 Git 主要的区别在于历史版本维护的位置，SVN 和 Git 主要的区别在于历史版本维护的位置，这样的好处在于：
1. 自己可以在脱机环境查看开发的版本历史。
2. 多人开发时如果充当中央仓库的 Git 仓库挂了，可以随时创建一个新的中央仓库然后同步就立刻恢复了中央库。

# 3. 使用 Github 仓库

## 3.1. Git 配置
提交代码时，git 使用 username 和 email 标识一个人，所以想要提交需要先配置这两个属性。

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"

```

参数含义：
- global：表示当前的主机上所有的 git 仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和 Email 地址。
- user.name: 名称
- user.email: 邮箱地址  
为单独的项目配置 git 参数，只需要在项目的.git 目录下，执行 git config 命令(去掉 --global 参数即可).

```bash
$ git config user.name 'My name'

```

这种方式的用户名 Email 会存放在.git/config 中，当同时存在.gitconfig 和 config 中时，在项目内进行 git 操作时，config 中的配置优先  
其他配置：  
&emsp;&emsp;忽略 SSL 证书 （在 ssl 证书未经过第三方机构签署）

```bash
$ git config --global http.sslVerify "false"

```

实际上，上面这些命令是修改了～/.gitconfig 这个文件，我们打开这个文件可以看到先前配置的 git 相关参数

## 3.2. 远程仓库
&emsp;&emsp;仓库就是远程存在一个用于存放我们提交的修改的仓库，Github 就是一个公有的对外提供 Git 仓库托管的服务，需要注意的是，仓库内的东西对外都是可见的，所以机密性的东西需要自行处理。  
&emsp;&emsp;使用 Github 首先需要进行注册，这里就不在进行说明。注册完毕后可以在 Github 上创建一个仓库，创建的步骤也不在说明。创建完毕后 github 会提示你有以下两种途径上传你的代码
1. 本地初始化 git 仓库，添加远程仓库，然后提交代码文件
创建一个目录用于充当本地 Git 仓库

```bash
mkdir mygitrepo  && cd mygitrepo
echo "# GitNote" >> README.md
git init
git add README.md  # 模拟代码文件
git commit -m "first commit"
git remote add origin git@github.com:dachenzi/GitNote.git   # 添加远程仓库，远程仓库的名称命名为 origin
git push -u origin master                                   # 提交代码到远程仓库 origin 的 master 分支上

```2. 只是代码提交

```bash
git remote add origin git@github.com:dachenzi/GitNote.git  # 本地已经提交完毕，关联远程仓库
git push -u origin master  # 提交代码到远程仓库

```

PS：仓库提供两种方式接入，HTTPS 和 SSH
- SSH 方式，我们可以生成密钥用于免密码提交
- HTTPS 的方式，提交的时候需要输入用户名密码(可以配置 git 保存密码有效期)，建议使用 ssh 的方式。  
关于使用 - u 选项：  
&emsp;&emsp;如果当前分支与多个主机存在追踪关系，那么这个时候 - u 选项会指定一个默认主机，这样后面就可以不加任何参数使用 git push。上面命令将本地的 master 分支推送到 origin 主机，同时指定 origin 为默认主机，后面就可以不加任何参数使用 git push 了。

```

删除远程仓库：       git remote remove origin (仓库名称)
从远程库克隆：       git clone 仓库地址
查看远程库信息：     git remote -v

```

# 4. Git 基本使用

## 4.1. 创建版本库
&emsp;&emsp;什么是版本库呢，版本库又名仓库(repository)，可以简单的理解为一个目录，这个目录里的文件都会被 git 管理起来，每个文件的修改，删除，git 都可以进行跟踪，以便任何时候可以追踪历史，或者在将来某一个时刻还可以还原。
1. 初始化一个 Git 仓库
创建一个版本库只需要使用 init 进行初始化即可。

```bash
$ mkdir myfirstrepo
$ cd myfirstrepo
$ git init

```

这样就可以把 git 仓库创建好了，并在该目录下产生.git 目录，用于存放 git 相关的用于跟踪的相关信息，千万不要乱修改，否则可能把 git 仓库给破坏了。
2. 添加文件到 Git 仓库
包括两步：

```bash
$ git add <file>
$ git commit -m "description"

```

git add 可以反复多次使用，添加多个文件，git commit 可以一次提交很多文件，-m 后面输入的是本次提交的说明，可以输入任意内容。

## 4.2. 查看工作区状态

```bash
$ git status

```1. 当我们在仓库中新建文件，但是没有 add 时，执行后会有如下提示

```bash
# Untracked files:
# (use "git add <file>..." to include in what will be committed)
#
#   readme.txt

```2. 这时，当我们 使用 add 命令添加后

```bash
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
#   new file: readme.txt

```

表示本次新增了新文件 readme.txt
3. 当我们修改 readme.txt 文件时，git 会告诉我们这个文件被修改了。

```bash
# Changes to be committed:
# (use "git rm --cached <file>..." to unstage)
#
#   modified: readme.txt

```但是不会告诉我们哪里被修改了，这时可以使用 diff 命令来查看详细的修改内容

```bash
diff --git a/readme.txt b/readme.txt
index 860d0e4..e757091 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1 +1 @@
-Hello World 2018
+HEllO World    # 第一行由 Hello World 2018 变为了 HELLO World

```

## 4.3. 查看修改内容

```bash
$ git diff file           # 是工作区(work dict) 和暂存区(stage) 的比较  （工作区的文件和 add 后的文件）
$ git diff --cached file  # 是暂存区(stage) 和分支(master) 的比较  （add 后的文件和 commit 后的文件）
$ git diff HEAD -- file   # 是工作区和分支的比较

```

## 4.4. 查看提交日志
&emsp;&emsp;当我们不断的对文件进行修改，然后不断的提交到版本库里，就好比玩游戏，每通过一关就会把当前的关卡保存，如果某一关没过去，那么还可以读取前一关的状态，继续开始。Git 也一样，每当你修改文件到一定程度，就可以保存一个快照，这个快照在 Git 中成为 commit，一旦把文件改乱，或者误删除，还可以从最近一个 commit 进行恢复。  
&emsp;&emsp;我们不可能知道所有自己每次提交的时间及内容，那么 git 提供了 log 命令用于查询这些提交的信息

```bash[root@localhost repo]# git log
commit 7521d7483dd263a6302168744a69ae8e3d7f11be
Author: daxin <daxin.li@foxmail.com>
Date: Sat May 19 17:47:50 2018 +0800
 
test2
 
commit e0b08fa7b70251f14cf5d6472260ba8145f105c1
Author: daxin <daxin.li@foxmail.com>
Date: Sat May 19 17:45:22 2018 +0800
 
test1
 
commit e449c011faf28c40398c59ace8c3017bd7fbd572
Author: daxin <daxin.li@foxmail.com>
Date: Sat May 19 17:43:25 2018 +0800
 
Hello World

```简化输出：

```bash
$ git log --pretty=oneline

```PS： log 还有一个常用的参数 - 1，表示显示最后一次提交。

```bash[root@daxin-vpn myfirstrepo]# git log -1
commit f1a9599b26ea4e2c44ba06497474e07c2c62781e
Author: dachenzi <daxin.li@foxmail.com>
Date:   Wed May 23 17:31:42 2018 +0800
 
    ignore files

```

## 4.5. 查看命令历史

```bash
$ git reflog

```例子：通过历史，可以确定 commit id，那么有了 commit id 就可以进行回退了

```bash
7521d74 HEAD@{0}: reset: moving to 7521d
e449c01 HEAD@{1}: reset: moving to HEAD^
e0b08fa HEAD@{2}: reset: moving to HEAD^
7521d74 HEAD@{3}: commit: test
e0b08fa HEAD@{4}: commit: test
e449c01 HEAD@{5}: commit(initial): Hello World

```

## 4.6. 版本回退

```bash
$ git reset --hard commit_id

```

commit_id 是版本号，是一个用 SHA1 计算出的序列，唯一标识某一次的提交，在 Git 中，还有一些特殊的标签，比如用 HEAD 表示当前版本，上一个版本就是 HEAD^，上上一个版本是 HEAD^^，往上 100 个版本写成 HEAD~100。根据 log 得到的 commit id，那么我们就可以自用穿越了。

# 5. 工作区、暂存区和版本库
Git 的本地版本库中存了很多东西，其中最重要的就是称为 stage（或者称为 index）的 `暂存区`，还有 Git 自动创建的 master，以及指向 master 的指针 HEAD。
- 工作区：一个 git 项目的根目录(仓库的主目录，我们之前执行 git init 的目录) 就是一个工作区；  
- 版本库：在工作区有一个隐藏目录.git，是 Git 的版本库。  
它们的关系如下图：  
![gitrepo](../Photo/gitrepo.png)  
还记得我们提交文件时的两步吗？
- git add 添加文件，实际上就是把文件修改添加到暂存区
- git commit 提交修改，实际上就是把暂存区的所有内容提交到当前分支

# 6. Git 高级

## 6.1. 撤销修改
当我们在工作区中修改了某些文件以后，发现修改错误，想要恢复成没有修改之前的样子，那么我们可以使用 Git 来进行撤销修改

### 6.1.1. 丢弃工作区的修改

```bash
$ git checkout -- <file>

```

该命令是指将文件在工作区的修改全部撤销，这里有两种情况：
- 一种是 file 自修改后还没有被放到暂存区(没有 add)，现在，撤销修改就回到和版本库一模一样的状态；
- 一种是 file 已经添加到暂存区后(add 以后)，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。  
总之，就是让这个文件回到最近一次 git commit 或 git add 时的状态。

### 6.1.2. 丢弃暂存区的修改
主要分两步： 
1. 第一步，把暂存区的修改撤销掉(unstage)，重新放回工作区：

```bash
$ git reset HEAD <file>     # 不加文件名，那么可以回滚所有暂存区的文件

```2. 第二步，撤销工作区的修改

```bash
$ git checkout -- <file>　  # * 表示通配符，表示回滚所有修改过后的文件

```

小结：
1. 当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令 git checkout -- <file>。
2. 当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令 git reset HEAD <file>，就回到了第一步，第二步按第一步操作。
3. 已经提交了不合适的修改到版本库时，想要撤销本次提交，进行版本回退，前提是没有推送到远程库。

## 6.2. 删除文件
一般情况下，我们删除文件 可以 简单的使用 rm filename 删除，但是这个时候 Git 知道我们删除了文件，因此工作区和版本库就不一致了，再使用 git status 命令时，会立刻告诉你哪些文件被删除了。
1. 如果真的要删除文件，那么需要使用 git rm file 来提交删除动作到暂存区，然后使用 git commit 进行提交

```bash
$ rm <files>
$ git rm <files>
$ git commit -m 'message'

# git rm <files> 包含了 rm 的动作，所以不用再执行

```2. 如果是误删，但是这时版本库中还存在，所以我们可以使用如下命令恢复文件

```bash
$ git checkout -- <file>

```3. 如果错误使用了 git rm file 删除文件，先撤销暂存区修改，重新放回工作区，然后再从版本库写回到工作区

```bash
$ git reset head <file>
$ git checkout -- <file>

```所以只要文件存在版本库中，工作区无论是修改还是删除，都可以" 一键还原 "。

## 6.3. 分支
&emsp;&emsp;当我们需要开发一个新的功能或者修改 bug，又不想直接修改 master 分支的代码，那么就需要新开一个分支，我们在新开的分支内的操作不会影响其他分支的内容，其他的版本控制系统都有分支的概念，Git 与它们不同的是，在 1 秒钟之内就能完成创建、切换和删除分支，无论是 1 个文件或者是 1 万个文件。

### 6.3.1. 创建及切换分支
&emsp;&emsp;前面我们已经知道，每次提交，git 都会把他们连成一个时间线，这条时间线就是一个分支，截至到目前，只有 1 条时间线，在 Git 里，这个分支叫做主分支，即 master 分支，HEAD 严格来说不是指向指向提交，而是指向 master，master 才是指向提交的，再用 HEAD 指向 master，就能确定当前分支，以及当前分支的提交点，当我们创建新的分支 dev 时，Git 新建了一个指针 dev，指向 master 相同的提交，再把 HEAD 指向 dev，就表示当前分支在 dev 上。（Git 创建一个分支很快，因为除了增加一个 dev 指针，改改 HEAD 指向，工作区和文件都没有任何变化。新建了 dev 分支后，后面的提交 master 指针将不会在改变，而 dev 指针会随着提交，其时间线会依次向后。如果我们在 dev 分支上的任务完成，就可以把 dev 合并到 master 上，Git 怎么合并呢？最简单的方法是直接把 master 指向 dev 的当前提交，就完成了合并，所以 Git 合并分支也就很快，就改改指针，工作区内容也不变，就算要删除 dev 分支也很方便，只需要删除指向 dev 的指针即可，这样我们就只剩下 master 一个分支

```bash
# 创建分支
$ git branch <branchname>
 
# 查看分支
$ git branch    # git branch 命令会列出所有分支，当前分支前面会标一个 * 号。
 
# 切换分支
$ git checkout <branchname>
 
# 创建 + 切换分支
$ git checkout -b <branchname>   × 常用

```

### 6.3.2. 合并分支及删除分支

```bash
$ git merge <branchname>       # 用于合并指定分支到当前分支。
$ git branch -d <branchname>   # -d 表示 delete

```在做合并的时候常常会出现，比如在创建 dev 分支后，又对 master 分支的文件进行了修改，如果改动的地方相同，那么在合并的时候会有冲突提示，这个时候我们需要手动解决冲突之后才能合并。

```bash[root@localhost repo]# git merge dev             # 在 master 分支上合并 dev 分支
Auto-merging readme.txt
CONFLICT(content): Merge conflict in readme.txt # 提示我们 readme.txt 文件在合并的时候产生冲突
Automatic merge failed; fix conflicts and then commit the result.

```

必须手动解决分支以后再进行提交(git status 也可以告诉我们冲突的文件)。  
Git 会在冲突的文件中标注出那些部分冲突，必须手动的修改需要保存的文件内容，解决冲突

```bash[root@localhost repo]# cat readme.txt
Hello world My name is Dahl.
Come on from China
<<<<<<< HEAD 　　　　# 当前分支名
like master - 1 　　# 内容
=======
like dev - 1 　　　　# 内容

> >>>>>> dev    　　# 合并的分支名  

```冲突解决完毕后

```bash
$ git add readme.txt
$ git commit -m 'conflict fixed'

```使用带参数的 git log 也可以看到分支合并的情况

```bash
$ git log --graph --pretty=oneline --abbrev-commit

```

最后再删除分支，即可。  
所以：当 Git 无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并。完成用 git log --graph 命令可以看到分支合并图。

### 6.3.3. 普通模式合并分支
&emsp;&emsp;通常，合并分支时，如果可能，Git 会用 Fast Forward 模式，但这种模式下，删除分支后，会丢掉分支信息，如果要强制禁用 Fast Forward 模式，Git 就会在 merge 时生成一个新的 commit，这样从分支历史上就可以看出分支信息，即在进行 merge 的时候使用 --no-ff 来表示禁用 Fast Forward

```bash
$ git merge --no-ff -m "description" <branchname>

```

### 6.3.4. 切换工作区
&emsp;&emsp;在软件开发的过程中，难免会有各种各样的 bug，在使用 Git 作为版本控制的环境内，一般用分支来进行 bug 修复，修复后，合并分支，然后临时分支删除。  
&emsp;&emsp;当遇到线上紧急 bug 修复时，那么就需要紧急修复，而此时手头的任务还没有完成，还没办法提交，所以这里 Git 提供了一个 stash 功能，可以把你目前的工作现场给存档，等到方便的时候再回来处理。

```bash
# 保存工作现场
$ git stash
 
# 查看工作现场
$ git stash list
 
# 恢复工作现场
$ git stash pop
 
# 丢弃一个没有合并过的分支
$ git branch -D <branchname>

```

### 6.3.5. 抓取分支
&emsp;&emsp;多人协作时，大家都会往 master 和 dev 分支上推送各自的修改。当我们从远程仓库 clone 时，默认情况下只能看到本地的 master 分支，如果想要从 dev 分支开始开发，那么需要在本地创建 dev 分支，然后对应到远程仓库的 dev 分支上

```bash
$ git checkout -b dev origin/dev

```

本地和远程分支的名称最好一致.  
因为大家都是从 dev 分支上开发新功能的，后来的人在推送本地代码的时候，由于远程仓库中的代码已经改变，所以会提示冲突

```bash[root@localhost repo]# git push origin dev
To git@github.com:dachenzi/GitNote.git
! [rejected] dev -> dev(fetch first)
error: failed to push some refs to 'git@github.com:dachenzi/GitNote.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first merge the remote changes(e.g.,
hint: 'git pull') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```出现这种情况时，很简单，Git 也提示我们了，需要先执行 git pull 把最新的提交从 origin/dev 抓下来，然后在本地合并解决冲突后，再推送

```bash[root@localhost repo]# git pull    # 包含：从远程仓库中拉取最新代码，并和本地进行合并，两个动作。
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details
 
    git pull <remote> <branch>
 
If you wish to set tracking information for this branch you can do so with:
 
    git branch --set-upstream-to=origin/<branch> dev

```出现这种情况，表示没有指定本地 dev 分支与远程 origin/dev 分支的链接，根据提示，设置 dev 和 origin/dev 的链接：

```bash[root@localhost repo]# git branch --set-upstream-to=origin/dev dev
Branch dev set up to track remote branch dev from origin.

```

由于 pull 会进行代码合并，所以如果冲突，那么还需要解决冲突后提交(请参照上面解决冲突部分)，然后再推送到远程仓库即可。

## 6.4. 标签
&emsp;&emsp;相当于 IP 和域名的映射，Commit id 是一串很长的数字，不是那么容易记忆，这时如果能在提交时，对当前版本打上一个 tag:v1.0，那么以后我就只需要说到 V.10 就好了。

### 6.4.1. 新建一个标签

```bash
$ git tag <tagname>  <commit-id>    # 不加 commit-d 时，默认为 HEAD

```如果不加 commit-id，默认为 HEAD，那么就会为当前分支的 HEAD 打上标签

```bash
# 针对某个 commit id 打标签

# 1、查看历史提交信息
$ git log --pretty=oneline --abbrev-commit  
# 2、针对 commit id 打标签
$ git tag v1.1 f52c633  
# 3、查看标签对应的信息
$ git show v1.0  
# 4、创建带有说明的标签， -a 表示标签名， -m 表示说明性的文字
$ git tag -a 'v1.1' -m 'Version 1.0' f52c633

```

### 6.4.2. 查看及推送标签

```bash
# 查看标签 
$ git tag

```不是按照时间来排序的，想要看详细的内容，可以使用 git show

```bash
$ git show v1.0

```

### 6.4.3. 推送本地标签
默认状态下标签是不会进行推送的，如果想要推送某个标签到远程仓库

```bash
$ git push origin <tagname>

```推送所有标签到远程仓库

```bash
$ git push origin --tags

```

### 6.4.4. 删除标签
删除本地标签

```bash
$ git push origin --tags

```删除一个远程标签

```bash
$ git push origin :refs/tags/<tagname>

```

## 6.5. 自定义 Git　
Git 除了上面所说的那些配置项以外还有很多可配置的，比如让 Git 显示颜色

```bash
git config --global color.ui true

```

这样配置以后文件名就会被标上颜色

### 6.5.1. 忽略特殊文件名
&emsp;&emsp;有些时候某些文件必须存放在工作区内，举个例子，比如 java 编译后的 class 文件，python 的 pyc 文件，这些文件在上传远程服务器时都是不需要的，那么如何忽略某些文件呢？  
&emsp;&emsp;在 Git 工作区的根目录下创建一个特殊的.gitignore 文件，然后把要忽略的文件名填进去，Git 就会自动忽略这些文件。

```bash[root@daxin-vpn myfirstrepo]# cat .gitignore
# Linux:
readme.txt2[root@daxin-vpn myfirstrepo]#

```提交的时候就不会检查 readme.txt2 文件了，如果我们要强制提交 readme.txt2，需要使用 - f 参数（强制添加）

```bash
$ git add -f readme.txt2

```或者你想确认下，自己的文件是否被.gitignore 过滤掉

```bash
git check-ignore -v readme.txt2

```

更多的过滤列表可以参考：https://github.com/github/gitignore

### 6.5.2. 配置别名
&emsp;&emsp;向 checkout，status 这种常用的命令，一来单词比较长，二来还容易打错，所以如果用 co 表示 checkout，用 st 表示 status 就好了，Git 给我们提供了命令别名的方式。

```bash
$ git config --global alias.st status
$ git config --global alias.co checkout

```而对于回滚文件的 git reset HEAD file 可以有如下简写

```bash
$ git config --global alias.unchange "reset HEAD"
$ git unchange readme.txt
# 实际上执行的就是 git reset HEAD readme.txt

```还有人把 lg 配置成（自己可以尝试一下，真的是好看的一比啊，哈哈。）
```

git config --global alias.lg "log --color --graph --pretty=format:'% Cred% h% Creset -% C(yellow)% d% Creset % s % Cgreen(% cr) % C(bold blue)<% an>% Creset' --abbrev-commit"

```

&emsp;&emsp;由于 config 是保存在 git 的用户相关配置文件中的，所以如果想要删除某些 alias，可以进入在.gitconfig 或者.git/config 下删除 alias 部分的设定，具体在那个文件，取决与你是否使用了 --global 等参数。