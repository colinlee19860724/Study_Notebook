
- [1. 内建函数 1](#1-内建函数-1)
- [2. 内建函数 2](#2-内建函数-2)
- [3. 内建函数 3](#3-内建函数-3)
- [4. 内建函数 4](#4-内建函数-4)
- [5. 内建函数 5](#5-内建函数-5)
- [6. 内建函数 6](#6-内建函数-6)
- [7. 内建函数 7](#7-内建函数-7)
- [8. 内建函数 8](#8-内建函数-8)
- [9. 可迭代对象](#9-可迭代对象)
- [10. 迭代器](#10-迭代器)
- [11. 内建函数 9](#11-内建函数-9)
- [12. 内建函数 10](#12-内建函数-10)
- [13. 总结](#13-总结)


# 1. 内建函数 1  
- **标识 `id()`**：返回对象的唯一标识，CPython 返回内存地址  
```python
In : a = 123

In : id(a)
Out: 9330656

In : def b(): 
...:     return a 
...:

In : id(b)
Out: 139701663500624

In : b()
Out: 123
```

- **哈希 `hash()`**：返回一个对象的哈希值  
```python
In : hash(range(3))
Out: 5050907061201647097

In : hash([3])    # 不能 hash 可变对象
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-b1bd0fbc0b77> in <module>
----> 1 hash([3])

TypeError: unhashable type: 'list'
```

- **类型 `type()`**：返回对象的类型  
```python
In : type(range(3))
Out: range

In : type(3)
Out: int

In : type(lambda x: x+1)
Out: function
```


- **类型转换**  
    1. `float(x)`：返回从数字或字符串 x 生成的浮点数。
    1. `int(x)`：返回一个使用数字或字符串 x 生成的整数对象，或者没有实参的时候返回 0 。
    1. `bin(x)`：将一个整数转变为一个前缀为“0b”的二进制字符串。
    1. `hex(x)`：将整数转换为以“0x”为前缀的小写十六进制字符串。
    1. `oct(x)`：将一个整数转变为一个前缀为“0o”的八进制字符串。
    1. `bool(x)`：返回一个布尔值，True 或者 False。
    1. `list([iterable])`：从可迭代对象返回一个列表。
    1. `tuple([iterable])`：从可迭代对象返回一个元组。
    1. `dict(**kwarg)`：从 k:v 键值对返回一个字典。
    1. `set([iterable])`：返回一个新的 set （集合）对象。
    1. `complex([real[, imag]])`：返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。
    1. `bytearray([source[, encoding[, errors]]])`：返回一个新的 bytes 数组。 bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。 
    1. `bytes([source[, encoding[, errors]]])`：返回一个新的“bytes”对象， 是一个不可变序列，包含范围为 0 <= x < 256 的整数。bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作。

**输入 `input([prompt])`**  
- 接收用户输入，返回一个字符串  
```python
In : input('please input: ')
please input: hello
Out: 'hello'
```

**打印 `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`**  

- 打印输出，默认使用空格分割、换行结尾，输出到控制台  
```python
In : print('hello noob')
hello noob

In : print('abc', 'hello', 'ok', sep='\n')
abc
hello
ok
```

# 2. 内建函数 2  

**对象长度 `len(s)`**  

- 返回对象（字符、列表、元组等）长度或项目个数 
```python
In : lst = [i for i in range(9)]

In : tup = (1, 2, 3)

In : st = 'colinlee'  

In : len(lst), len(tup), len(st)
Out: (9, 3, 8)
```


**`isinstance(obj, class_or_tuple)`**  

- 判断对象 obj 是否属于某种类型或者元组中列出的某个类型  
- `isinstance(True, int)`  
```python
In : isinstance(lst, tuple)  
Out: False

In : isinstance(tup, tuple)  
Out: True

In : isinstance(st, str)  
Out: True

In : isinstance(0, bool)  
Out: False

In : isinstance(True, int)  
Out: True
```


**`issubclass(cls, class_or_tuple)`**  
- 判断类型 cls 是否是某种类型的子类或元组中列出的某个类型的子类  
- `issubclass(bool, int)`  
```python
In : issubclass(bool, int)  
Out: True

In : issubclass(float, int)  
Out: False
```
  
# 3. 内建函数 3 

绝对值 `abs(x)` (x 为数值)  
```python
In : abs(-3)
Out: 3

In : abs(-3.14)  
Out: 3.14

In : abs(5.20)  
Out: 5.2
```

最大值 `max()` 最小值 `min()`  
- 返回可迭代对象中最大或最小值  
- 返回多个参数中最大或最小值  
```python
In : max(1, 3, 1, 4)  
Out: 4

In : min(1, 3, 1, 4)  
Out: 1

In : import random  
In : sam = random.sample(range(10), k=6)  
In : sam  
Out: [4, 1, 0, 3, 6, 9]

In : max(sam), min(sam)  
Out: (9, 0)

```

`round(x)` 四舍六入五取偶，`round(-0.5)`  
```python
In : round(1.4), round(1.6), round(1.5)
Out: (1, 2, 2)

In : round(-1.4), round(-1.6), round(-1.5)
Out: (-1, -2, -2)

In : round(-0.4), round(-0.6), round(-0.5)
Out: (0, -1, 0)
```
`pow(x , y)` 等价于 `x**y`  
```python
In : pow(2, 3), pow(2, 0)
Out: (8, 1)
```

`range(stop)` 从 0 开始到 stop-1 的可迭代对象；`range(start, stop [, step])` 从 start 开始到 stop-1 结束步长为 step 的可迭代对象  
```python
In : range(3)
Out: range(0, 3)

In : print(range(3))
range(0, 3)

In : for i in range(3):
    ...:     print(i)
    ...:
0
1
2

In : for i in range(1, 10, 2):
    ...:     print(i)
    ...:
1
3
5
7
9
```

`divmod(x, y)` 等价于 `tuple([x//y, x%y])`  
```python
In : divmod(10, 3)
Out: (3, 1)

In : tuple(10//3, 10%3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-d1b3fe479f67> in <module>
----> 1 tuple(10//3, 10%3)

TypeError: tuple() takes at most 1 argument (2 given)

In : tuple([10//3, 10%3])
Out: (3, 1)
```

`sum(iterable [, start])` 对可迭代对象的所有数值元素求和  
```python
In : sum(range(1,101,1))
Out: 5050
```

# 4. 内建函数 4 

- `chr(i)` 给一个一定范围的整数返回对应的字符  
```python
In : chr(97), chr(20013)
Out: ('a', '中')
```

- `ord(c)` 返回字符对应的整数，返回的是 Unicode  
```python
In : ord('a'), ord('中')
Out: (97, 20013)
```

`str()` 返回 object 的 字符串 版本。 如果未提供 object 则返回空字符串。  
```python
In : str(123)
Out: '123'

In : a = 'good'

In : str(a)
Out: 'good'
```

`repr()` 返回包含一个对象的可打印表示形式的字符串。  
```python
In : repr(123)
Out: '123'

In : repr(range(3))
Out: 'range(0, 3)'

In : class cls:
    ...:     pass
    ...:

In : repr(cls)
Out: "<class '__main__.cls'>"
```

`ascii()` 就像函数 repr()，返回一个对象可打印的字符串，但是 repr() 返回的字符串中非 ASCII 编码的字符，会使用 \x、\u 和 \U 来转义。生成的字符串和 Python 2 的 repr() 返回的结果相似。  
```python
In : st = 'I \tam \nColinLee'

In : print(st)
I       am
ColinLee

In : ascii(st)
Out: "'I \\tam \\nColinLee'"

In : ascii('胜利是属于我们的')
Out: "'\\u80dc\\u5229\\u662f\\u5c5e\\u4e8e\\u6211\\u4eec\\u7684'"
```

# 5. 内建函数 5 

`sorted(iterable [, key][, reverse])` 排序  
- 立即返回一个新的列表，默认升序  
- reverse 是反转  
```python
In : sorted([1, 3, 5])
Out: [1, 3, 5]

In : sorted([3, 1, 5])
Out: [1, 3, 5]

In : sorted([1, 3, 5], reverse=True)
Out: [5, 3, 1]

In : dic = {'c':1, 'b':2, 'a':1}

In : sorted(dic)
Out: ['a', 'b', 'c']

In : dic
Out: {'c': 1, 'b': 2, 'a': 1}
```

  
# 6. 内建函数 6  

翻转 `reversed(seq)`  返回一个翻转元素的迭代器  
```python
In : list(reversed("13579"))
Out: ['9', '7', '5', '3', '1']

In : {reversed((2, 4)) } # 有几个元素？
Out: {<reversed at 0x210243222b0>}

In : for x in reversed(['c','b','a']): print(x)
a
b
c

In : reversed(sorted({1, 5, 9}))
Out: <list_reverseiterator at 0x21024360748>

In : for x in reversed(sorted({1, 5, 9})): print(x)
9
5
1
```
  
# 7. 内建函数 7 

枚举 `enumerate(seq, start=0)`  
- 迭代一个序列，返回索引数字和元素构成的二元组  
- start 表示索引开始的数字，默认是 0 
```python
In : for x in enumerate([2,4,6,8]): print(x)
(0, 2)
(1, 4)
(2, 6)
(3, 8)

In : for x in enumerate("abcde"): print(x,end=" ")
(0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
In : enumerate('abcde')
Out: <enumerate at 0x210242c9c18>

In : print(enumerate('abcde'))
<enumerate object at 0x00000210242C9630>

In : dict(enumerate('abcde', start=1))
Out: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
```

# 8. 内建函数 8 

迭代器和取元素 `iter(iterable)`、`next(iterator [, default])`  
- iter 将一个可迭代对象封装成一个迭代器  
- next 对一个迭代器取下一个元素。如果全部元素都取过了，再次 next 会抛 StopIteration 异常 
```python
In : it = iter(range(3))

In : it
Out: <range_iterator at 0x210242a5670>

In : next(it)
Out: 0

In : next(it)
Out: 1

In : next(it)
Out: 2

In : next(it)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-60-bc1ab118995a> in <module>
----> 1 next(it)

StopIteration:
  
In : it2 = reversed([1,3,5])

In : next(it2)
Out: 5

In : next(it2)
Out: 3

In : next(it2)
Out: 1

In : next(it2)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-65-bc1ab118995a> in <module>
----> 1 next(it2)

StopIteration:
```

# 9. 可迭代对象  
- 可迭代对象  
- 能够通过迭代一次次返回不同的元素的对象。  
- 所谓相同，不是指值是否相同，而是元素在容器中是否是同一个，例如列表中值可以重复的，  
> &emsp;&emsp;['a', 'a']，虽然这个列表有 2 个元素，值一样，但是两个 'a' 是不同的元素，因为有不同的索引  

- 可以迭代，但是未必有序，未必可索引  
可迭代对象有：list、tuple、string、bytes、bytearray、range 对象、set、dict、生成器、迭代器 等  
- 可以使用成员操作符 `in`、`not in`，`in` 本质上对于线性结构就是在遍历对象，非线性结构求 hash 
```python
In : 3 in range(10)
Out: True

In : list(range(10))
Out: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In : 3 in (x for x in range(10))
Out: True

In : (x for x in range(10))
Out: <generator object <genexpr> at 0x0000021023F4B308>

In : tuple(x for x in range(10))
Out: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

In : 3 in {x:y for x,y in zip(range(4),range(4,10))}
Out: True

In : {x:y for x,y in zip(range(4),range(4,10))}
Out: {0: 4, 1: 5, 2: 6, 3: 7}
```
  
# 10. 迭代器  

- 迭代器  
- 特殊的对象，一定是可迭代对象，具备可迭代对象的特征  
- 通过 iter 方法把一个可迭代对象封装成迭代器  
- 通过 next 方法，迭代 迭代器对象  
- 生成器对象，就是迭代器对象  
```python
In : for x in iter(range(10)): print(x)
0
1
2
3
4
5
6
7
8
9

In : g = (x for x in range(10))

In : print(type(g))
<class 'generator'>

In : print(next(g))
0

In : print(next(g))
1

In : print(next(g))
2
```
# 11. 内建函数 9 

拉链函数 `zip(*iterables)`  
- 像拉链一样，把多个`可迭代对象`合并在一起，返回一个`迭代器`  
- 将每次从不同对象中取到的元素合并成一个元组  
- 取值依据木桶原理，元组的个数 = 元素最少的`可迭代对象`的元素个数
```python
In : list(zip(range(10),range(10)))
Out:
[(0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (4, 4),
 (5, 5),
 (6, 6),
 (7, 7),
 (8, 8),
 (9, 9)]

In : list(zip(range(10),range(10),range(5),range(10)))
Out: [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4)]

In : dict(zip(range(10),range(10)))
Out: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

In : {str(x):y for x,y in zip(range(10),range(1,5))}
Out: {'0': 1, '1': 2, '2': 3, '3': 4}
```
# 12. 内建函数 10 

**`all(iterable)`**  
- 可迭代对象所有元素都要等效为 True，或空的可迭代对象，all 函数返回 True  
- 一旦可迭代对象有一个元素等效为 False，all 函数返回 False  

**`any(iterable)`**  
- 可迭代对象任意一个元素等效为 True，any 函数返回 True  
- 空可迭代对象或所有元素都等效 False，any 函数返回 False 

```python
In : lst = [True, {1}, [2, 3], 5.1, 'abc']

In : print(all(lst), any(lst))
True True

In : print(all([]), any([]))
True False

In : print(all(lst + [0]), any(lst + [0]))
False True
```

# 13. 总结
&emsp;&emsp;以上内建函数的权威解释和用法请参见 [2. 内置函数 — Python 3.6.8 文档](https://docs.python.org/zh-cn/3.6/library/functions.html) 和 [Python3 内置函数 | 菜鸟教程](https://www.runoob.com/python3/python3-built-in-functions.html)