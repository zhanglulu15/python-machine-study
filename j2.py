#层次聚类:更多的是为层次话化的可视化提供支持，在我们比较陌生的数据层次时有帮助
#在klearn.cluster库中提供了一种AgglomerativeClustering的分类算法：基于层次的聚类方法

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

#从磁盘读取城市经度纬度表
import csv
x = []
f = csv.reader(open('/home/lulu/code/shuju/city.csv', encoding='utf-8'))
for v in f:
    #x.append([float(v.split(',')[2]),float(v.split(',')[3])])
    #print(v)
    jd = v[2]
    wd = v[3]
    if jd is '' or wd is '':
        continue
    #print([float(jd),float(wd)])
    x.append([float(jd),float(wd)])



#转换成numpy array
x = np.array(x)


#类簇的数量
n_clusters = 5

#现在把数据和对应的分类放入聚类函数中进行聚类，使用方差最小化的方法'ward‘
cls = AgglomerativeClustering(linkage = 'ward',n_clusters = n_clusters).fit(x)   #基于层次聚类，现在把数据和对应的分类数放入聚类函数中进行聚类，使用方差最小化的方法'ward'

#x中每一项所属分类的一个列表
cls.labels_

markers = ['^','x','o','*','+']
for i in range(n_clusters):
    menbers = cls.labels_ == i
    plt.scatter(x[menbers,0],x[menbers,1],s =60,marker= markers[i],c = 'b',alpha=0.5)  #s散点大小，marker = markers[i],表示i取0,1,2,3
                                                                                        #分别代表取各种图形，alpha表示透明度
plt.title('')
plt.show()