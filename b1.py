#线性回归
import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
#print(len(x))
y = [0.199,0.389,0.580,0.783,0.980,1.177,1.380,1.575,1.771]
A = np.vstack([x,np.ones(len(x))]).T
print(np.ones(9))
print(A)
#调用最小二乘法
a,b = np.linalg.lstsq(A,y)[0]
#转换成numpy array
x = np.array(x)
y = np.array(y)
#画图
plt.figure()
plt.plot(x,y,'o',label = 'original data',markersize = 10)
plt.plot(x,a * x + b,'r',label = 'Fitted line')
plt.show()


# #使用最小二乘法进行线性拟合
import numpy as np
import matplotlib.pyplot as plt
#原始数据
x = [1,2,3,4,5,6,7,8,9]
y = [0.199,0.389,0.580,0.783,0.980,1.177,1.380,1.575,1.771]
t1= t2 = t3 = t4 =0
n =len(x)
for i in range(n):
    t1 += y[i]
    t2 += x[i]
    t3 += x[i] * y[i]
    t4 +=x[i] ** 2
    a = (t1*t2/n - t3) / (t2*t2/n - t4)
    b = (t1 - a*t2) / n
    x = np.array(x)
    y = np.array(y)

#画图
plt.figure()
plt.plot(x,y,'o',label = 'original data',markersize = 10)
plt.plot(x ,a*x + b,'r',label = 'Fitted line')
plt.show()


#曲线拟合转化为线性拟合
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#原始数据
T = [1960,1961,1962,1963,1964,1965,1966,1966,1968]
s = [29.72,30.61,31.51,32.13,32.34,32.85,33.56,34.20,34.83]
xdata = np.array(T)
ydata = np.log(np.array(s))
def func(x,a,b):
    return a + b*x

#使用非线性最小二乘法拟合函数
popt,pcov = curve_fit(func,xdata,ydata)
print()

#画图
plt.figure()
plt.plot(xdata,ydata,'ko',label = 'original noised data')
plt.plot(xdata,func(xdata, *popt),'r',label = 'fitted curve')
plt.show()