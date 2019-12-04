**16 - 文件操作-StringIO-BytesIO**

---

[TOC]

---

# 1. 文件操作
&emsp;&emsp;读写文件是最常见的 IO 操作(一般说 IO 操作，指的是文件 IO，如果是网络，一般都会直接说网络 IO)，在磁盘上读写文件的功能都是由操作系统提供的，操作系统不允许普通的程序直接操作磁盘(大部分程序都需要间接的通过操作系统来完成对硬件的操作)，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。在操作系统中，文件常用的操作有：

| 功能 | 介绍 |
| --|-- |
| open | 打开 |
| read | 读取 |
| write | 写 |
| close | 关闭 |
| readline | 行读取 |
| readlines | 多行读取 |
| seek | 文件指针操作 |
| tell | 指针操作   |
## 1.1. open 函数介绍
&emsp;&emsp;在 python 中，我们使用 open 函数来打开一个文件，然后返回一个文件对象(流对象) 和文件描述符。打开文件失败，则返回异常。

> 第三方模块 codecs 包中提供的 open 函数，具备内置函数 open 的所有功能，并且在内部它对目标文件进行了编码的与判断处理，当你不知道目标文件的编码类型时，使用 codecs.open 来说更可靠。  

## 1.2. 打开操作
&emsp;&emsp; 想要读取文件，那么就需要先行打开文件。下面来看一下 open 函数的用法

```python
open(['file', "mode='r'", 'buffering=-1', 'encoding=None', 'errors=None', 'newline=None', 'closefd=True', 'opener=None'],)

```

-`file`：要打开的文件名(默认为当前路径，否则要指定绝对路径)。
- `mode`：表示打开文件的格式。
- `buffering`: 设置缓冲区的大小(二进制模式和文本模式不同)
- `encoding`：打开文件的编码格式(文本模式)
- `errors`: 转码错误时是否提示异常
- `newline`: 文本模式中对新行的处理方式
- `closefd`: 删除描述符时，文件对象是否释放

> &emsp;&emsp;Python 2.x 中包含 file 和 open 两个操作文件的函数，Python 3.x 中只有 open，操作方法相同 `f = file('/etc/passwd','r')`    

### 1.2.1. mode 模式
文件打开的方式有如下几种：
描述字符 | 意义 | 备注
----|----|---
r | 只读打开 | 文件的默认打开方式，文件不存在会报异常
w | 只写打开 | 文件不存在会创建，存在的话，会覆盖源文件（非追加）
x | 创建并只写一个新文件 | 文件已存在则报错
a | 只追加写模式 | 在文件末尾追加，文件不存在，新建并追加
b | 二进制模式 |`字节流`，将文件就按照字节理解，与字符编码无关。二进制模式操作时，字节操作使用 bytes 类型
t | 文本模式 |`字符流`，将文件的字节按照某种字符编码理解，按照字符操作，缺省模式
+| 读写打开一个文件 | 给原来只读、只写方式打开提供缺失的读或者写能力

> 默认使用文本只读模式打开，特殊文件需要用文本模式传输的话，建议使用 b    

&emsp;&emsp;`+ 符`，为 r、w、a、x 提供缺失的读或者写的功能，但是，获取文件对象依旧按照 r、w、a、x 自己的特征。但 + 不能单独使用，可以认为它是为前面的模式字符做的增强功能。

描述字符 | 意义
---|---
r+| 读模式附加写功能
w+| 写模式附加读功能
a+| 追加写模式附加读功能
x+| 打开一个新文件可读可写

> 以上为文本模式，二进制模式时只需要添加 b 即可。即 r+b, 或者 rb + 都可  

```python
In : f = open('hello.txt','r')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback(most recent call last)
<ipython-input-2-27a5c78b3969> in <module>
----> 1 f = open('hello.txt','r')

FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'

In : f = open('123.txt')

In : f.read()
Out: '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00abc'

In : f.close()

In : f = open('123.txt','w')

In : f.read()
---------------------------------------------------------------------------
UnsupportedOperation                      Traceback(most recent call last)
<ipython-input-7-571e9fb02258> in <module>
----> 1 f.read()

UnsupportedOperation: not readable

In :

```

注意：
- 我们把这个 f 成为文件句柄（用来标识一个文件的内存对象），包含文件名，字符集，大小，硬盘上的起始位置等等。
- f 在这里就变成了一个文件迭代器，我们可以通过使用 for line in f , 去循环的读取文件的每一行内容

```python
# for 循环遍历文件，打印文件的每一行

In : f = open('123.txt')

In : for i in f:
...:     print(i,end='')
...:
hello
world
my
name
is
colin
thanks
In :

```

> 注意：这里 for line in fd，其实可以从 fd.readlines() 中读取，但是如果文件很大，那么就会一次性读取到内存中，非常占内存，而这里 fd 存储的是对象，只有我们读取一行，它才会把这行读取到内存中，建议使用这种方法。  

### 1.2.2. 文件指针
&emsp;&emsp;为什么文件只能读一次，第二次读就是空的了？是否可以重复读取呢？在对文件操作中，会存在一个指针 `用于指定当前光标的位置`，当我们读完一次后， 文件指针就指向了文件的末尾了，那么如果想要重复读取，那么只需要对指针的位置进行调整即可。
1. mode = r , 指针起始在 0
2. mode = a , 指针其实在 EOF(end of file：文件末尾)

```python
f.tell()    # 显示当前文件指针的位置
f.seek(offset, whence=0, /)   # 移动文件指针的位置

```

- offset：偏移多少字节
- whence：从哪里开始  
在文本模式下：
- whence `0`：缺省值，表示从头开始，offset 只能正整数
- whence `1`：表示从当前位置开始，offset 只能设置为 0
- whence `2`：表示从 EOF 位置开始，offset 只能设置为 0

> 文本模式支持从开头向后偏移的方式。whence 为 1 时，只支持偏移 0(`seek(0,0)`)，相当于原地不同，没什么卵用。whence 为 2 时，表示从 EOF 开始，但也只支持偏移 0(`seek(0,2)`)，相当于将文件指针移动到 EOF。    

二进制模式下：
- whence `0`: 缺省值，表示从头开始，offset 只能正整数
- whence `1`: 表示从当前位置，offset 可正可负
- whence `2`: 表示从 EOF 开始，offset 可正可负

> 二进制模式支持任意起点的偏移，从头、从尾部、从中间位置开始，向后 seek 可以超界，但是向前 seek 的时候，不能超界，否则抛异常  

### 1.2.3. 缓冲区
&emsp;&emsp;open 函数的第三个参数为 buffering，叫作缓冲区，缓冲区是内存中的一小部分空间，用于存放准备写入磁盘的数据，操作系统在进行磁盘写入的时候，由于磁盘速度要远远慢于 CPU 以及内存，如果每次写入数据时，都要直接写到磁盘上的话，那么效率会非常的低，所以在操作系统层面会对写入操作进行优化，比如缓冲区默认大小为 4K 或者 4K 的倍数(为什么是 4K，和磁盘扇区有关，这里就不详述了)，当写入的数据小于 4K，会先存在缓冲区，当缓冲区满了，或者超过一定时间没有写入，操作系统会将数据一次性的刷入(flush) 磁盘。  
&emsp;&emsp;buffering 的默认值为 - 1，表示使用缺省大小的 buffer，如果是二进制模式，由 `io.DEFAULT_BUFFER_SIZE` 决定，默认是 `4096` 或者 `8192`，如果是文本模式，设备类型为终端设备时，使用 `行缓存方式`，如果不是，则使用二进制模式的策略。使用其他值时，有如下含义：

- `0` ：只在二进制模式使用，表示关闭 buffer
- `1` ：只在文本模式使用，表示使用行缓冲。(见到换行符就 flush)
- `大于 1` ：用于指定 buffer 的大小  
二进制场景：

```

 python
In : import io

In : f = open('123.txt','w+b')
In : print(io.DEFAULT_BUFFER_SIZE)
8192

In : f.write("colin".encode())
Out: 5
In : f.seek(0)
Out: 0
In : f.read()
Out: b'colin'

In : f.flush()    # 默认情况下缓冲区大小为 8192 字节，所以我们写入的不会被立即刷入到磁盘上，如果我们要手动刷入可以手动执行 flush 命令
In : f.close()   # close 会触发 flush 操作

In : f = open('123.txt','w+b',4)  # 缓冲区为 4 个字节
In : f.write('dax'.encode())    # 3 个字节不会刷入磁盘
Out: 3
In : f.write('in'.encode())   # 超过缓冲区大小会直接连同本次写入的数据一起刷入磁盘
Out: 2

In : f.seek(0)
Out: 0
In : f.read()
Out: b'colin'

In : f.flush()
In : f.close()

​```文本字符串场景：

​```python
In : f = open('123.txt','w+')   # 没有指定缓冲区的大小，采用默认值 - 1（由于不是终端设备，所以采用二进制的策略 由 io.DEFAULT_BUFFER_SIZE 控制
In : !cat 123.txt

In : f.write('colin')
Out: 5

In : !cat 123.txt
In : f.write('\n')   # 遇到换行符的时候并没有刷入磁盘
Out: 1
In : !cat 123.txt  
In : f = open('123.txt','w+',1)   # 指定缓冲区的大小为 1(行)
In : f.write('colin')
Out: 5

In : f.write(' hello')
Out: 6

In : !cat 123.txt    # 没有遇到换行符，所以不会刷入磁盘
In : f.write('\n')   # 遇到换行符，然后刷入磁盘
Out: 1
In : !cat 123.txt
colin hello

In :

```

buffering | 说明
---|---
buffering=1 | 文本和二进制模式时，都是 io.DEFAULT_BUFFER_SIZE 控制
buffering=0 | 文本模式时不支持，二进制模式时表示关闭缓冲区
buffering=1 | 文本模式表示行换成，二进制模式表示一个字节
buffering>1 | 文本模式时，是 io.DEFAULT_BUFFER_SIZE 字节，flush 后把当前字符串也写入磁盘。二进制模式时，表示缓冲区的大小，直到超过这个值时，才会刷入磁盘

> 一般来说，文本模式一般都用默认缓冲区大小，二进制模式可以指定 buffer 的大小。除非我们明确知道，否则选择默认缓冲区大小是一个比较好的选择，另外在日常编程中，明确知道需要写磁盘了，都会手动调用一次 flush，而不是等到自动 flush 或者 close 的时候。  

### 1.2.4. encoding 编码
&emsp;&emsp;当我们操作二进制文件的时候，数据都是十六进制的，并没有什么编码的一说。而在使用文本模式时，就需要指定编码类型了，常用的中文编码比如，GBK、UTF-8、Unicode 等，文件在内存中都是 Unicode 格式的，而存储在磁盘上就是按照本地编码的格式存储了，windows 上默认的是 GBK(ANSI,cp936)，当我们存储的文本数据不是默认的格式时，在打开时就会产生乱码，这时可以使用指定编码格式打开文件。

```python
encoding=None, 默认值时，表示使用操作系统默认编码类型
- windows: GBK(0xB0A1)
- Linux: UTF-8(0xE5 95 8A)

```

### 1.2.5. 其他参数`errors`: 什么样的编码错误将被捕获。
- None/strict：有编码错误将抛出 ValueError 异常
- ignore：表示忽略  
`newline`: 文本模式中，换行的转换。可以为 None、''(空串)、'\r'、'\n'、'\r\n'。
- 读时，None 表示 '\r'、'\n'、'\r\n' 都被转换为 '\n';''(空串) 表示不会自动转换通用换行符；其他合法字符表示换行符就是指定字符，就会按照指定字符分行
- 写时，None 表示 '\n' 都会被替换为系统指定缺省分隔符(os.linesep);'\n' 表示 '\n' 不替换；其他的合法字符表示 '\n' 会被替换为指定的字符

`closefd`: 关闭文件描述符.
- True: 表示关闭它
- False: 会在文件关闭后保持这个文件描述符

> fileobj.fileno() 查看  

## 1.3. 读写操作
`read(size=-1)`: 表示读取的多少个字符或字节；负数或者 None 表示读取到 EOF(end of file), 中文文本时，表示 size 个字符。  

```python

>>> f = open('123.txt','r+')  

>>> f.read(5)  

'colin'

>>> f.read(5)  

' hell'

>>> f.read(1)  

'o'

>>> f.read(1)  

'\n'

>>> f.read(1)  

' 你 '
`

```readline(size=-1)`: 一行行读取文件内容。size 设置一次能读取行内几个字符或者字节。负数或者 None 表示读取到 EOF(end of file)

```python

>>> f = open('123.txt','r+')  

>>> f.readline(3)  

'a d'

>>> f.readline()    

'axin hello world\n'

>>> f.readline(-10)    

'c\n'
`

​```readlines(hint=-1)`: 读取所有行并返回列表。**`当指定 hint 为负数时，则会读取所有行，当指定为正数时，表示读取 hint 个字符所在的行`**。比如第一行有 6 个字符，第二行有 3 个字符，当我们使用 readlines(7) 时，就会返回两行，而如果使用 readlines(5) 时就会只返回第一行。

​```python
In : f.readlines()
Out: ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9']

In : f = open('123.txt','r+')

In : f.readlines(9)
Out: [' 你好啊我了个去 \n', ' 为什么 \n']

In : f.readlines(3)
Out: [' 你好 \n', ' 在 ']

In :
`

​```write(s)`: 把字符串写入到文件中并返回写入字符串的个数。
`writelines(lines)`: 将字符串列表写入文件中。

​```python
In : f = open('123.txt','r+')

In : f.seek(0,2)
Out: 25

In : f.write('10')
Out: 2

In : f.seek(25)
Out: 25

In : f.read()
Out: '10'

In : f.writelines(['11','12'])

In : f.seek(25)
Out: 25

In : f.read()
Out: '101112'

```

## 1.4. 关闭操作
&emsp;&emsp;当我们打开一个文件时，那么在系统中就会存在一个文件描述符对应这个文件，并且在文件系统中，一个程序可以使用的文件描述符的数量是有限的，如果我们使用完毕后不进行释放，那么很有可能就耗光文件描述符的数量(Linux 中默认的文件描述符为 1024，使用 ulimit -a 查看)，产生异常，所以在使用完毕后，我们就需要手动的进行关闭

```python
f.close()  

```

> 关闭文件的操作，会同时调用 flush()，把缓冲区的数据刷入磁盘。当文件已经关闭，再次关闭没有任何效果  

## 1.5. 上下文管理
&emsp;&emsp;上面说我们每次打开一个文件都需要手动的进行关闭，那么如果忘记了，这个文件会一直占用着对应的文件描述符，如果多次打开一个文件不关闭，那么每次都会占用新的文件描述符，直到文件描述符用完。上下文管理就是为了解决这种问题的，它有如下特点：
1. 使用 with .. as 关键字。
2. with 语句块执行完毕的时候，会自动关闭文件对象
3. 不会开启新的作用域(不会产生诸如函数的内部变量等)  
&emsp;&emsp;2.6 以上版本支持 with 读取，`with open('/tmp/hello.txt') as fd:`, 然后所有打开文件的操作都需要缩进，包含在 with 下才，这样不需要明确的指定 close，当新的代码没有缩进的时候，文件会自动关闭。

```python
In : with open('123.txt','r+') as f:
     ...:     f.read()
     ...:

In : f.closed
Out: True

​```或者：

​```PYTHON
In : f = open('123.txt','r+')

In : with f:
     ...:     f.read()
     ...:

In : f.closed
Out: True

```

## 1.6. 文件对象的其他方法
文件对象的内置方法还有很多种，如下所示：

```python
fd.closed()：    # 判断文件是否被关闭，若被打开提示 False，没有的话提示 True
fd.flush()：     # 把修改的内容，强制刷新到文件中去
fd.isatty：      # 判断是否是一个终端文件
fd.mode：        # 查看文件的打开模式
fd.name：        # 查看文件的名称
fd.next：        # 迭代的方法，和 readline 很像，区别是，next 读到末尾会报错，readline 会继续返回空
fd.read：        # 一次性读取所有内容，以字符串的方式存取
fd.readable():   # 判断文件是否可读
fd.readlines：   # 一次性读取所有内容，以列表的方式存取（适合操作小文件）
fd.readline()：  # 每次读取一行内容
fd.seek(0)：     # 调整文件读取的指针位置
fd.seekable()：  # 判断文件是否可以调整指针位置（tty，磁盘等文件是不能被 seek 的），可以被 seek 则返回真，否则返回假
fd.tell()：      查询文件目前读取位置（以字符为单位）
fd.truncate()：  截取文件，从开头开始截取，不指定指针位置的话，那么会清空文件
fd.write：       把一个字符串写入到文件中去
fd.writelines()：把字符串列表写入文件中
fd.xreadlines()：读一行打印一行，针对大文件非常适用 -----> Python 2.x 中适用，3.x 中已经取消
fd.encoding:     查看文件的编码
fd.writeable()： 判断文件是否可以写
fd.fileno()：    返回文件在操作系统上的文件描述符（一个进程的运行默认会打开三个特殊的文件描述符：0 表示 stdin、1 表示 stdout，2 表示 stderr）
fd.name：        文件名称 

```

# 2. StringIO 模块
&emsp;&emsp;用于在内存空开辟一个文本模式的 buffer, 可以像文件对象一样操作它，当 close 方法被调用时，这个 buffer 会被释放.

> 使用前需要先进行导入，from io import StringIO  

```python
In : from io import StringIO

In : s = StringIO()   # 实例化一个 StringIO 对象用于读写，相当于 f = open('123.txt','r+')

In : s.write('123')
Out: 3

In : s.readline()
Out: ''

In : s.seek(0)
Out: 0

In : s.readline()
Out: '123'
`

​```getvalue()`: 获取全部内容，跟文件指针没有关系.

​```python
In : from io import StringIO

In : s = StringIO()

In : s.write('123')
Out: 3

In : s.readline()
Out: ''

In : s.seek(0)
Out: 0

In : s.readline()    # 指针已经切换到文件末尾
Out: '123'

In : s.getvalue()    # 无视指针，可以读取所有
Out: '123'

```

> 一般来说，磁盘的操作比内存的操作要慢得多，内存足够的情况下，一般的优化思路是少落地，减少磁盘 IO 的过程，可以大大提高程序的运行效率.  

# 3. BytesIO 模块
&emsp;&emsp;用于在内存中开辟一个二进制模式的 buffer, 可以像文件对象一样操作它，当 close 方法被调用时，这个 buffer 会被释放.

> 调用前需要先导入: from io import BytesIO  

```python
In : from io import BytesIO

In : b = BytesIO()  # 实例化一个 BytesIO 对象用于存储二进制数据

In : b.write(b'abc')
Out: 3

In : b.seek(0)
Out: 0

In : b.read()
Out: b'abc'

In : b.getvalue()   # 同样无视指针的存在
Out: b'abc'

```

&emsp;&emsp;针对 StringIO 和 BytesIO 来说，还有如下方法:
1. readable(): 可读吗？2. writeable(): 可写吗？3. seekable(): 可以调整指针吗？# 4 file-like 对象
&emsp;&emsp;类文件对象，可以像文件对象一样操作，比如 socket 对象，输入输出对象(stdin,stdout) 等都是类文件对象.

```python
In : from sys import stdin,stdout

In : stdout.write('123')
123
In : type(stdout)
Out: colorama.ansitowin32.StreamWrapper

In :

```

每个程序初始化运行时，都会打开 3 个文件:
- stdin: 标准输入
- stdout: 标准输出
- stderr: 标准错误输出