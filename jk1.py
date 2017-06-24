#coding=utf-8
import numpy as np
w = 0.01 * np.random.randn(10,5)   #生产服从标准正太分布的随机数
print(w)


# lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
def f(x):
    return x*x
print(f(3))

#等价于
x = 3
a = lambda x:x*x

