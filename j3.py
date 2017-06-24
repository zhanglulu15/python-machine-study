#密度聚类:用在聚类形状不规则的情形下
#sklearn.cluster.DBSCAN用来做基于密度聚类的算法
import numpy as np
from sklearn.cluster import DBSCAN
import  matplotlib.pyplot as plt

#国家面积和人口
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
#转换成numpy array
x = np.array(x)

#做归一化
a = x[:,:1]/17075400.0 * 10000
b = x[:,1:]/1392358249.0 * 10000
x = np.concatenate((a,b),axis=1)

#现在把训练数据和对应的分类放入分类器进行训练，这里没有出现噪点是因为把min_samples设置成了1
cls = DBSCAN(eps=2000,min_samples=1).fit(x)   #基于密度聚类的函数

#x中每项所属分类的一个列表
n_clusters = len(set(cls.labels_))

#x中每项所属分类的一个列表
cls.labels_

#画图

markers = ['^','x','o','*','+']
for i in range(n_clusters):
    menbers = cls.labels_ == i
    plt.scatter(x[menbers,0],x[menbers,1],s =60,marker = markers[i],c = 'b',alpha=0.5)  #s散点大小，marker = markers[i],表示i取0,1,2,3
                                                                                        #分别代表取各种图形，alpha表示透明度
plt.title('dbscan')
plt.show()