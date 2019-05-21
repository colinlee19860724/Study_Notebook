
- [内建函数 1](#内建函数-1)
- [内建函数 2](#内建函数-2)
- [内建函数 3](#内建函数-3)
- [内建函数 4](#内建函数-4)
- [内建函数 5](#内建函数-5)
- [内建函数 6](#内建函数-6)
- [内建函数 7](#内建函数-7)
- [可迭代对象](#可迭代对象)
- [迭代器](#迭代器)
- [内建函数](#内建函数)
- [内建函数](#内建函数-1)


# 内建函数 1  

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
```
  
# 内建函数 2 

**对象长度 `len(s)`**  
- 返回一个集合类型的元素个数  

**`isinstance(obj, class_or_tuple)`**  

- 判断对象 obj 是否属于某种类型或者元组中列出的某个类型  
- `isinstance(True, int)`  

**`issubclass(cls, class_or_tuple)`**  
- 判断类型 cls 是否是某种类型的子类或元组中列出的某个类型的子类  
- `issubclass(bool, int)`  
  
# 内建函数 3 

绝对值 `abs(x)`  x 为数值  
```python
In : abs(-3)
Out: 3
```

最大值 `max()` 最小值 `min()`  
- 返回可迭代对象中最大或最小值  
- 返回多个参数中最大或最小值  

`round(x)` 四舍六入五取偶，`round(-0.5)`  

`pow(x , y)` 等价于 `x**y`  

`range(stop)` 从 0 开始到 stop-1 的可迭代对象；`range(start, stop [, step])` 从 start 开始到 stop-1 结束步长为 step 的可迭代对象  

`divmod(x, y)` 等价于 `tuple(x//y, x% y)`  

`sum(iterable [, start])` 对可迭代对象的所有数值元素求和  
``python
In : sum(range(1,101,1))
Out: 5050
``

# 内建函数 4 

- `chr(i)` 给一个一定范围的整数返回对应的字符  
- `chr(97)`	chr(20013)  
- `ord(c)` 返回字符对应的整数，返回的是 Unicode  
- `ord('a')`	ord(' 中 ')  
  

`str()` 、repr()、ascii() 后面说  

# 内建函数 5 

`sorted(iterable [, key][, reverse])` 排序  
- 立即返回一个新的列表，默认升序  
- reverse 是反转  
`sorted([1, 3, 5])`  
`sorted([1, 3, 5], reverse=True)`  
`sorted({'c':1, 'b':2, 'a':1})`  
  
# 内建函数 6  

翻转 `reversed(seq)`  
- 返回一个翻转元素的迭代器  
`list(reversed("13579")`)  
{`reversed((2, 4)`) } # 有几个元素？  
for x in `reversed(['c','b','a'])`: print(x)  
`reversed(sorted({1, 5, 9})`)  
  
# 内建函数 7 

枚举 `enumerate(seq, start=0)`  
- 迭代一个序列，返回索引数字和元素构成的二元组  
- start 表示索引开始的数字，默认是 0 for x in `enumerate([2,4,6,8])`:  
`print(x)`  
  

for x in `enumerate("abcde")`: print(x,end=" ")  

# 内建函数 8 

迭代器和取元素 `iter(iterable)`、next(iterator [, default])  
- iter 将一个可迭代对象封装成一个迭代器  
- next 对一个迭代器取下一个元素。如果全部元素都取过了，再次 next 会抛 StopIteration 异常 it = `iter(range(5)`)  
`next(it)`  
  

it = `reversed([1,3,5])` next(it)  

# 可迭代对象  

- 可迭代对象  
- 能够通过迭代一次次返回不同的元素的对象。  
- 所谓相同，不是指值是否相同，而是元素在容器中是否是同一个，例如列表中值可以重复的，  
['a', 'a']，虽然这个列表有 2 个元素，值一样，但是两个 'a' 是不同的元素，因为有不同的索引  
- 可以迭代，但是未必有序，未必可索引  
可迭代对象有：list、tuple、string、bytes、bytearray、range 对象、set、dict、生成器、迭代器 等  
- 可以使用成员操作符 in、not in，in 本质上对于线性结构就是在遍历对象，非线性结构求 hash 3 in `range(10)`  
3 `in(x for x in range(10)`)  
3 in {x:y for x,y in `zip(range(4)`,range(4,10))}  
  
# 迭代器  

- 迭代器  
- 特殊的对象，一定是可迭代对象，具备可迭代对象的特征  
- 通过 iter 方法把一个可迭代对象封装成迭代器  
- 通过 next 方法，迭代 迭代器对象  
- 生成器对象，就是迭代器对象  
for x in `iter(range(10)`): print(x)  
  

g = (x for x in `range(10)`) print(type(g)) print(next(g)) print(next(g))  

# 内建函数  

拉链函数 `zip(*iterables)`  
- 像拉链一样，把多个可迭代对象合并在一起，返回一个迭代器  
- 将每次从不同对象中取到的元素合并成一个元组  
  

`list(zip(range(10)`,range(10))) list(zip(range(10),range(10),range(5),range(10)))  

`dict(zip(range(10)`,range(10)))  
{`str(x)`:y for x,y in zip(range(10),range(10))}  

# 内建函数  

**`all(iterable)`**  
- 可迭代对象所有元素都要等效为 True，或空的可迭代对象，all 函数返回 True  
- 一旦可迭代对象有一个元素等效为 False，all 函数返回 False  

**`any(iterable)`**  
- 可迭代对象任意一个元素等效为 True，any 函数返回 True  
- 空可迭代对象或所有元素都等效 False，any 函数返回 False 

```python
lst = [True, {1}, [2, 3], 5.1, 'abc']  
print(all(lst), any(lst)) 
print(all([]), any([]))  
print(all(lst + [0]), any(lst + [0])  
```