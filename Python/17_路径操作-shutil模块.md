**17 - 路径操作-shutil模块**

---

[TOC]

---

# 1. 路径操作
&emsp;&emsp;使用 Python 操作文件系统时，少不了会对路径进行切换，对目录的遍历，以及获取文件的绝对路径的一系列的操作，Python 内置了相关的模块完成对应的功能，其中:
- 3.4 以前使用 os.path 模块
- 3.4 开始使用 pathlib 模块

## 1.1. os.path 模块
&emsp;&emsp;os.path 是 os 模块中的一个比较重要的用来拼接、判断路径的主要方法，它主要有如下方法：

```python
os.path.abspath('dir/file')    获取 dir/file 的绝对路径
os.path.split('path')          把路径分割为目录和文件名组成的元组格式，不管 path 是否存在
os.dirname('path')             获取文件的父目录名称，不管 path 是否存在
os.basename('path')            获取文件的名称，不管 path 是否存在
os.path.exists('path')         判断 path 是否存在，return bool
os.path.isabs('path')          判断 path 是否是从根开始，return bool
os.path.isfile('path')         判断 path 是否是一个文件
os.path.isdir('path')          判断 path 是否是一个目录
os.path.join ('path1','path2','path3')：把 path1 和 path2 及 path3 进行组合，但如果 path2 中包含了根路径，那么就会舍弃 path1, 从 path2 开始组合
os.path.getatime('path')       获取文件的 atime 时间，返回时间戳
os.path.getmtime('path')       获取文件的 mtime 时间，返回时间戳
os.path.getsize(filename)      获取文件的大小，单位是字节

```

> Linux 下：从 / 开始，Windows 下从 C,D,E 盘开始

```python
In : import os  
In : os.path.join ('/etc','sysconfig','network-scripts')  
Out: '/etc/sysconfig/network-scripts'

In : os.path.join ('/etc','/sysconfig','network-scripts')  
Out: '/sysconfig/network-scripts'

In : p = os.path.join ('/etc','sysconfig','network-scripts')  
In : p  
Out: '/etc/sysconfig/network-scripts'

In : type(p)  
Out: str

In : os.path.exists(p)  
Out: True

In : os.path.split(p)  
Out: ('/etc/sysconfig', 'network-scripts')

In : os.path.abspath('.')  
Out: '/home/python/py368'

In : os.path.dirname(p)  
Out: '/etc/sysconfig'

In : os.path.basename(p)  
Out: 'network-scripts'

> >> os.path.splitdrive('c:/etc/sysconfig/network-script')   # windows   

('c:', '/etc/sysconfig/network-script')

```

> \_\_file\_\_：变量比较特殊，存放的是当前的 Python 文件的名称，我们可以使用 os.path.abspath(__file__) 来获取当前 python 文件的绝对路径，然后进行打包或者进行相对调用。  

## 1.2. pathlib 模块
&emsp;&emsp;3.4 以后建议使用 pathlib 模块，它提供 Path 对象来对路径进行操作，还包括了目录和文件。

> 在使用时需要实现导入： from pathlib import Path  

### 1.2.1. 目录操作
下面来说一下日常的目录相关操作

#### 1.2.1.1. 初始化(一个路径对象)
通过构建一个 Path 对象来对路径进行初始化

```python
In : from pathlib import Path
In : p = Path()  # 当前目录
In : p1 = Path('a','b','c')   # 当前目录下的 a/b/c
In : p2 = Path('/etc','sysconfig','network-scripts')  # /etc/sysconfig/network-scripts

In : p
Out: PosixPath('.')

In : p1
Out: PosixPath('a/b/c')

In : p2
Out: PosixPath('/etc/sysconfig/network-scripts')

```

#### 1.2.1.2. 路径拼接和分解`/`: Path 对象支持使用`/` 来进行路径的拼接，拼接规则应遵循：

- `Path 对象 / Path 对象`
- `Path 对象 / 字符串` 或者 `字符串 / Path 对象`

```python
In : p2 / 'ifcfg-eth0'
Out: PosixPath('/etc/sysconfig/network-scripts/ifcfg-eth0')

In : p2 /p1  
Out: PosixPath('/etc/sysconfig/network-scripts/a/b/c')

In : '/root' /p2
Out: PosixPath('/etc/sysconfig/network-scripts')

```

需要注意的是：
1. 拼接对象中，至少有一个是 `Path 对象`，拼接的顺序和路径的顺序是一致的
1. p1 是相对路径，而 p2 是从根开始，如果 p1/p2 那么返回的将会是 p2
2. 如果当 `字符串 / Path 对象` 这种格式时，如果 `Path 对象`  是一个绝对路径，那么将无法进行拼接  
`parts 属性`: 将 Path 对象按照当前操作系统的分隔符进行分割返回一个元组

```python
In : p2.parts
Out: ('/', 'etc', 'sysconfig', 'network-scripts')
`

```joinpath(*other)`: 在 Path 对象中使用当前操作系统的路径分隔符分割并追加多个字符串。 

```python
In : p2.joinpath('/etc')
Out: PosixPath('/etc')

In : p2.joinpath('etc')
Out: PosixPath('/etc/sysconfig/network-scripts/etc')

In : p2.joinpath('/etc','/proc')
Out: PosixPath('/proc')

```

需要注意的是：
1. 如果添加的的路径都为  `/` 开始，那么最后添加的路径将会覆盖前面所有添加的路径字符串。

#### 1.2.1.3. 获取路径
&emsp;&emsp;Path 返回的是一个路径对象，那么如何才可以只打印路径的字符串格式呢，我们可以通过 `str(Path 对象)` 进行转换，当需要 bytes 格式时，也可以使用 `bytes(Path 对象)` 转换。

```python
In : bytes(p2)  
Out: b'/etc/sysconfig/network-scripts'

In : str(p2)  
Out: '/etc/sysconfig/network-scripts'

```

#### 1.2.1.4. 父目录`parent`: 当前目录的逻辑父目录`parents`: 所有父目录的序列，索引 0 为当前目录的父目录，依次类推

```python
In : p2.parent
Out: PosixPath('/etc/sysconfig')

In : p2.parent.parent
Out: PosixPath('/etc')

In : p2.parent.parent.parent    # 链式操作
Out: PosixPath('/')

In : p2.parents
Out: <PosixPath.parents>   # 可迭代对象

In : list(p2.parents)
Out: [PosixPath('/etc/sysconfig'), PosixPath('/etc'), PosixPath('/')]

```

> parent 属性，看似支持类 js 的链式操作，主要还是因为每次使用 parent 属性时，返回的还是一个 Path 对象，所以才可以一直 parent 下去。  

#### 1.2.1.5. 目录的组成部分
&emsp;&emsp;在一个目录的绝对路径中我们可能会单独使用目录的名称、目录的后缀名等等，Path 对象提供了专门的属性及方法便于获取或者对它们进行修改。
- `name`: 目录的最后一个部分
- `suffix`：目录中最后一个部分的扩展名
- `stem`：目录中最后一个部分，不包含后缀名
- `suffixes`: 多个后缀名形成的列表

```python
In : from pathlib import Path  
In : p = Path('/tmp/mysql.tar.gz')  
In : p.name  
Out: 'mysql.tar.gz'

In : p.suffix  
Out: '.gz'  
In : p.stem  
Out: 'mysql.tar'

In : p.suffixes  
Out: ['.tar', '.gz']

```

-`with_suffix(suffix)`: 有扩展名则替换，无则补充扩展名(注意后缀名要加点)
- `with_name(name)`：替换目录最后一个部分并返回一个新的路径

```python
In : p  
Out: PosixPath('/tmp/mysql.tar.gz')

In : p.with_suffix('.abc')  
Out: PosixPath('/tmp/mysql.tar.abc')

In : p1 = Path('/tmp/nginx')  
In : p1.with_suffix('.abc')  
Out: PosixPath('/tmp/nginx.abc')

In : p  
Out: PosixPath('/tmp/mysql.tar.gz')

In : p.with_name('nginx.tar.gz')  
Out: PosixPath('/tmp/nginx.tar.gz')

```

#### 1.2.1.6. 全局方法及判断方法
- `cwd()`: 返回当前工作目录
- `home()`: 返回当前家目录
- `is_dir()`: 是否是目录，是目录且存在，则返回 True
- `is_file()`: 是否是普通文件，是文件且存在，则返回 True
- `is_symlink()`: 是否是软链接
- `is_socket()`: 是否是 socket 文件
- `is_block_device()`: 是否是块设备
- `is_char_device()`: 是否是字符设备
- `is_absolute()`: 是否是绝对路径

```python
In : p = Path('/etc','sysconfig')  
In : p2 = Path('/etc','hosts')  
In : p3 = Path('/etc','rc.d','rc3.d','S10network')  
In : p.is_dir()  
Out: True

In : p1.is_file()  
Out: False

In : p2.is_file()  
Out: True

In : p3.is_symlink()  
Out: True

In : p.is_absolute()  
Out: True 

```

-`resolve()`: 返回当前 Path 对象的绝对路径。如果是软连接，则直接被解析
- `absolute()`: 获取 Path 对象的绝对路径

```python
In : p3 = Path('hosts')  
In : p3  
Out: PosixPath('hosts')

In : p3.resolve()          # 软链接的真正路径  
Out: PosixPath('/etc/hosts')

In : p3.absolute()         # 软链接的绝对路径  
Out: PosixPath('/home/python/py368/hosts')

```

-`exists()`: 文件或者目录是否存在
- `rmdir()`: 删除空目录(没有提供目录为空的方法)
- `touch(mode=0o666，exist_ok=False)`: 创建一个文件
    * `mode`: 文件的属性，默认为 666
    * `exist_ok`: 在 3.5 版本加入，False 时，路径存在，抛出 FileExistsError;True 时，异常将被忽略

```python
In : p = Path('/tmp','hello.py')  
In : p.exists()  
Out: False

In : p.touch(mode=0o666,exist_ok=False)  
In : p.exists()  
Out: True

In : p.touch(mode=0o666,exist_ok=False)  
---------------------------------------------------------------------------
FileExistsError                           Traceback(most recent call last)
...
FileExistsError: [Errno 17] File exists: '/tmp/hello.py'

In :  

```

- as_uri(): 将路径返回成 URI

```python
In : p2.as_uri()  
Out: 'file:///etc/hosts'

```

-`mkdir(mode=0o777,parents=False,exist_ok=False)`: 创建一个目录
    * `parents`：是否创建父目录，True 等同于 `mkdir -p`, False 时，父目录不存在曝出 FileNotFoundError
    * `exist_ok`: 在 3.5 版本加入，False 时，路径存在，抛出 FileExistsError;True 时，异常将被忽略
- `iterdir()`: 迭代当前目录，不递归。

```python
In : for x in p4.parents[0].iterdir(): 
...:     if x.is_dir(): 
...:         flag = False 
...:         for _ in x.iterdir(): 
...:             flag = True 
...:             break 
...:         print('dir: {} , is {}'.format(x,'not empty ' if flag else 'empt
...: y' )) 
...:     elif x.is_file(): 
...:         print('{} is a file'.format(x)) 
...:     else: 
...:         print('other file')

```

> 判断文件类型，当文件为目录时，判断其是否为空目录。  

#### 1.2.1.7. 通配符
- `glob(partten)`: 在 `目录下` 通配给定的格式
- `rglob(partten)`: 在 `目录下` 递归通配给定的格式(递归目录)  
- `match(partten)`: 模式匹配(对当前 Path 对象进行匹配)，成功返回 True
支持的通配符与 Linux 下相同：
- ？ 表示一个字符
- \* 表示任意个字符
- [abc] 或[a-z] 表示区间内的任意一个字符

```python
In : p4  
Out: PosixPath('/etc/sysconfig/network-scripts')

In : list(p4.glob('ifu?-*'))  
Out: 
[PosixPath('/etc/sysconfig/network-scripts/ifup-aliases'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-bnep'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-eth'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-ippp'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-ipv6'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-isdn'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-plip'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-plusb'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-post'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-ppp'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-routes'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-sit'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-tunnel'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-wireless'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-ib'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-Team'),
 PosixPath('/etc/sysconfig/network-scripts/ifup-TeamPort')]

In : p4.match('/etc/*/network-script?')  
Out: True

```

#### 1.2.1.8. 目录属性
- `stat()`: 查看目录的详细信息，相当于 stat 命令
- `lstat()`: 如果是符号链接，则显示符号链接本身的文件信息

```python
In : p4.stat()  
Out: os.stat_result(st_mode=16877, st_ino=67533402, st_dev=2050, st_nlink=2, st_uid=0, st_gid=0, st_size=4096, st_atime=1550229289, st_mtime=1545830238, st_ctime=1545830238)

```

### 1.2.2. 文件操作
&emsp;&emsp;Path 对象同样提供了打开文件的函数，功能类似于内建函数 open。返回一个文件对象。当我们创建一个 Path 对象时，这个文件已经被打开，当我们写入数据时，文件不存在会新建，重名或者是目录，会有相应的异常提示，它的语法是

```python
Path.open(mode='r',buffering=-1,encoding=None,errors=None,newline=None)

```例：

```python
In : p5  
Out: PosixPath('/tmp/123')

In : p = p5.open(mode='r')  
In : p  
Out: <_io.TextIOWrapper name='/tmp/123' mode='r' encoding='UTF-8'>

In : p.read()  
Out: '123'

In : p5.read_text()     # 不存在时报异常，存在则直接打开并读取  
Out: '123'

```

3.5 以后新增加的函数方法：
- `Path.read_bytes()`: 以 'rb' 方式读取路径对应文件，并返回二进制流。
- `Path.read_text()`: 以 'rt' 方式读取路径文件， 并返回文件。__无视指针__
- `Path.write_bytes()`: 以 'wb' 方式写入数据到路径对应文件中。
- `Path.write_text()`: 以 'wt' 方式写入数据到路径对应文件中。

## 1.3. os 模块
os 模块的常用方法：

```python
os.getcwd():        获取当前路径
os.chdir()：        切换当前目录，当路径中存在 \ 的时候，由于是转意的意思，那么就需要对 \ 进行转意，那么路径就是 c:\\User, 或者在目录前面加 r，表示后面的字符串不进行解释
os.curdir():        获取当前目录名
os.pardir():        获取上级目录名
os.mkdir('dir'):    创建目录，注意只能创建一级目录
os.makedirs('dir_path'): 创建多级目录
os.rmdir('dir'):    删除一个目录
os.removedir('dir_path')：删除多级目录（目录为空的话）
os.listdir('dir'):  显示目录下的所有文件，默认为当前目录，返回的结果为 list
os.remove('file'):  删除一个文件
os.rename('old_name','new_name'): 修改文件名称
os.stat('file/dir')：获取文件 / 目录的 stat 信息(调用的是系统的 stat)
os.sep:             返回当前操作系统的路径分隔符(Windows 下：\\ , Linux 下:/）
os.linesep:         返回当前操作系统的换行符（Windows 下:\r\n  ,Linux 下:\n）
os.pathsep:         返回当前操作系统环境变量分隔符（Windows 下是；,Linux 下是:）
os.name:            返回当前系统的类型（nt 表示 Windows,  posix 表示 Linux）
os.system('Commmand'): 执行命令
os.environ:         获取系统环境变量，使用字典存储
os.path.abspath('dir/file'): 获取 dir/file 的绝对路径
os.path.split('path'): 把路径分割为目录和文件名组成的元组格式，不管 path 是否存在
os.dirname('path')：获取文件的父目录名称，不管 path 是否存在
os.basename('path'): 获取文件的名称，不管 path 是否存在

```

> os.stat(follow_symlinks=True)，返回源文件本身信息，False 时，显示链接文件的信息，对于软连接本身，还可以使用 os.lstat 方法

```python
In : os.lstat('hosts')  
Out: os.stat_result(st_mode=41471, st_ino=2083428, st_dev=2050, st_nlink=1, st_uid=1001, st_gid=1001, st_size=10, st_atime=1550259162, st_mtime=1550259161, st_ctime=1550259161)

In : os.stat('hosts')  
Out: os.stat_result(st_mode=33188, st_ino=67245317, st_dev=2050, st_nlink=1, st_uid=0, st_gid=0, st_size=158, st_atime=1550229294, st_mtime=1370615492, st_ctime=1545666279)

In : os.stat('hosts',follow_symlinks=False)      # 等同于 os.lstat()  
Out: os.stat_result(st_mode=41471, st_ino=2083428, st_dev=2050, st_nlink=1, st_uid=1001, st_gid=1001, st_size=10, st_atime=1550259162, st_mtime=1550259161, st_ctime=1550259161)

In :  

```

# 2. shutil 模块
&emsp;&emsp;根据前面所学的知识，我们如果想要进行文件拷贝，需要先打开两个文件对象对象，源文件读取内容，写入到目标文件中去。 这种方式虽然完成了文件的拷贝，但是却丢失了文件的属性信息，比如属组、权限等，因为我们根本没有进行复制。所以，python 提供了一个用于高级文件操作的库，它的名字就叫做 shutil。

## 2.1. copy 复制
- `shutil.copyfileobj(fsrc,fdes,length)`: 将文件内容拷贝到另一个文件中，可以只拷贝部分内容，需要我们自行打开文件对象进行 copy,length 表示 buffer 的大小，需要注意的是 fdes 必须可写

```python

> >> import os,shutil  

> >> os.system('ls')  

1.txt

> >> shutil.copyfileobj(open('1.txt'),open('2.txt','w'))  

> >> os.system('ls')  

1.txt  2.txt

> >>   

```

-`shutil.copyfile(fsrc,fdes)`: 复制文件，我们只需要传入文件名称即可进行复制，不用自行预先打开，等于创建一个新的文件，把老文件写入到新文件中然后关闭，新创建的文件权限和属主等信息遵循操作系统规定(本质上还是调用 copyfileobj)

```python

> >> shutil.copyfile('1.txt','3.txt')  

> >> os.system('ls')  

1.txt  2.txt  3.txt

```

-`shutil.copymode(src,des)`: 复制文件权限，既把 src 文件的权限复制给 des 文件，只改变权限，不改变其他比如属组，内容等(des 文件必须存在)

```python

> >> os.system('ls -l')  

total 12
-rwxrwxrwx 1 root root 6 Mar  9 18:35 1.txt
-rw-r--r-- 1 root root 6 Mar  9 18:36 2.txt
-rw-r--r-- 1 root root 6 Mar  9 18:38 3.txt

> >> shutil.copymode('1.txt','2.txt')  

> >> os.system('ls -l')  

total 12
-rwxrwxrwx 1 root root 6 Mar  9 18:35 1.txt
-rwxrwxrwx 1 root root 6 Mar  9 18:36 2.txt
-rw-r--r-- 1 root root 6 Mar  9 18:38 3.txt

> >>   

```

-`shutil.copystat(src,des)`: 复制文件的权限，还包括，atime，mtime，flags 等信息，不改变文件内容（des 需存在）

```python

> >> os.system('stat 1.txt')  

  File: `1.txt'
  Size: 6             Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d    Inode: 926326      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (0/    root)   Gid: (0/    root)
Access: 2017-03-09 18:36:59.223738919 +0800
Modify: 2017-03-09 18:35:23.148738381 +0800
Change: 2017-03-09 18:39:59.061738605 +0800

> >> os.system('stat 3.txt')  

  File: `3.txt'
  Size: 6             Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d    Inode: 940237      Links: 1
Access: (0644/-rw-r--r--)  Uid: (0/    root)   Gid: (0/    root)
Access: 2017-03-09 18:39:42.214738376 +0800
Modify: 2017-03-09 18:38:13.862738316 +0800
Change: 2017-03-09 18:38:13.862738316 +0800

> >> shutil.copystat('1.txt','3.txt')  

> >> os.system('stat 3.txt')  

  File: `3.txt'
  Size: 6             Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d    Inode: 940237      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: (0/    root)   Gid: (0/    root)
Access: 2017-03-09 18:36:59.223738000 +0800
Modify: 2017-03-09 18:35:23.148738000 +0800
Change: 2017-03-09 18:44:33.286738354 +0800

> >>   

```

-`shutil.copy(src,des)`: 复制文件的同时复制权限信息，等同于执行了如下命令:
    1. __shutil.copyfile(src,dest,follow_symlinks=True)__ 
    2. __shutil.copymode(src,dest,follow_symlinks=True)__
- `shutil.copy2(src,des)`: 比 copy 对了全部原数据，但需要平台支持，等同于执行了如下命令:
    1. __shutil.copyfile(src,dest,follow_symlinks=True)__ 
    2. __shutil.copystat(src,dest,follow_symlinks=True)__
- `shutil.copytree(src,dest,symlinks=False,ignore=None,copy_function=copy2,ignore_dangling_symlinks=False)`: 递归复制文件，类似于 copy -r，默认使用 copy2
    - src 必须存在，dest 必须不存在。
    - `ignore = func`, 提供一个 callable(src,namnes) --> ignoted_names。提供一个函数，它会被调用。src 是原目录，names 是原目录下的文件列表(os.listdir(src))，返回值是要被过滤的文件名的 set 类型数据

```python
In : def func(src,names): 
     ...:     ig = filter(lambda x: not x.endswith('conf'),names) 
     ...:     return set(ig)

In : os.listdir('old')  
Out: 
['123.txt',
 '456.txt',
 'asound.conf',
 'brltty.conf',
 'chrony.conf',
 'dleyna-server-service.conf',
 'dnsmasq.conf',
 'dracut.conf',
 'e2fsck.conf',
 'fprintd.conf',
 'fuse.conf',
 'GeoIP.conf',
 'host.conf']

In : shutil.copytree('old','new',ignore=func)  
Out: 'new'

In : os.listdir('new')  
Out: ['123.txt', '456.txt']

```

> shutil 模块自己也实现了一个过滤某些特征的方法，`shutil.ignore_patterns('*py')`，表示过滤 * py 的文件。

## 2.2. rm 删除
- `shutil.rmtree(path, ignore_errors=False, onerror=None)`: 递归的删除文件，类似于 rm -rf，需要注意的是它不是原子操作，如果删除错误，就会中断，已经删除的就删除了。
    - ignore_errors：为 True 时，忽略错误。 为 omitted/False 时，onerror 生效
    - onerror 为 callabe，接受三个参数 function、path 和 sys.exc_info。(不常用)

```python

> >> os.system('ls -l')  

total 8
drwxr-xr-x 2 root root 4096 Mar  9 18:46 test
drwxr-xr-x 2 root root 4096 Mar  9 18:46 test1

> >> shutil.rmtree('test1')  

> >> os.system('ls -l')  

total 4
drwxr-xr-x 2 root root 4096 Mar  9 18:46 test

> >>   

```

## 2.3. move 移动
- `shutil.move(src,des,copy_function=copy2)`: 递归移动文件、目录到目标、返回目标，类似于 mv 命令，本身使用的是 os.rename 方法，如果不支持 rename，如果是目录则 copytree 再删除原目录。

```python
In : import shutil  
In : ls  
new/  old/

In : shutil.move('new','/tmp/new')  
Out: '/tmp/new'

In : ls  
old/

In : shutil.move('old','new_old')  
Out: 'new_old'

```

## 2.4. 打包
- `shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, owner=None, group=None,)`: 打包压缩，支持 "zip", "tar", "gztar","bztar", or "xztar"
    - base_name: 打包后的包名
    - format：打包 / 压缩的格式，gztar 就是 tar.gz
    - root_dir: 要打包的目录
    - owner：包的属主
    - group：包的属组

```python
In : shutil.make_archive('abc','gztar',root_dir='new_old')  
Out: '/home/python/py368/abc.tar.gz'

In : ls  
123/  abc.tar.gz  new_old/

```

