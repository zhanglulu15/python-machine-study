#用KMmeans做玩分类后在做聚类质量的评估
#定义轮廓系数 s(v)=(b(v) - a(v))/max[a(v),b(v)]
#其中a(v):表示类簇内部的紧凑性，b(v)表示：该类簇和其他类簇之间的分离程度
import numpy as np
from sklearn.cluster import KMeans


#面积，入口
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

#类簇的数量
n_clusters = 3

#现在把数据和对应
cls = KMeans(n_clusters).fit(x)

#每个簇的中心点
cls.cluster_centers_

#x中每个点所属的簇
cls.labels_

#曼哈顿距离
def manhattan_distance(x,y):
    return np.sum(abs(x-y))


#a(v),x[0]到其他点的距离的平均值
distance_sum = 0
for v in x[1:]:
    distance_sum += manhattan_distance(np.array(x[0]),np.array(v))
av = distance_sum/len(x[1:])
print(av)


#b(v),x[0]
distance_min = 100000
for i in range(n_clusters):
    group = cls.labels_ == i
    members = x[group,:]
    for v in members:
        if np.array_equal(v,x[0]):
            continue
        distance = manhattan_distance(np.array(v),cls.cluster_centers_)
        if distance_min > distance:
            distance_min = distance
bv = distance_sum/n_clusters
print(bv)


sv = float(bv - av)/max(av,bv)
print(sv)
