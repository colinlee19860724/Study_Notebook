**4_内置结构-元组-字符串-bytes-bytearray-切片**

---

[TOC]

---


# 1. 元组概念
&emsp;&emsp;__元组__（类型为 `tuple`）和列表十分相似，但是元组和字符串一样是不可变的。

## 1.1. 元组的特点
- 元组可以存储一系列的值，使用 `小括号` 来定义，是一个 `有序` 的元素的集合。
- 元组内的元素是 `不可变` 的
- 当元组内嵌套列表这种引用类型时，元组的不可变表示的是嵌套的列表其内存地址不会变，当直接操作元组内嵌套的列表时，是可以进行修改的

## 1.2. 元组的定义
__格式：__

```python
tuple()           # 工厂函数，用于创建并返回一个空元组
tuple(iterable)   # 使用可迭代对象的元素，来初始化一个元组
```

例子：

```python
In : t=(1)    # 会认为 () 只是优先级

In : type(t) 
Out: int

In : t=(1,)

In : type(t)
Out: tuple     # tuple 表示元组类型
 
# 引用其他元组
In : a=(1,2,3)

In : t=('123',a)

In : t
Out:('123',(1, 2, 3))
 
# 通过索引只引用某一个值
In : t=('123', a[1])

In : t
Out:('123', 2)

# tuple 接受一个可迭代对象转换为元组
In : tuple(range(1,7,2))
Out:(1, 3, 5)
```

## 1.3. 元组的访问
&emsp;&emsp;元组和列表在内存中的格式是相同的，都是线性顺序结构，所以我们可以像列表一样，使用 `索引访问` 元组的元素，其中元组支持 `正索引` 和 `负索引`，同样不支持索引超界，会提示 `IndexError`。

```python
In : b =(1,2,3)

In : b[1]       
Out: 2

In : b[-1]
Out: 3
```

&emsp;&emsp;当元组内嵌套的是列表这种引用类型时，你可以对列表内的数据进行修改，因为列表是可变的。

```python
In : lst = (1, 2, [1, 2])
In : a = lst * 3

In : a
Out:(1, 2, [1, 2], 1, 2, [1, 2], 1, 2, [1, 2])

In : a[2][0] = 100 # 可以对嵌套的列表进行赋值操作 

In : a
Out:(1, 2, [100, 2], 1, 2, [100, 2], 1, 2, [100, 2])

In : a[3] = 100      # 修改指向的地址是不被允许的     
---------------------------------------------------------------------------
TypeError  Traceback(most recent call last)
<ipython-input-47-2b62bbdeb061> in <module>
----> 1 a[3] = 100

TypeError: 'tuple' object does not support item assignment

```

## 1.4. 元组的查询
&emsp;&emsp;我们通过使用元组的 `index` 方法和 `count` 来获取和统计元组中的元素。

```python
# 返回元组内匹配 value 的第一个元素的 index
T.index(value, [start, [stop]]) --> integer   

# 统计 value 在元组中出现的次数，不存在时，则返回 0
T.count(value) --> integer   
```

> &emsp;&emsp;__注意：t.index 和 t.count 因为要遍历列表所有元素，时间复杂度都是 O(n), 随着列表的元素增加，而效率下降__

```python

In : a=('1','2','3')

In : a.count("4")     # 不存在，返回 0
Out: 0

In : a.count("1")
Out: 1
 
# a.index(value) 用来返回 value 在元组中的索引，如果 value 不在元组中，则会报错。
# 如果有多个，默认返回第一个（可以指定从哪个索引开始查找到某个索引结束，指定范围区间）
In : a=('1','2','3')

In : a.index('1')
Out: 0

In : a.index('3')
Out: 2

In : a=('1','2','3')    

In : a.index('4')     # 不存在，就会报错     
---------------------------------------------------------------------------
ValueError Traceback(most recent call last)
<ipython-input-58-dca64b8e9162> in <module>
----> 1 a.index('4')

ValueError: tuple.index(x): x not in tuple

>>> t1
('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
>>> t1.index('a',5,7)    # 在指定的区间内查找
6
```

# 2. 命名元组
&emsp;&emsp;命名元组是元组的子类，所以它也是无法进行修改的，它的特点是可以针元组的对字段进行命名。  
&emsp;&emsp;Tuple 有一个兄弟，叫 namedtuple。虽然都是 tuple，功能更为强大。对于 namedtuple，你不必再通过索引值进行访问，你可以把它看做一个字典通过名字进行访问，只不过其中的值是不能改变的。  

```python
# 格式：
collections.namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)   
# 返回一个新的元组子类，名为 typename 。
# 这个新的子类用于创建类元组的对象，可以通过域名来获取属性值，同样也可以通过索引和迭代获取值。
```

__常用参数含义__
- `typename`: 一般和命名元组的名称相同。
- `field_names`: 可以是空白字符或逗号分隔的字段的字符串，可以是字段的列表
> &emsp;&emsp;`namedtuple` 存放在 collections 包中，所以需要先进行导入

```python
>>> from collections import namedtuple    
>>> Point = namedtuple('Point', ['x', 'y'])  # 创建一个名为 Point 的命名元组类，其中含有两个字段
>>> p = Point(11, 22)     # 创建一个实例，11 会传递给 x，22 会传递给 y。
>>> p[0] + p[1]    # 可以通过索引访问
33
>>> p.x + p.y      # 也可以通过字段名访问
33
>>> p.x = 33       # 无法修改，将报错 
---------------------------------------------------------------------------
AttributeError    Traceback(most recent call last)
<ipython-input-63-dac7085722b7> in <module>
----> 1 p.x = 33

AttributeError: can't set attribute
```

> &emsp;&emsp;Namedtuple 比普通 tuple 具有更好的可读性，可以使代码更易于维护。同时与字典相比，又更加的轻量和高效。但是有一点需要注意，就是 namedtuple 中的属性都是不可变的。任何尝试改变其属性值的操作都是非法的。

```python
In : from collections import namedtuple

In : Animal = namedtuple('animal', 'name age type')   
# 创建一个名为 Animal 的命名元组类，其中含有 name、age、type 三个字段

In : Tom = Animal(name='Tom', age=33, type='cat')   
# 创建一个实例并根据字段的关键字赋值。

In : Tom
Out: animal(name='Tom', age=33, type='cat')

In : print(Tom)
animal(name='Tom', age=33, type='cat')

In : type(Tom)
Out: __main__.animal

In : Tom.type       # 可以通过字段名访问
Out: 'cat'

In : Tom.age = 3    # 和 tuple 一样，无法修改值，将报错 
---------------------------------------------------------------------------
AttributeError     Traceback (most recent call last)
<ipython-input-9-63d4b4478930> in <module>
----> 1 Tom.age = 3

AttributeError: can't set attribute
```


# 3. 字符串
&emsp;&emsp;字符串是 Python 中比较重要的数据类型，是以单引号 `'` 或双引号 `"` 括起来的任意文本，比如 'abc'，"xyz" 等等。请注意，`''` 或 `""` 本身只是一种表示方式，不是字符串的一部分，因此，字符串 'abc' 只有 a，b，c 这 3 个字符。如果 ' 本身也是一个字符，那就可以用双引号 `""` 括起来，比如 "I'm OK" 包含的字符是 `I，'，m，空格，O，K` 这 6 个字符。有三种方法定义字符串：` 单引号 `，` 双引号 `，` 三引号 `，需要注意的是字符串是不可变对象，并且从 Python3 起，字符串就是`Unicode` 类型。   
&emsp;&emsp;__定义方式：__

```python
str1='this is string'
str2="this is string"

# 也可以是三个双引号，三个引号可以多行注释但是不能单双混合，
# 三重引号除了能定义字符串以外，还可以表示注释。
str3='''this is string'''   

# 在 print 打印字符串的时候 \n 会被当作换行符进行打印
str4='hello\n world'    

# 前面使用了 r 对字符串进行整体转义，所见即所得
str5=r'hello\n world'   

# 当然使用 \ 也可以对特殊符号进行脱义
str6='hellow\\nworld'   

# R 和 r 相同
str7=R'hello\nworld'    
```

## 3.1. 字符串的基本操作
&emsp;&emsp;Python 的字符串是一个有序序列，所以他可以和列表一样使用下标来访问元素，但是由于它是不可变类型，所以无法对字符串中的某个字符进行修改，下面介绍下字符串的基本操作。
> &emsp;&emsp;单个字符并没有特殊的类型，Python 中没有字符的概念，严格来讲，说字符是不准确的，字符串是由一个个长度为一的字符串组成的，虽然听起来很别扭，但真的就是这样!
### 3.1.1. 字符串的访问
&emsp;&emsp;字符串和列表相似，都是顺序的线性结构，所以它可以被索引，也可以被遍历。字符串的索引类似数组的下标：

```python
In : a = '1234567'

In : a[0] # 下标从 0 开始，0 表示第一个数
Out: '1'

In : a[3] # 表示第四个数
Out: '4'

In : a[1] = 100   # 字符串无法修改  
---------------------------------------------------------------------------
TypeError  Traceback(most recent call last)
<ipython-input-3-8554a2b011c3> in <module>
----> 1 a[1] = 100

TypeError: 'str' object does not support item assignment

In : for i in a:       # 可以被 for 循环进行迭代
   ...:     print(i) 
   ...:     
1
2
3
4
5
6
7

In : list(a)    # 可以被当作一个可迭代对象传给 list，转换为一个列表
Out: ['1', '2', '3', '4', '5', '6', '7']
```

### 3.1.2. 字符串的拼接
&emsp;&emsp;当我们需要把多个字符串连接在一起，那么就需要对字符串进行拼接，python 提供了 `join` 方法，`+` 号，以及 `*` 号，使我们方便的完成需求。

```python
# 使用 join 对可迭代对象进行拼接，以 str 做为分隔符，返回拼接后的字符串。
str.join(iterable) --> str   
```

- `join`：str 可以为任意字符，包括空。可迭代对象中的元素必须是`字符串`类型
- `+`：把两个字符串直接进行连接，返回一个新的字符串
- `*`：把字符串重复复制 N 次，返回一个新的字符串

```python
In : str1 
Out: ['h', 'e', 'l', 'l', 'o']

In : ''.join(str1)
Out: 'hello'

In : str2 = ''.join(str1)  

In : str2 
Out: 'hello'

In : '-'.join(str1)      # 使用 - 进行拼接   
Out: 'h-e-l-l-o'

In : str2 * 2     
Out: 'hellohello'

In : str2 + str2  
Out: 'hellohello'

In : lst = [['1','2'], '1', '3']

In : ''.join(lst)  # lst 的第 0 个元素是列表，不是字符串，无法拼接，会报错
---------------------------------------------------------------------------
TypeError  Traceback(most recent call last)
<ipython-input-19-58ac5d2512ec> in <module>
----> 1 ''.join(lst)

TypeError: sequence item 0: expected str instance, list found
```

> &emsp;&emsp;**和 `+` 相比，用 `join` 进行字符串的拼接效率最高。**  
> &emsp;&emsp;因为字符串对象是不可改变的，也就是说在 Python 创建一个字符串后，你不能把这个字符中的某一部分改变。任何操作函数改变了字符串后，都会返回一个新的字符串，原字串并没有变。  
> &emsp;&emsp;所以任何对字符串的操作包括 `+` 操作符都将创建一个新的字符串对象，而不是改变原来的对象.因此 N 个字符串相加必将丢弃中间 N-1 个结果，而列表不同，列表是可以改变的，因此前面使用 list 的 append，再使用 join 还原成字符串，只内建了一次，节省了很多资源和时间。  
> &emsp;&emsp;字符串不可改变的现象其实这也是有变通的办法的，可以用 `S=list(S)` 这个函数把 S 变为由单个字符为成员的 list，这样的话就可以使用 `S[3]='a'` 的方式改变值，然后再使用 `S=''.join(S)` 还原成字符串。  

## 3.2. 字符串分割
&emsp;&emsp;字符串中有关于字符分割功能的主要有两类，`split` 系和 `partition` 系，他们分别适用于不用的场景。但用的比较多的是 `split`。
- `split` 系：将字符串按照分割符分隔成若干字符串，并返回列表
- `partition` 系：将字符串按照分割符分割成 2 段，返回这 2 段和分隔符组成的三元组

```python
# 从左至右对字符串 str 进行切割，分割符为 sep，默认为尽可能多的空字符，
# maxsplit 表示分割几次，默认为 -1，全部进行分割，返回一个切割后的列表。
str.split(sep=None, maxsplit=-1) --> list of strings   

# 从左至右对字符串 str 进行切割，必须指定一个分割符 sep，返回一个三元组，
# 其中中间的元素为分割符，第一个和最后一个元素为按照分隔符分开后的前后两个元素。
# 当分隔符无法对字符串进行分割时，返回的是（字符串，空，空）组成的三元组。
str.partition(sep) --> (head, sep, tail)   

# 例子：
In : s = "hello world I am Colin"

In : s.split()         # 默认使用空格进行分割      
Out: ['hello', 'world', 'I', 'am', 'Colin']

In : s.split('o')      # 使用字母 o 进行分割
Out: ['hell', ' w', 'rld I am C', 'lin']   

In : s.split('o',1)    # 使用字母 o 进行分割，并且只分割 1 次    
Out: ['hell', ' world I am Colin']

In : s.split(sep='o',maxsplit=1)    # 也可以用关键字进行传参
Out: ['hell', ' world I am Colin']

In : s.partition(' ')  # 使用 ' ' 进行分割，返回三元组
Out:('hello', ' ', 'world I am Colin')

In : s.partition('o')  # 用字母 o 进行分割，返回一个三元组
Out:('hell', 'o', ' world I am Colin')

# --------------------------------------------------------------
In : s = "helloworldIamColin"   # 当分割符不存在时

# 一定会返回一个列表，如果没有被切分，那么会返回只有一个元素的列表
In : s.split()     
Out: ['helloworldIamColin']

# 一定会返回一个三元组，如果没有被切分，那么会从字符串的最右边切开，
# 形成一个三元组，和一个空字符组成的列表
In : s.partition(' ') 
Out:('helloworldIamColin', '', '')

In : s.partition('12')
Out:('helloworldIamColin', '', '')
```

&emsp;&emsp;当然 split 类还包含了其他两个方法：

```python
# 功能与 split 相同，只不过从右往左切分
str.rsplit(sep=None, maxsplit=-1) --> list of strings   

# 按照行来切分，keepends 表示是否保留换行符，True 表示保留，False 表示不保留，默认为 False
str.splitlines([keepends]) --> list of strings    

# 例子：
In : s = 'I am struper Man' 

# 不指定分割次数，一般和 split 是一样的效果
In : s.rsplit('a')     
Out: ['I ', 'm struper M', 'n']

 #  当指分割 1 次时，会从右边开始切分
In : s.rsplit(sep='a',maxsplit=1)           
Out: ['I am struper M', 'n']

In : s = 'hello\nworld\rI\nam\r\nColin'     

In : print(s)
hello
Iorld
am
Colin

In : s.splitlines() # 默认不保留分隔符
Out: ['hello', 'world', 'I', 'am', 'Colin']

In : s.splitlines(True)     # True 表示保留分隔符
Out: ['hello\n', 'world\r', 'I\n', 'am\r\n', 'Colin']
```

&emsp;&emsp;partition 和 split 相似，也有个`rpartition`函数，也是从右开始截取，需要注意的是，当分隔符无法对字符切分时，返回的是（`空`，`空`，`字符串`）组成的三元组。

## 3.3. 字符串大小写
- `upper`：将字符串转换为大写字母
- `lower`：将字符串转换为小写字母
- `swapcase`：大小写相互掉换
- `capitalize`：转换成首字母大写的单词格式
- `title`：转换成每个单词首字母大写的标题模式

```python
In : s = 'hElLo wORld i aM Colin'

In : s.upper()    
Out: 'HELLO WORLD I AM Colin'

In : s.lower()    
Out: 'hello world i am Colin'

In : s.swapcase() 
Out: 'HeLlO WorLD I Am Colin'

In : s.capitalize()       
Out: 'Hello world i am colin'

In : s.title()    
Out: 'Hello World I Am Colin'    
```

## 3.4. 字符串排版
- `center(width [,fillchar])`：居中显示，参数 width 表示整体宽度，fillchar 表示填充字符，默认填充字符为空格
- `ljust(width [, fillchar])`：左对齐，width 表示整体宽度，fillchar 表示填充字符，默认填充字符为空格
- `rjust(width [, fillchar])`：右对齐，width 表示整体宽度，fillchar 表示填充字符，默认填充字符为空格
- `zfill(width)`：居右显示，参数 width 表示整体宽度，左边用 0 进行填充

```python
In : a   
Out: 'abc'

In : a.ljust(20,'-')      
Out: 'abc-----------------'

In : a.rjust(20,'-')      
Out: '-----------------abc'

In : a.center(30,'-')     
Out: '-------------abc--------------' 

In : a.zfill(20)
Out: '00000000000000000abc'
```

## 3.5. 字符串修改
&emsp;&emsp;前面说字符串是不可变的，为什么这里又说字符串的修改？请继续往下看

```python
# 对字符串 str 进行查找，将指定的 old 字符串转换为 new 字符串，
# count 表示替换的次数，默认表示重复替换所有
str.replace(old, new [, count]) --> str   

# 从字符串 str 两端去除指定的字符集 chars 中的所有字符，
# chars 默认是所有空白字符(\n,\r\n,\r,\t 等等都包含)
str.strip([chars]) --> str

str.lstrip([chars]) --> str    # 从左开始

str.rstrip([chars]) --> str    # 从右开始
```

> 注意：replace 的替换是**生成一个新的字符串**, 而**不是就地修改原字符串**，这也是字符串修改的原理

```python
In : s = ' \n\t Hello World \n\r' 

# ' 不指定 chars，默认是任意多个空白字符
In : s.strip()     
Out: 'Hello World'

# 如果指定了 chars，那么就挨个使用 char 进行匹配去除
In : s.strip(' \n\tHd')   
Out: 'ello World \n\r'

In : s.strip(' \n\rHd')    
Out: '\t Hello Worl'

In : s.replace('World', 'Colin')
Out: ' \n\t Hello Colin \n\r' 

# 默认从头到尾进行替换
In : s.replace('o', 'O') 
Out: ' \n\t HellO WOrld \n\r'

# 指定替换 1 次      
In : s.replace('o', 'O', 1) 
Out: ' \n\t HellO World \n\r'  
```

## 3.6. 字符串查找
&emsp;&emsp;我们有很多的时候要判断关键字是否存在一个字符串中，那么我们就需要在字符串中 `遍历` 查找，是否有匹配的字符串。python 提供了 `find`、`rfind`、`index`、`count` 等函数用于完成需求。

```python
# 在指定的区间[start, end)，从左至右，查找子串 sub 。
#  找到返回索引，没找到返回 -1
str.find(sub [, start [, end]]) --> int 

# 在指定的区间[start, end)，从右至左，查找子串 sub 。
# 找到返回索引，没找到返回 -1
str.rfind(sub [, start [, end]]) --> int  

# 在指定的区间[start, end)，从左至右，查找子串 sub 。
# 找到返回索引，没找到抛出异常 ValueError
str.index(sub [, start [, end]]) --> int  

# 在指定的区间[start, end)，从右至左，查找子串 sub 。
# 找到返回索引，没找到抛出异常 ValueError
str.rindex(sub[, start[, end]]) --> int  

# 在指定的区间[start, end)，从左至右，统计子串 sub 出现的次数，
# 默认为整个字符串。没有找到返回 0
str.count(sub [, start [, end]]) --> int  
```

&emsp;&emsp;find 、index 和 count 方法由于是遍历查找，所以时间复杂度都是 O(n), 会随着字符串序列的数据规模的增大，而效率下降。

```python

In : s = 'abc abc abc'    

In : s.find('a')  
Out: 0

# 指定区间，注意这里 -1 表示最后 1 位，但是不包含 -1，类似于 [1,-1)
In : s.find('a',1,-1)   
Out: 4

# end 超出范围，没找到返回 -1
In : s.find('a',-1,-15)   
Out: -1

In : s.rfind('a') 
Out: 8

In : s.rfind('a', 2, -1)    
Out: 8  
  
In : s.rfind('c', 2, -1)    
Out: 6  

# end 超出范围，没找到返回 -1，start，end 表示起始和终止，
# 最好不要使用负数表示区间
In : s.rfind('c', 2, -100)    
Out: -1  

In : s.index('a') 
Out: 0

# 从索引 2 至最右边，从右往左查找  
In : s.rindex('a', 2)     
Out: 4

# 没找到，直接报异常
In : s.index('e') 
---------------------------------------------------------------------------
ValueError Traceback(most recent call last)
<ipython-input-25-90b1c28da6f0> in <module>
----> 1 s.index('e')

ValueError: substring not found

In : s.count('a')
Out: 3
```

## 3.7. 字符串判断
&emsp;&emsp;Python 的字符串对象提供了两个函数，用于对字符串的起始位和结尾位来进行匹配，它们是 `startswith` 和 `endswith`。

```python
# 在指定的区间[start, end)，字符串是否是 prefix 开头，
# 默认为 0，即整个字符串 str, 返回 bool 类型。
str.startswith(prefix [, start [, end]]) --> bool       

# 在指定的区间[start, end)，字符串是否是 suffix 结尾，
# 默认为 0，即整个字符串 str, 返回 bool 类型。
str.endswith(suffix [, start [, end]]) --> bool 
```

&emsp;&emsp;例子：
```python
In : s    
Out: 'abc abc abc'

# 从 s 的 [1,-1) 开始判断 'bc' 是否是开头
In : s.startswith('bc',1,-1)    
Out: True

# 从 s 的 [2,-1) 开始匹配 'bc' 是否是结尾
# 这里 -1 不包含，所以返回 False
In : s.endswith('bc',2,-1)     
Out: False     

In : s.endswith('bc',3,7) 
Out: True

In : s.startswith('abc')  
Out: True

In : s.endswith('bc')     
Out: True 
```

&emsp;&emsp;除了判断开始和结尾，Python 的字符串还提供了部分函数，用来判断字符串内的元素类型，比如判断字符串是否是纯数字组成？是否是纯字母组成等，这些函数的返回值统一都为`bool`型，可以作为`if 语句的条件表达式 `。

```python
str.isalpha()      # 是否是字母
str.isalnum()      # 是否是字母和数字组成
str.isdigit()      # 是否全是十进制数字，int
str.isdecimal()    # 判断是否是数字类型，包含 float，但不包含负数
str.islower()      # 判断字符串是否全是小写字母
str.isupper()      # 判断字符串是否全是大写字母
str.isspace()      # 是否是空白字符
str.isnumberic()   # 判断是否是正整数
str.isidentifier() # 是否是一个合规的变量标识符
```

## 3.8. 字符串格式化
&emsp;&emsp;字符串格式化是我们需要重点掌握的东西，在早期的 Python 中使用的是 C 语言风格的字符串替换，使用起来比较难看，不符合 python 的风格（纯属笔者猜测）。后来 Python 推荐使用内置的 `format` 函数来对字符串进行格式化。  
&emsp;&emsp;字符串格式化是一种拼接字符串输出样式的手段，更灵活方便，之前我们使用 `join` 和 `+` 来对字符串进行拼接。
- `join`：只能使用分隔符，且要求被拼接的是可迭代对象且元素必须是字符串类型
- `+`：使用起来比较方便，但是非字符串需要先转换为字符串类型才可以进行拼接。  

### 3.8.1. C 语言格式化
&emsp;&emsp;在 Python 2.5 版本以前，只能使用 `printf-style formatting` 风格的 print 输出，这种风格来自于 C 语言的 printf 函数，它有如下格式要求。(__建议使用 format__)  
1. 占位符：使用 `% 和格式字符串`组成，例如 `%s`，`%d` 等。s 调用 `str()` ，r 会调用 `repr()`。所有对象都可以被这两个转换
2. 占位符中还可以插入修饰字符，例如 `%03d` 表示打印 3 个位置，不够的话，前面补 0
3. `format % value` 格式字符串和被格式字符串之间使用 % 分割
4. `values` 只能是一个对象，或是一个与格式字符串占位符数量相等的元组，或一个字典

```python
In : 'I am %03d' % 20  # 表示 3 为数字，不够的话高位补 0
Out: 'I am 020'

In : 'I like %s' % 'Python'      # 字符串格式化
Out: 'I like Python'

In : 'I am %s' % 20      # 20 会被 str 作用后，传递给字符串 
Out: 'I am 20'

# 3.2f 表示最长 3 为，小数点后精度为 2 位，当数字大时整体长度会被撑开，
# x 表示 16 进制，02X 表示两位显示，高位补 0
In : '%3.2f%%,0x%x,0X%02X' % (89.7654, 10, 15)     
Out: '89.77%,0xa,0X0F'

In : "I am %-5d" % 20     
Out: 'I am 20   '

In : "I am %5d" % 20      
Out: 'I am    20'
```

### 3.8.2. format 格式化
&emsp;&emsp;Python 中推崇使用 `format()` 函数来对字符串进行格式化。

```python
# 函数的一般格式，{} 表示占位符，使用 format 中的参数进行传递
'{}{XXX}'.format(*args, **kwargs)  --> str   
```

&emsp;&emsp;format 非常灵活，下面是基本使用方法说明：
1. `args` 是可变位置参数，是一个元组
2. `kwargs` 是可变关键字参数，是一个字典
3. `花括号` 表示 `占位符`
4. `{}` 表示按照顺序匹配 `位置参数`，`{n}` 表示取位置参数中 `索引为 n 的值`
5. `{xxx}` 表示在关键字参数中搜索名称一致的值，`kwargs` 必须放在 `可变位置参数的后面`
6. `{{}}` 表示打印花括号

```python
# 按照位置格式化，第一个元素给第一个括号，第二个元素给第二个括号      
In : '{}:{}'.format('10.0.0.13','8888')       
Out: '10.0.0.13:8888'    # 

# 命名格式化，host 表示只获取关键字为 host 的值来填充，
# 其他没有指定关键字的占位符，则按照位置参数进行传递，并格式化显示     
In : '{host}:{}:{}'.format('10.0.0.13','8888',host='Colin')   
Out: 'Colin:10.0.0.13:8888'

# 访问元素的方式进行字符串格式化(不常用)
In : '{0[0]}:{0[1]}'.format(['10.0.0.13','8888'])   
Out: '10.0.0.13:8888'

# 由于 p 对象含有 x 和 y 属性，所以可以在字符串格式化时直接引用
In : from collections import namedtuple     
In : Point = namedtuple('_Point',['x','y']) 
In : p = Point(4,5)       
In : print('{' + '{0.x},{0.y}'.format(p) + '}')   
Out: '{4,5}'
```

### 3.8.3. 对齐
&emsp;&emsp;字符串还提供了多种的对齐方式，便于我们对输出内容做一个简单的优化。
- `<`：左对齐（默认）
- `>`：右对齐
- `^`: 居中对齐  
> &emsp;&emsp;对齐方式需要在占位符内使用 `：号` 进行分割

```python
#   打印字符串，这个字符串占 5 位，默认靠左对齐，其他位使用空格填充
In : '{:5}'.format('c')     
Out: 'c    '

# > 表示右对齐
In : '{:>5}'.format('c')       
Out: '    c'

# 字符串站 5 位，左对齐，其他位使用 0 填充(可以简写为 '{:<05}')
In : '{:0<5}'.format('c')     
Out: 'c0000'

In : '{:0>5}'.format('c')
Out: '0000c'

# > 表示右对齐，其他位用 * 填充
In : '{:*>5}'.format('c')     
Out: '****c'

# 居中对齐，其它位使用 0 进行填充 
In : '{:0^5}'.format('c')     
Out: '00c00'

# 居中对齐，其它位使用 * 进行填充
In : '{:*^5}'.format('c')
Out: '**c**'
```

> &emsp;&emsp;当填充符为数字的时候，可以与宽度写在一起，比如 `'{:0<5}'.format('3')` 可以写成 `'{:<05}'.format('3')`，而 ` '{:0^5}'.format('3')` 可以写成 ` '{:^05}'.format('3')`


### 3.8.4. 浮点数与进制
&emsp;&emsp;虽然用的不多，还是这里还是举例说明一下进制和浮点数的使用方法（注意宽度可以被撑破）

- `d`: 表示十进制
- `x`: 表示十六进制
- `o`: 表示八进制
- `b`: 表示二进制
- `F`: 表示浮点型
- `#`: 表示添加进制前缀
- `*[1,2,3]`: 表示把列表中的元素解构出来：`*[1,2,3]` --> `1,2,3`

```python
# 输出时转换进制
In : "int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(42)
Out: 'int: 42; hex: 2a; oct: 52; bin: 101010'

# 加上进制前缀
In : "int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(42)
Out: 'int: 42; hex: 0x2a; oct: 0o52; bin: 0b101010'

In : octets = [10,0,0,13]      

In : '{:02X}{:02X}{:02X}{:02X}'.format(*octets) 
Out: '0A00000D'

In : '{:02X}-{:02X}-{:02X}-{:02X}'.format(*octets)      
Out: '0A-00-00-0D'  
 
# ----------------------------------------------------------
In : "{}".format(3**0.4)# 默认按照字符串打印 
Out: '1.5518455739153598' 
 
# f 表示填充位为小数，小数是有精度的
In : "{:f}".format(1.5518455739153598)     
Out: '1.551846' 
 
# 表示小数的长度为 2，但是如果小数的位数超过 2，会直接撑开   
In : "{:02f}".format(1.5518455739153598)    
Out: '1.551846' 

# 表示小数的长度为 10，默认是右对齐 
In : "{:10f}".format(1.5518455739153598)    
Out: '  1.551846' 
 
# 左对齐 
In : "{:<10f}".format(1.5518455739153598)   
Out: '1.551846  ' 
 
# .2f 表示小数点后取两位的浮点型 
In : "{:.2f}".format(1.5518455739153598)    
Out: '1.55' 
 
# 总长 3 位，小数点后保留 2 位，若整数位长度超出，则撑开 
In : "{:3.2f}".format(123456.123456)   
Out: '123456.12' 
 
# 使用百分比显示
In : "{:2.2%}".format(1.5518455739153598)   
Out: '155.18%'
```

# 4. bytes、bytearray
&emsp;&emsp;Python3 引入两个新类型：
1. bytes：不可变字节序列
2. bytearray：字节数组，可变

__字符串与 bytes__
- 字符串是字符组成的有序序列，字符可以使用编码来理解
- bytes 是字节组成的有序的不可变序列
- bytearray 是字节组成的有序的可变序列

__编码与解码__
- 字符串按照不同的字符集编码 encode 返回字节序列 bytes
  - `str.encode(encoding='utf-8', errors='strict') --> bytes`
- 字节序列按照不同的字符集解码decode返回字符串
  - `bytes.decode(encoding="utf-8", errors="strict") --> str`
  - `bytearray.decode(encoding="utf-8", errors="strict") --> str`

```python
In : '李'.encode()
Out: b'\xe6\x9d\x8e'

In : b'\xe6\x9d\x8e'.decode()
Out: '李'

In : b"\x41\x61".decode()
Out: 'Aa'

# bytearray 和 bytes 不一样的地方在于，bytearray 是可变的。
In : str1 = '人生苦短，Python当歌'

In : b1 = bytearray(str1.encode())

In : b1
Out: bytearray(b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa6\xe7\x9f\xad\xef\xbc\x8cPython\xe5\xbd\x93\xe6\xad\x8c')

In : type(b1)
Out: bytearray

In : b1.decode()
Out: '人生苦短，Python当歌'

In : b1[:6] = bytearray('生命'.encode())

In : b1
Out: bytearray(b'\xe7\x94\x9f\xe5\x91\xbd\xe8\x8b\xa6\xe7\x9f\xad\xef\xbc\x8cPython\xe5\xbd\x93\xe6\xad\x8c')

In : b1.decode()
Out: '生命苦短，Python当歌'
```
## 4.1. ASCII
&emsp;&emsp;ASCII（American Standard Code for Information Interchange，美国信息交换标准代码）是基于拉丁字母的一套单字节编码系统，编码范围从 0 到 127  

**熟记常用字符的 ASCII 码**

| Char |Decimal（十进制）|Hex（十六进制） |
| :---:|:---:|:---: |
| `\t` 水平制表符 | 9 | 09 |
| `\n` 换行符 | 10 | 0A |
| `\v` 垂直制表符 | 11 | 0B |
| `\f` 换页符 | 12 | 0C |
| `\r` 回车符 | 13 | 0D |
| `(space)` 空格 | 32 | 20 |
| `0~9` | 48~57 | 30~39 |
| `A-Z` | 65~90 | 41~5A |
| `a-z` | 97~122 | 61~7A |

## 4.2. bytes 定义
- `bytes()` 空 bytes
- `bytes(int)` 指定字节的 bytes，被 0 填充
-` bytes(iterable_of_ints) --> bytes` （ 由[0,255] 的 int 组成的可迭代对象 ）
- `bytes(string, encoding[, errors]) --> bytes` （ 等价于 string.encode() ）
- `bytes(bytes_or_buffer) --> immutable copy of bytes_or_buffer` （从一个字节序列或者 buffer 复制出一个新的不可变的 bytes 对象）
- 使用 b 前缀定义
  - 只允许基本 ASCII 使用字符形式 b'abc9'
  - 使用 16 进制表示 b"\x41\x61"
```python
In : bytes()
Out: b''

In : bytes(5)
Out: b'\x00\x00\x00\x00\x00'

In : bytes(range(3))
Out: b'\x00\x01\x02'
```
## 4.3. bytes 操作
- 和 str 类型类似，都是不可变类型，所以方法很多都一样。只不过 bytes 的方法，输入是 bytes ，输出是 bytes

```python
In : b'abcdef'.replace(b'f',b'k')
Out: b'abcdek'

In : b'abc'.find(b'b')
Out: 1
```

- 类方法 `bytes.fromhex(string)`：string 必须是 2 个字符的 16 进制的形式，'6162 6a 6b'，空格将被忽略

```python
In : bytes.fromhex('6162 09 6a 6b00')
Out: b'ab\tjk\x00'
```
- hex()：返回16进制表示的字符串

```python
In : 'abc'.encode().hex()
Out: '616263'
```

- 索引：b'abcdef'[2] 返回该字节对应的数，int类型
```python
In : b'abcdef'[2]
Out: 99
```

## 4.4. bytearray 定义

- `bytearray()` 空 bytearray
- `bytearray(int)` 指定字节的 bytearray，被 0 填充
- `bytearray(iterable_of_ints) --> bytearray` （[0,255]的 int 组成的可迭代对象）
- `bytearray(string, encoding[, errors]) --> bytearray` （近似 string.encode()，不过返回可变对象）
- `bytearray(bytes_or_buffer)` 从一个字节序列或者 buffer 复制出一个新的可变的 bytearray 对象
- 注意，b 前缀定义的类型是 bytes 类型

```python
In : bytearray()
Out: bytearray(b'')

In : bytearray(6)
Out: bytearray(b'\x00\x00\x00\x00\x00\x00')

In : bytearray(range(3))
Out: bytearray(b'\x00\x01\x02')
```

## 4.5. bytearray 操作
- 和 bytes 类型的方法相同

```python
In : bytearray(b'abcdef').replace(b'f',b'k')
Out: bytearray(b'abcdek')

In : bytearray(b'abc').find(b'b')
Out: 1
```

- 类方法 `bytearray.fromhex(string)`：string 必须是 2 个字符的 16 进制的形式，'6162 6a 6b'，空格将被忽略

```python
In : bytearray.fromhex('6162 09 6a 6b00')
Out: bytearray(b'ab\tjk\x00')
```
- hex()：返回 16 进制表示的字符串

```python
In : bytearray('abc'.encode()).hex()
Out: '616263'
```

- 索引：`bytearray(b'abcdef')[2]` 返回该字节对应的数，int类型
- `append(int)` 尾部追加一个元素
- `insert(index, int)` 在指定索引位置插入元素
- `extend(iterable_of_ints)` 将一个可迭代的整数集合追加到当前 bytearray
- `pop(index=-1)` 从指定索引上移除元素，默认从尾部移除
- `remove(value)` 找到第一个 value 移除，找不到抛 ValueError 异常
- 注意：上述方法若需要使用 int 类型，值在 [0, 255]
- `clear()` 清空 bytearray
- `reverse()` 翻转 bytearray，就地修改

```python
In : bytearray(b'abcdef')[2]
Out: 99

In : b = bytearray()

In : b.append(97)

In : b.append(99)

In : b.insert(1,98)

In : b.extend([65,66,67])

In : print(b)
bytearray(b'abcABC')

In : b.remove(66)

In : print(b)
bytearray(b'abcAC')

In : b.pop()
Out: 67

In : print(b)
bytearray(b'abcA')

In : b.reverse()

In : print(b)
bytearray(b'Acba')

In : b.clear()

In : print(b)
bytearray(b'')
```

## 4.6. 字节序
- 大端模式，big-endian；小端模式，little-endian
- Intel X86 CPU使用小端模式
- 网络传输更多使用大端模式
- Windows、Linux使用小端模式
- Mac OS使用大端模式
- Java虚拟机是大端模式

![LSB_MSB](../Photo/LSB_MSB.png)

> &emsp;&emsp;C2 认为是尾巴。尾巴放在低地址端，就是`小端模式` `LSB:Least Significant Bit`，最低有效位；尾巴放在大地址端，就是`大端模式` `MSB:Most Significant Bit`，最高有效位。

## 4.7. int 和 bytes
- `int.from_bytes(bytes, byteorder)`
  - 将一个字节数组表示成整数
- `int.to_bytes(length, byteorder)`
  - byteorder 字节序
  - 将一个整数表达成一个指定长度的字节数组

```python
In : i = int.from_bytes(b'abc', 'big')

In : print(i, hex(i))
6382179 0x616263

In : print(i.to_bytes(3, 'big'))
b'abc'

In : b1 = bytearray()

In : b1.append(97)

In : b1
Out: bytearray(b'a')

In : b1.extend(range(98, 100))

In : b1
Out: bytearray(b'abc')
```

# 5. 切片
&emsp;&emsp;列表、元组、字符串、bytes、bytearray 都属于线性结构，线性结构其他的特点还有：
- 可迭代 (for ... in)
- len() 可以获取长度
- 可以通过下标进行访问(有序)
- 都可以被切片

&emsp;&emsp;那什么是切片？我们说通过索引区间访问线性结构一段数据的方法就叫做切片，需要注意的是**切片操作会引起内存复制，当对一个过于庞大的线性结构进行切片的时候，请慎重考虑内存使用率的问题**。切片的表达方式和基本特点有：
1. 格式：`sequence[start:stop:[,step=1]]` 返回 `[start, stop, step=1)` 的**前闭后开**子序列。
2. 支持负索引。注意方向问题
3. 当 start 为开头（为 0 ） 或 stop 为末尾（注意和 -1 的区别）时，可以省略。`[:]` 表示复制原线性结构数据，等效于 `copy()` 方法（注意当对象为 list 时，属于 `浅 copy`）
4. 超过上界(右边界)，则取到末尾；超过下界(左边界)，则取到开头。
5. start 一定要在 stop 的左边

```python
In : a = 'hello world , My name is Colin'
In : a[2:-1]   
Out: 'llo world , My name is Coli'

In : a[2:]       
Out: 'llo world , My name is Colin'

In : a[-100:]    
Out: 'hello world , My name is Colin'

# stop 位置在 start 左边，所以没办法取出，如果实在想要倒着取，那么需要使用负步长
In : a[10:-100]      
Out: '' 

# 负步长就可以形成开闭区间，注意是从起始位开始按照 step 取的(所以会倒序排列返回) 
In : a[10:-100:-1]   
Out: 'dlrow olleh'

# 列表类型，步长为 2
In : list('My Name is ColinLee')[4:20:2]         
Out: ['a', 'e', 'i', ' ', 'o', 'i', 'L', 'e']

# 元组类型，步长为 2
In : tuple('My Name is ColinLee')[4:20:2]        
Out: ('a', 'e', 'i', ' ', 'o', 'i', 'L', 'e')
```

__注意：__
- 切片并不会对原数据进行修改，会返回新的数据
- 如果不是用变量接受，那么就会被标记为待回收
- 由于是新生成的数据，所以 `内存地址` 和原数据内存地址 `一定不相同`。

## 5.1. 切片赋值
&emsp;&emsp;既然可以进行切片，那么就会引申出来，是否可以进行切片赋值，什么是切片赋值？它该如何表示？下面以列表例进行说明。  
- 切片操作写在等号的左边
- 被插入的可迭代对象在等号右边

```python
In : lst = list(range(10))
In : lst 
Out: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In : lst[1:3]   
Out: [1, 2]

# 只能使用可迭代对象进行赋值
In : lst[1:3] = 1       
---------------------------------------------------------------------------
TypeError  Traceback(most recent call last)
<ipython-input-82-7fef59136c7e> in <module>
----> 1 lst[1:3] = 1

TypeError: can only assign an iterable


In : lst[1:3] = [100,200]

In : lst 
Out: [0, 100, 200, 3, 4, 5, 6, 7, 8, 9]  

In : a
Out: [0, 4]

In : b = list()

In : b[:] = a

In : b
Out: [0, 4]

In : c = a

In : print(id(a), id(b), id(c))
1935299790344 1935291542600 1935299790344
```

仔细看上面示例代码会发现几个问题：
1. lst[1:3] = 1 切片赋值会失败，因为 `切片赋值` 赋的值必须是 `一个可迭代对象`
2. 切片赋值改变了原数据
3. 字符串、元组这类不可变的元素，无法使用切片赋值

> &emsp;&emsp;当我们使用切片时，它会产生新的内存地址来存放生成的新列表，但是如果把切片操作放在赋值操作的左边时，那么就相当于引用了原列表的 `[start:stop]` 的索引，这种操作是不会生成新的内存空间的，换句话来讲就是直接对原列表进行了 `list.insert` 操作.

```python
In : lst 
Out: [0, 100, 200, 3, 4, 5, 6, 7, 8, 9]

 # 这种操作相当于在 [1:3) 的位置上进行了 list.remove
In : lst[1:3] = []         

In : lst 
Out: [0, 3, 4, 5, 6, 7, 8, 9]

# 这种操作相当于在 [1:3) 的位置上进行了 list.insert
In : lst[1:3] = [100,200]   

In : lst 
Out: [0, 100, 200, 5, 6, 7, 8, 9]
```

> &emsp;&emsp;我们知道 list 在进行 insert 和 remove 时的时间复杂度都是 O(n)，在进行切片赋值时的时间复杂度也是一样，所以建议不要使用这种方法。