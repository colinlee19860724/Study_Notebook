**10_函数嵌套-作用域-闭包-LEGB-函数销毁**

---

[TOC]

---


# 1. 函数嵌套
&emsp;&emsp;一个函数中存在另外一个函数 (定义 / 调用)，这种方式我们称之为函数嵌套。函数的嵌套主要分为 `嵌套调用`，以及 `嵌套定义`。

```python
# 1.函数的嵌套调用
# 判断两个变量的最大值
def max2(a,b):        
    return a if a > b else b

# 判断四个变量的最大值
def max4(a,b,c,d):    
    res1 = max2(a,b)  # 函数的嵌套调用
    res2 = max2(res1,c)  
    res3 = max(res2,d)  
    print(res3)  
 
In : max4(10,100,21,99)
100

# 2.函数的嵌套定义
def func1():
    print('from func1')
    def func2():
        print('from func2')
        def func3():
            print('from func3')
        func3()  # 只有在 func2 中才能调用内部定义的函数 func3
    func2()

In : func1()
from func1
from func2
from func3

In : func3()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-b7e4f488dc81> in <module>
----> 1 func3()

NameError: name 'func3' is not defined
```

> &emsp;&emsp;**注意**：在函数的内部定义函数，只能在函数内部进行调用，在其他地方无法进行调用，强行调用就会提示 NameError 异常，所以说函数是有可见范围的，这就涉及到了作用域了

# 2. 作用域
&emsp;&emsp;一个标识符的可见范围，叫做**标识符的作用域**，一般常说的是**变量的作用域**。根据作用的范围主要分为 **全局作用域** 和 **局部作用域**。
- **全局作用域**：在整个程序运行环境中都可见
- **局部作用域**：在函数、类的内部可见，并且使用范围不能超过所在的局部作用域 (比如在函数内部定义了一个变量 x，我在全局使用变量 x 是不行的。)

```python
x = 1   # 全局变量
def outer():
    def inner():
        y = 100   # 局部变量
        print(x) 
    inner()

In : outer()
1

In : print(y)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-d9183e048de3> in <module>
----> 1 print(y)

NameError: name 'y' is not defined
```

- 全局变量 x 在全局生效，所以内部函数 inner 是可以打印 x 的  
- 局部变量 y 只在 inner 内部生效，所以在全局 print(y) 是无法调用局部变量 y 的  

&emsp;&emsp;**观察下面的例子**：

```python
x = 1
def outer():
    def inner():
        x += 1
        return x
    return inner()

In : outer()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-11-0811df1b6f71> in <module>
----> 1 outer()

<ipython-input-10-c03563d674ed> in outer()
      4         x += 1
      5         return x
----> 6     inner()
      7

<ipython-input-10-c03563d674ed> in inner()
      2 def outer():
      3     def inner():
----> 4         x += 1
      5         return x
      6     inner()

UnboundLocalError: local variable 'x' referenced before assignment

```

&emsp;&emsp;代码是从上到下执行的，所以这样写也没什么毛病，但是这里这个例子是无法执行的，为什么呢？  
1. x 作为全局变量，在 inner 内部是可见的
2. 在定义函数的阶段，Python 的**函数是作为一个整体一起被解释的**。
3. inner 函数在解释时，解释器发现在 inner 内部对 x 进行了定义 (`x += 1`)，那么它就不会在调用全局变量 x，而是标识 x 是局部定义的变量
4. 而在执行 `x += 1` 的时候，inner 内部的 x 还没有被定义，所以会提示 x 在定义前被执行了。(`x += 1` -> `x = x + 1` , 预先求 `x + 1` 时提示的，变量类型是赋值即定义)。  

如何解决呢？有两种方法：**更换变量名称**、声明当前变量非本地变量 (`global`)

```python
x = 1
def outer():
    def inner():
        y = x + 1    # 这里定义的 y 是局部变量，而 x 来自于全局变量
        return y
    return inner()
print(outer())
```

## 2.1. global 关键字
我们通过在函数内部使用 `global` 关键字来声明一个变量不是局部变量，而是一个全局变量。

```python
def outer():
    def inner():
        # 在函数内部声明一个全局变量，全局不存在时新建全局变量 x，
        # 全局变量 x 存在时，则使用全局变量 x
        global x   
        x = 10   # 修改全局变量 x 的值
        return x
    inner()

In : print(outer())
Out: 10
```

> &emsp;&emsp;虽然全局变量 x，在全局没有被定义，但是由于在函数内部使用了 global 关键字，所以 x 就变成了全局变量了。使用了 global 关键字，那么之前的例子就可以进行如下修改了

```python
x = 1
def outer():
    def inner():
        global x  # 使用全局变量 x
        x += 1    # 这里的 x 是全局变量，那么对 x 的修改必然会作用域全局
        return x
    return inner()

outer()
print(x)        # 2 , 在函数内部把全局变量 x 给修改了！！！
```

针对 global 的总结：
1. 外部作用域变量在内部作用域是可见的，但是不要在内部函数中直接使用或者修改，因为函数的目的就是为了封装，尽量与外界隔离。
2. 如果函数需要使用外部全局变量，请尽量使用函数的形参定义，在调用时传递实参来使用
3. 建议**不要使用 global**。

# 3. 闭包
&emsp;&emsp;在很多编程语言中都存在闭包的概念，那什么是闭包呢？闭包其实就是一个概念，出现在嵌套函数中，指的是：**内层函数引用到了外层函数的自由变量**，就形成了闭包
> **自由变量**：未在本地作用域中定义的变量，比如在嵌套函数的外层定义的变量 (非全局变量)，对内层来说，这个变量就叫做自由变量。

```python
def outer():
    c = [1]
    def inner():
        c[0] = 1
        return c
    return inner()

a = outer()
print(a)
```

&emsp;&emsp; **注意**：上面这个例子比较特殊，首先它是一个闭包，在 inner 函数内引用了外层函数的自由变量 c。因为这里的 c 是一个引用类型，我们可以直接通过 c 来操作 c 中的元素，但是没办法对 c 本身进行修改，即`c += [1,3]`。看似是列表拼接，但是它会重新对 c 进行声明，这就引发了之前的问题，内部函数 inner 没有定义 c，所以会报错！  
&emsp;&emsp;**当 c 不是引用类型的话，我们就没办法修改了吗？** 当然不是，可以使用 global 把 c 声明为全局变量，但是这就不是闭包了，所以这里就需要使用`nonlocal` 了 (python 3 特有)。  
&emsp;&emsp;**疑问？** 我们都说函数执行完毕后，函数的内部变量将会被回收，这里的 outer 执行完毕后，那么变量 c 应该会被回收啊，为什么还能被内层的 inner 找到呢？这是因为在定义阶段，解释器解释到 inner 函数时，由于函数是作为一个整体被解析的，所以解释器知道在 inner 内部引用了外部的变量，所以在执行函数 outer 时，并不会回收已被内部函数 inner 引用的自由变量 c。  

**一句话总结：闭包 = 函数 + 函数的运行环境**

## 3.1. nonlocal 关键字
&emsp;&emsp;使用了 nonlocal 关键字，将变量标记为不在本地作用域定义，而在上一级局部作用域中定义，但不能是全局作用域中定义。  
> nonlocal 只能用在嵌套函数的内部。  

```python
def outer():
    c = 100
    def inner():
        nonlocal c  # 声明不是本地的 c（引用上级目录的 c)
        c += 200    # 对 c 进行修改
        return c
    print(' 内 ', c)   # 100
    c = 1000
    return inner()

a = outer()
print(' 外 ',a)  # 1200

# 输出
 内  100
 外  1200
```

# 4. 默认值的作用域
&emsp;&emsp;在 Python 中，一切皆对象，函数也不列外，当我们给函数定义默认值时，Python 会把它存放在函数的属性中，这个属性值就伴随这个函数对象的整个生命周期。  
> `foo.__defaults__` 属性查看函数的默认值属性  

```python
import random

def add2(x=set(),y=[]):
    x.add(random.randint(1,10))
    y.append(1)
    # print(x)
    # print(y)

print(add2(),id(add2))
print(add2.__defaults__)

print(add2(),id(add2))
print(add2.__defaults__)

# 输出
None 2156636731456
({10}, [1])
None 2156636731456
({10, 6}, [1, 1])
```

&emsp;&emsp;仔细查看输出结果，发现函数地址没有变，也就是说函数这个对象没有变，但是我们发现每次它的`__default__`属性都会发生变化，这是为什么呢？这是因为 set 和 list 的默认值都是引用类型，它们引用的都是函数在定义时定义的默认值中。 虽然函数执行完就释放了内存空间，也是由于引用类型，指向默认空间的指针没了，但是已经在调用时改变了默认值空间的对象中的元素，所以在下一次再次调用时此时默认值空间的元素已经被改变了。所以当函数的默认值为引用类型时，这点要特别的注意了  
解决办法：  
- 在定义时使用引用类型时，在函数内部使用前先进行 copy。
- 在定义函数时默认使用 None 值，在函数内判断如果是 None 则开辟一个引用类型。

# 5. 变量名解析原则 LEGB
&emsp;&emsp;变量的解析原则，也可以理解为变量的查找顺序：
- L(`Local`): 本地作用域、局部作用域的 local 命名空间。函数调用是创建，调用结束消亡
- E(`Enclosing`): Python 2.2 时引入嵌套函数，实现了闭包，这个就是嵌套函数的外部函数的命名空间
- G(`Global`): 全局作用域，即一个模块的命名空间。模块被 import 时创建，解释器退出时消亡
- B(`Build-in`): 内置模块的命名空间，生命周期从 Python 解释器启动时创建到解释器退出时消亡。例如 print 函数、open 函数等。
> 变量查找的规则为 L > E > G > B，即：先本地，后嵌套，再全局，最后是内置函数中。  

# 6. 函数的销毁
全局函数：
- 重新定义同名函数
- del 语句删除函数名称，函数对象引用计数减 1
- 程序结束时  

局部函数：
- 重新在上级作用域定义同名函数
- del 语句删除函数名称，函数对象的引用计数减 1
- 上级作用域销毁时
