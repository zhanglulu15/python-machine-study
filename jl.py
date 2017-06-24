#聚类
#准备一个中国城市的经度纬度表，每一列分别代表省，市，纬度，经度，然后利用kmeans聚类，将中国城市分成五个地区
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

#现在把数据和对应
cls = KMeans(n_clusters).fit(x)

cls.labels_

markers = ['^','x','o','*','+']
for i in range(n_clusters):
    menbers = cls.labels_ == i
    plt.scatter(x[menbers,0],x[menbers,1],s =60,marker= markers[i],c = 'b',alpha=0.5)  #s散点大小，marker = markers[i],表示i取0,1,2,3
                                                                                        #分别代表取各种图形，alpha表示透明度
plt.title('')
plt.show()