Python 知识点

判断一个元素是否在 list 中
```
a = [1, 2.5, 7, 13221, 4.6545]
if 7 in a:
    print('yes')
else:
    print('no')
```

判断是否是数字
```
try:
   val = int(userInput)
except ValueError:
   print("That's not an int!")
```

判断是什么类型
```
>>> type([]) is list
True
>>> type({}) is dict
True
>>> type('') is str
True
>>> type(0) is int
True
>>> type({})
<type 'dict'>
>>> type([])
<type 'list'>
```

Python range() 函数用法

```
range(start, stop[, step])

>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
```
以下是 range 在 for 中的使用，循环出runoob 的每个字母:
```
>>>x = 'runoob'
>>> for i in range(len(x)) :
...     print(x[i])
...
r
u
n
o
o
b
>>>
```

If 在列表中
```
 if number in range(len(response)):
            print('yes')
        else:
            print('no')
```

Input text
```
in Python 3.x:

filename = input('Enter a file name: ')
```

代码风格指南

```
pip install pycodestyle
```

runing 

```
pycodestyle filename.py
```

程序 autopep8 能自动将代码格式化 成 PEP 8 风格。用以下指令安装此程序：

```
pip install autopep8
autopep8 --in-place optparse.py
```
