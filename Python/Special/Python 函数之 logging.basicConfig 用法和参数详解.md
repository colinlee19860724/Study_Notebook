- [1. Python 函数之 logging.basicConfig 用法和参数详解](#1-python-函数之-loggingbasicconfig-用法和参数详解)
    - [1.1. logging 模块简介](#11-logging-模块简介)
    - [1.2. `logging.basicConfig(**kwargs)`](#12-loggingbasicconfigkwargs)
    - [1.3. LogRecord 属性](#13-logrecord-属性)


# 1. Python 函数之 logging.basicConfig 用法和参数详解

## 1.1. logging 模块简介
&emsp;&emsp;logging 模块是 Python 内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等；相比 print，具备如下优点：

1. 可以通过设置不同的日志等级，在 release 版本中只输出重要信息，而不必显示大量的调试信息；
2. print 将所有信息都输出到标准输出中，严重影响开发者从标准输出中查看其它数据；logging 则可以由开发者决定将信息输出到什么地方，以及怎么输出；
3. 和 print 相比，logging 是线程安全的。

> &emsp;&emsp;**线程安全**：线程执行一段代码，不会产生不确定的结果，那这段代码就是线程安全的。  
> &emsp;&emsp;多线程的时候执行 print 应该是一行行打印，但是很多字符串打在了一起，为什么？  
> &emsp;&emsp;说明，print 函数被打断了，被线程切换打断了。print 函数分两步，第一步打印字符串，第二步打印换行符，就在这之间，发生了线程的切换。这说明 print 函数是**线程不安全**的。  

&emsp;&emsp;**先举个例子：**
```python
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='my.log',
                    filemode='w')

logging.info('This is a info.')
logging.debug('This is a debug message.')
logging.warning('This is a warning.')

# 输出到同目录下 my.log 文件中的内容：
Wed 05 Jun 2019 22:25:32 test.py INFO This is a info.
Wed 05 Jun 2019 22:25:32 test.py WARNING This is a warning.
```
&emsp;&emsp;请读者根据以下参数自行解读为什么会有这样的输出。

## 1.2. `logging.basicConfig(**kwargs)`  
&emsp;&emsp;使用默认格式化程序创建 StreamHandler 并将其添加到根日志记录器中，从而完成日志系统的基本配置。如果没有为根日志程序定义处理程序，debug()、info()、warning()、error()和 critical() 函数将自动调用 basicConfig()。
&emsp;&emsp;如果根日志记录器已经为其配置了处理程序，则此函数不执行任何操作。

> 注解：这个函数应该在其他线程启动之前从主线程调用。在 2.7.1 和 3.2 之前的 Python 版本中，如果从多个线程调用此函数，则可能(在很少的情况下)不止一次地将处理程序添加到根日志记录器中，从而导致意想不到的结果，比如在日志中消息被复写。

&emsp;&emsp;支持以下关键字参数。

格式 | 描述
---|---
filename | 指定使用**指定的文件名**而不是 StreamHandler 创建 FileHandler。
filemode | 如果指定 filename，则以此模式打开文件('r'、'w'、'a')。默认为“a”。
format | 为处理程序使用指定的格式字符串。
datefmt | 使用 time.strftime() 所接受的指定日期/时间格式。
style | 如果指定了格式，则对格式字符串使用此样式。'%' 用于 printf 样式、'{' 用于 str.format()、'$' 用于 string。默认为“%”。
level | 将根记录器级别设置为指定的级别。
stream | 使用指定的流初始化 StreamHandler。注意，此参数与 filename 不兼容——如果两者都存在，则会抛出 ValueError。
handlers | 如果指定，这应该是已经创建的处理程序的迭代，以便添加到根日志程序中。任何没有格式化程序集的处理程序都将被分配给在此函数中创建的默认格式化程序。注意，此参数与 filename 或 stream 不兼容——如果两者都存在，则会抛出 ValueError。

## 1.3. LogRecord 属性
&emsp;&emsp;LogRecord 有许多属性，其中大部分是从构造函数的参数派生出来的。(注意，名称并不总是与 LogRecord 构造函数参数和 LogRecord 属性完全对应。)这些属性可用于将记录中的数据合并到格式字符串中。下表以 % 样式的格式字符串列出(按字母顺序)属性名、它们的含义和对应的占位符。

&emsp;&emsp;如果您使用 {} 格式 (str.format())，可以使用 {attrname} 作为格式字符串中的占位符。如果您正在使用 `$-formatting` (string.Template)，请使用 `${attrname}` 格式。当然，在这两种情况下，都要用想要使用的实际属性名替换 attrname。

&emsp;&emsp;在使用 {} 格式的情况下，您可以通过将它们放在属性名后面来指定格式化标志，并使用冒号将它们与属性名分隔开。例如 `{msecs:03d}` 的占位符将把毫秒值 4 格式化为 004。有关可用选项的详细信息，请参阅 `str.format()` 文档。

属性名称 | 格式 | 描述
---|---|---
args | 您不应该自己设置此格式。 | 参数组成的元组合并到 msg 中以生成消息，或 dict，其值用于合并(当只有一个参数时，它是一个字典)。
asctime | `%(asctime)s` | 创建日志记录时的时间（以便于人识读的格式）。默认情况下，它的形式是“2003-07-08 16:49:45,896”(逗号后面的数字是时间的毫秒部分)。
created | `%(created)f` | 创建日志记录的时间(由 time.time() 函数返回的时间戳（1970纪元后经过的浮点秒数）)。
exc_info | 您不应该自己设置此格式。 | 异常元组(如 sys.exc_info)，如果没有发生异常，则为 None。
filename | `%(filename)s` | **路径名**的**文件名**部分。
funcName | `%(funcName)s` | 包含日志记录调用的函数的名称。
levelname | `%(levelname)s` | 消息的文本日志级别('DEBUG'、'INFO'、'WARNING'、'ERROR'、'CRITICAL')。
levelno | `%(levelno)s` | 消息的数字日志级别(DEBUG、INFO、WARNING、ERROR、CRITICAL)。
lineno | `%(lineno)d` | 发出日志调用的源行号(如果可用)。
message | `%(message)s` | 已记录的消息，计算为 msg % args。这是在调用 Formatter.format() 时设置的。
module | `%(module)s` | 模块(文件名的名称部分)。
msecs | `%(msecs)d` | 创建日志记录时的毫秒部分。
msg | 您不应该自己设置此格式。 | 在原始日志记录调用中传递的格式字符串。与 args 合并以生成消息或任意对象(请参阅使用任意对象作为消息)。
name | `%(name)s` | 用于记录调用的日志程序的名称。
pathname | `%(pathname)s` | 发出日志调用的源文件的完整路径名(如果可用)。
process | `%(process)d` | 进程ID(如果可用)。
processName | `%(processName)s` | 进程名(如果可用)。
relativeCreated | `%(relativeCreated)d` | 创建日志记录的时间(以毫秒为单位)相对于加载日志模块的时间。
stack_info | 您不应该自己设置此格式。 | 堆栈帧信息(在可用的情况下)从当前线程的堆栈底部开始，直到并包括导致创建此记录的日志调用的堆栈帧。
thread | `%(thread)d` | 线程ID(如果可用)。
threadName | `%(threadName)s` | 线程名(如果可用)。


&emsp;&emsp;以上内容翻译整理自 Python 官方文档 [16.6. logging — Logging facility for Python — Python 3.6.8 documentation](https://docs.python.org/3.6/library/logging.html?highlight=logging#module-logging)
