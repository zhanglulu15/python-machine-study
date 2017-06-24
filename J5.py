#簇数的确定
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
x = [
    [9670250,1392358249],
    [2980000,1247923065],
    [9629091,317408015],
    [8514877,201032714],
    [377837,127270000],
    [7692024,23540517],
    [9984670,34591000],
    [17075400,143551289],
    [513115,67041000],
    [181035,14805358],
    [99600,50400000],
    [120538,24052231],
]
#转换成numpay array
x = np.array(x)

#归一化
a = x[:,:1]/17075400.0*10000
b = x[:,1:]/1392358249*10000
x = np.concatenate((a,b),axis=1)

#类簇的数量
n_clusters = 3

cls = KMeans(n_clusters).fit(x)  #使用K-Means算法，在m=1时所计算的肘方法的函数值，如果想计算m为其他值时的结果，
                                 # 可修改代码：n_clusters =1,即可得到相应的距离值

#每个类簇的中心点
cls.cluster_centers_

#x中每个点所属的簇
cls.labels_

#曼哈顿距离
def manhattan_distance(x,y):
    return np.sum(abs(x-y))

distance_sum = 0
for i in range(n_clusters):
    group = cls.labels_ == i
    members = x[group,:]
    for v in members:
        distance_sum += manhattan_distance(np.array(v),cls.cluster_centers_)
print(distance_sum)



