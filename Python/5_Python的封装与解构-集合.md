
- [1. 封装与解构](#1-封装与解构)
    - [1.1. 封装](#11-封装)
    - [1.2. 解构](#12-解构)
    - [1.3. Python3 的解构](#13-python3-的解构)
- [2. set 类型](#2-set-类型)
    - [2.1. set 的定义](#21-set-的定义)
    - [2.2. set 的基本操作](#22-set-的基本操作)
        - [2.2.1. 增加元素](#221-增加元素)
        - [2.2.2. 删除元素](#222-删除元素)
        - [2.2.3. 修改元素](#223-修改元素)
        - [2.2.4. 成员判断](#224-成员判断)
    - [2.3. set 和线性结构](#23-set-和线性结构)
- [3. 集合](#3-集合)
    - [3.1. 集合运算](#31-集合运算)
    - [3.2. 并集](#32-并集)
    - [3.3. 交集](#33-交集)
    - [3.4. 差集](#34-差集)
    - [3.5. 对称差集](#35-对称差集)
    - [3.6. 集合的其他运算](#36-集合的其他运算)


# 1. 封装与解构
&emsp;&emsp;封装与解构属于 Python 语言的一种特性，它使用起来很像其他语言中的`"逗号表达式"`，但内部原理是不同的，在某些场景下：比如变量交换、复制时使用，显得非常优雅。

## 1.1. 封装
&emsp;&emsp;封装顾名思义就是装箱，把多个值使用逗号分隔，组合在一起，本质上来看，其返回的是一个元组，只是省略了小括号。(一定要区别于 C 语言的逗号表达式)

```python
In : t1 = (1,2)  # 定义一个元组

In : t2 = 1,2    # 省略括号，其内部还是会封装成元组

In : t1
Out: (1, 2)

In : t2
Out: (1, 2)

In : type(t1)
Out: tuple

In : type(t2)
Out: tuple
```

## 1.2. 解构
&emsp;&emsp;解构，就是把箱子解开，在 Python 中表示从线性结构中把元素解开，并且顺序的赋值给其他变量，需要注意的是，解构时接受元素的变量，需要放在等式的左边，并且数量要和右边待解开的元素的个数一致。  

```python
In : t1
Out: (1, 2)

In : a,b = t1    # 表示把 1 赋给 a，把 2 赋给 b

In : a 
Out: 1

In : b
Out: 2

In : a,b,c = t1   # 当接受元素的变量多于解构的元素时，会提示ValueError，反之相同
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-101-2e8ad53e5fc7> in <module>
----> 1 a,b,c = t1

ValueError: not enough values to unpack (expected 3, got 2)
```

## 1.3. Python3 的解构
&emsp;&emsp;了解了封装与解构，那么回想一下当我们需要进行变量交换的时候，是否可以通过封装与解构进行优化呢？当我们在其他语言中进行 a，b 变量的值的交换，我们需要一个中间变量 temp，即：`temp = a ; a = b ; b = temp`，在 Python 中我们可以省略它。

```python
>>> a = 1
>>> b = 2
>>> a,b = b,a    # 等号右边使用了封装，而左边就使用了解构，这样就完成了变量的交换了，是不是很方便
>>> a
2
>>> b
1
>>> 
```

> &emsp;&emsp;为什么可以使用这种操作，是因为 Python 在进行变量赋值时，会先计算等式右边的表达式，封装起来，然后再进行解构，赋值给对应位置上的变量。   

- `*号`： 使用方式为: `*变量名`，贪婪吸收解构的元素并形成一个列表，__无论能否吸收，都会返回一个列表__。
- `_号`：表示丢弃一个变量(实际上是使用 `_` 做变量名接受不想要的值，但不使用它，相当于把它丢弃，这是一个惯例，是一个不成文的约定，不是标准)

```python
In : t = list(range(5))

In : t  
Out: [0, 1, 2, 3, 4]

In : head,*mid,tail = t

In : head     
Out: 0

In : mid
Out: [1, 2, 3]

In : tail     
Out: 4
```

&emsp;&emsp;需要注意的是：
1. `*变量名` 这种格式不能单独使用
2. 也不能多个 `*变量名` 连续使用（因为从原理上看，两个 `*变量名` 连起来使用，会引起歧义，所以 Python 禁止了这种写法）
3. `*_` 这种格式，可以收集足够多的元素并丢弃之

```python
# 从 [1,(2,3,4),5] 中取出 4 来
>>> _,(*_,a),_ = [1,(2,3,4),5]
>>> a
>>> 4

# 环境变量 JAVA_HOME=/usr/bin/java，返回环境变量名和路径
>>> env, path = 'JAVA_HOME=/usr/bin/java'.split('=')
>>> env, path
>>> ('JAVA_HOME','/usr/bin/java')

# 或者

In : env, _, path = 'JAVA_HOME=/usr/bin/java'.partition('=')

In : env, path
Out: ('JAVA_HOME', '/usr/bin/java')
```

> &emsp;&emsp;解构是 Python 提供的很好的功能，可以方便的提取复杂的数据结构的值，配合 `*` 和 `_` 使用时，会更加便捷。

# 2. set 类型
&emsp;&emsp;集合 set 在 Python 中是一个非常重要的`非线性结构`，它使用 `{}` 表示，用三个词总结集合的特点就是：__可变的__、__无序的__、__不重复__。它的官方解释如下：
- set 是一个无序的，不重复的 `可hash对象` 组成的集。
- 常用来进行成员测试，在一个序列中去掉重复的对象，和进行数学上的计算，比如 `交集(intersection)`、`并集(union)`、`差集(difference)`、`对称差集(symmetric difference)` 等。
- 和其他容器类型相似，在一个无序的集合中支持 `x in set`,`len(set)`,`for x in set` 等操作。
- set 不会记录元素的位置以及元素加入集合的顺序，所以 set 不支持`索引`，`切片`或者其他的类序列的操作。

> &emsp;&emsp;什么是可 hash 对象，可以简单的理解为可以被 `hash()` 计算的对象，在 Python中，可 hash 对象是不可变类型的，比如 tuple, str, int 等等。

## 2.1. set 的定义
&emsp;&emsp;Python提供了两种定义一个集合的方式，`set()` 和 `set(iterable)`，他们的用法如下：

```python
set() ==>> new empty set object     # 返回一个空的set对象
set(iterable) ==>> new set object   # 返回一个set对象，元素由iterable填充
```

例如：

```python
In : s1 = set()

In : s2 = set(range(5))          # {0, 1, 2, 3, 4}

In : s3 = set(list(range(10)))   # 外面使用 list 进行转换，多此一举

In : s3
Out: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

In : s4 = {}                     # 这种方式实际上是创建了一个空字典，而不是集合

In : s4        
Out: {}

In : type(s4)  
Out: dict

In : s5 = {(1,3),3,'a'}

In : s6 = {[1,2],(1,2,),1,2}       # list 属于不可 hash 对象，所以无法添加到 set 中去
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-52-237c72203405> in <module>
----> 1 s6={[1,2],(1,2,),1,2}

TypeError: unhashable type: 'list'
```

## 2.2. set 的基本操作
&emsp;&emsp;set 是可变的类型，那就意味着，我们可以对 set 进行增加、删除、修改等操作。  

### 2.2.1. 增加元素
&emsp;&emsp;set 提供了两种定义一个集合的方式，`add` 和 `update`，他们的用法如下：  

```python
s.add(elem) ==>> None            # 在集合 s 中添加一个元素 elem，如果元素存在，则什么都不做(去重特性)。（就地修改）

s.update(*others) ==>> None   # 把 *others 个可迭代可 hash 对象，和 s 进行并集，然后赋给 s。（就地修改）
```

例如：

```python
In : s = {1, 2, 3}        

In : s.add('abc')       # 把字符串 'abc' 当作一个元素添加进去

In : s
Out: {1, 2, 3, 'abc'}  

In : s.add((1,2,3))     # 把元组 (1,2,3) 当作一个元素添加进去

In : s
Out: {(1, 2, 3), 1, 2, 3, 'abc'}

In : s.update(range(5),'abcdef',[5,6,7,8])     # 合并多个可迭代可 hash 对象到 s 集合中来

In : s
Out: {(1, 2, 3), 0, 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}
```

### 2.2.2. 删除元素
&emsp;&emsp;set 提供了多种删除元素的方式，比如 `remove` ,`pop`，他们的用法如下：

```python
s.remove(elem)  ==>> None   # 在集合 s 中删除一个元素，这个元素必须存在集合 s 中，否则会报 KeyError 异常

s.discard(elem) ==>> None   # 在集合 s 中删除一个元素，如果元素不存在集合中，那么什么也不做

s.pop()  ==>> item     # 在集合 s 中随便弹出一个元素，并返回元素的本身，如果集合本身为空，那么会提示 KeyError 异常

s.clear()  ==>> None   # 清空集合
```

例如：

```python
In : s
Out: {(1, 2, 3), 0, 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}

In : s.remove(0)  

In : s
Out: {(1, 2, 3), 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}

In : s.remove(1000)       # 不存在集合内的元素，删除会报异常   
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-74-9d9da17ab719> in <module>
----> 1 s.remove(1000)

KeyError: 1000

In : s = {(1, 2, 3), 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}

In : s.pop()   
Out: 1

In : s
Out: {(1, 2, 3), 2, 3, 4, 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}

In : s1 = set()

In : s1.pop()      # 空集合会报异常        
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-84-095118de218b> in <module>
----> 1 s1.pop()

KeyError: 'pop from an empty set'

In : s = {(1, 2, 3), 4, 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}

In : s.discard(1000)     # 不会报异常   

In : s.discard(4) 

In : s
Out: {(1, 2, 3), 5, 6, 7, 8, 'a', 'abc', 'b', 'c', 'd', 'e', 'f'}

In : s.clear() 

In : s
Out: set()
```

### 2.2.3. 修改元素
&emsp;&emsp;上来我们需要先想一个问题，为什么要修改 set 呢？修改的本质是什么？
- 修改的本质其实就是找到这个元素，删除，然后再加入新的元素
- 由于集合是非线性结构，所以无法被索引
- 但是 set 是容器，可以被迭代  

> &emsp;&emsp;所以 set 不能像 list 那样，通过索引修改元素，因为它无序的特性，修改其实等同于删除后再添加元素。

### 2.2.4. 成员判断
&emsp;&emsp;我们说既然 set 是容器，那么我们就可以对容器内的元素进行判断，那么就需要使用成员判断符 `in` 和 `not in` 了。
- `in`：`x in s`, 判断元素 x 是否是在集合 s 中，返回 bool 类型
- `not in`：`x not in s`,  判断元素 x 不在集合 s 中，返回 bool 类型

```python
In : s = set(range(20))    

In : s
Out: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

In : 1 in s    
Out: True

In : 10000 not in s        
Out: True
```


## 2.3. set 和线性结构
&emsp;&emsp;在 list，str 这种`线性结构`中进行`成员判断`时，因为需要遍历，线性结构的查询时间复杂度是 `O(n)`，即随着数据规模的增大而增加耗时。  
&emsp;&emsp;而set 等非线性结构，内部使用的是 hash 值作为 key，查询时只需把要判断的元素进行 hash，找到 set 中对应的门牌号，把里面的数据拽出来，看看是不是相同就可以，时间复杂度可以做到 `O(1)`，查询时间和数据规模无关，效率很高。  
&emsp;&emsp;在 Python 中可 hash 对象 __都属于不可变类型__ ，Python 中的可 hash 对象如下：  
- 数值类型 int、float、complex
- 布尔值 True、False
- 字符串 String、Bytes
- 元组 tuple
- None  

# 3. 集合
&emsp;&emsp;简单来说，所谓的一个集合，就是将数个对象归类而分成一个或数个形态各异的大小整体。 一般来讲，__集合__ 是具有某种特性的事物的整体，或是一些确认对象的汇集。构成集合的事物或对象称作 __元素__ 或是 __成员__。集合的元素可以是任何事物，可以是人，可以是物，也可以是字母或数字等。 （此解释来自于维基百科）

- __全集__：所有元素的结合。例如实数集，所有实数组成的集合就是实数集
- __子集 subset 和超集 superset__：一个集合 A 所有的元素都在另一个集合 B 内，A 是 B 的子集，B 是 A 的超集
- __真子集和真超集__：A 是 B 的子集，且 A 不等于 B，A 就是 B 的真子集，B 就是 A 的真超集
- __并集__：多个集合合并的结果
- __交集__：多个集合的公共部分
- __差集__：集合中除去和其他集合共有的部分

> &emsp;&emsp;这些是小学数学基础概念。

## 3.1. 集合运算
&emsp;&emsp;通过集合运算，我们可以方便地求出集合的差集、并集等，Python的集合除了提供了大量的集合运算方法，还提供了不少的特殊符号用来表示集合运算。

## 3.2. 并集
&emsp;&emsp;将集合 A 和集合 B 所有元素合并在一起，组成的集合称为集合 A 和集合 B 的 __并集__

![union](https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/union.png)

```python
s.union(*others) ==>> new set object   # 把多个集合和集合 s 进行合并，返回一个新的集合对象, 使用 | 表示

s.update(*others) ==>> None            # 把 *others 个可迭代可 hash 对象，和 s 进行并集，然后赋给 s。（就地修改）, 使用 |= 表示
```

## 3.3. 交集
&emsp;&emsp;集合 A 和集合 B，由所有属于 A 且属于 B 的元素组成的集合称为 __交集__。

![intersection](https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/intersection.png)

```python
s.intersection(*others) ==>> new set object   # 返回多个集合的交集，使用 & 表示

s.intersection_update(*others) ==>> None      # 获取多个集合的交集，就地进行修改，使用 &= 表示
```

## 3.4. 差集
&emsp;&emsp;集合 A 和 B，由所有属于 A 且不属于 B 的元素组成的集合称为 __差集__。

![difference](https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/difference.png)

```python
s.difference(*others) ==>> new set object    # 返回集合s和其他多个集合的差集，使用 - 表示

s.difference_update(*others) ==>> None       # 返回集合s和其他多个集合的差集，就地进行修改，使用 -= 表示
```

## 3.5. 对称差集
&emsp;&emsp;不属于集合 A 和集合 B 交集的其他元素组成的集合，数学表达式为：`(A-B) U (B-A)`。

![symmetric_differece](https://github.com/colinlee19860724/Study_Notebook/raw/master/Photo/symmetric_differece.png)

```python
s.symmetric_difference(other) ==>> new set object   # 返回和另一个集合的对称差集，使用 ^ 表示

s.symmetric_difference_update(other) ==>> None      # 返回和另一个集合的对称差集，就地修改，使用 ^= 表示
```

## 3.6. 集合的其他运算

```python
s.issubset(other) ==>> bool      # 判断当前集合是否是另一个集合的子集，使用 <= 表示

set1 < set2                      # 判断 set1 是否是 set2 的真子集

s.issuperset(other) ==>> bool    # 判断当前集合是否是 other 的超集，使用 >= 表示

set1 > set2                      # 判断 set1 是否是 set2 的真超集

s.isdisjoint(other) ==>> bool    # 判断当前集合和另一个集合有没有交集，没有交集返回 True
```

&emsp;&emsp;以上集合运算举例说明之：

```python
>>> s1 = set(range(1, 10))

>>> s2 = set(range(8, 15))

>>> s1, s2
({1, 2, 3, 4, 5, 6, 7, 8, 9}, {8, 9, 10, 11, 12, 13, 14})

>>> s1 | s2         # s1 和 s2 的并集
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

>>> s1 |= s2 ; s1   # 就地修改，结果赋值给 s1
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

>>> s1 = set(range(1, 10)) ; s2 = set(range(8, 15)) ; s1, s2
({1, 2, 3, 4, 5, 6, 7, 8, 9}, {8, 9, 10, 11, 12, 13, 14})

>>> s1 & s2         # s1 和 s2 的交集
{8, 9}

>>> s1 &= s2 ; s1   # 就地修改，结果赋值给 s1
{8, 9}

>>> s1 = set(range(1, 10)) ; s2 = set(range(8, 15)) ; s1, s2
({1, 2, 3, 4, 5, 6, 7, 8, 9}, {8, 9, 10, 11, 12, 13, 14})

>>> s1 - s2         # s1 和 s2 的差集，从 s1 中排除与 s2 的交集中的元素，得到所有属于 s1 但是不属于 s2 的元素组成的集合
{1, 2, 3, 4, 5, 6, 7}

>>> s1 -= s2 ; s1    # 就地修改，结果赋值给 s1
{1, 2, 3, 4, 5, 6, 7}

>>> s1 = set(range(1, 10)) ; s2 = set(range(8, 15)) ; s1, s2
({1, 2, 3, 4, 5, 6, 7, 8, 9}, {8, 9, 10, 11, 12, 13, 14})

>>> s1 ^ s2  # s1 和 s2 的对称差集，从 s1 和 s2 的并集中排除 s1 的 s2 交集
{1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14}

>>> s1 ^= s2 ; s1    # 就地修改，结果赋值给 s1
{1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14}

>>> s1,s2
({1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14}, {8, 9, 10, 11, 12, 13, 14})

>>> s2 < s1  # 判断 s2 是否是 s1 的真子集
False

>>> s1 = set(range(6)) ; s2 = set(range(5, -1, -1)) ; s1, s2
({0, 1, 2, 3, 4, 5}, {0, 1, 2, 3, 4, 5})

>>> s1 <= s2   # 判断 s1 是否是 s2 的子集
True

>>> s1 < s2   # 判断 s1 是否是 s2 的真子集
False

>>> s2 >= s1   # 判断 s2 是否是 s1 的超集
True

>>> s2 > s1   # 判断 s2 是否是 s1 的真超集
False

>>> s1.isdisjoint(s2)   # 判断 s2 是否与 s1 没有交集，没有交集返回 True
False
```