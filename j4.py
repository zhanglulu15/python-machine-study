import numpy as np
from sklearn.cluster import  KMeans
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

#归一化
a = x[:,:1]/17075400.0 * 10000
b = x[:,1:]/1392358249.0 * 10000
x = np.concatenate((a,b),axis=1)

pn = x[np.random.choice(x.shape[0],3,replace=True),:]
#print(pn)

#随机选出3个
xn = []
for i in pn:
    distance_min = 1000000
    for j in x:
        if np.array_equal(j,i):
            continue
        distance = np.linalg.norm(j - i)
        if distance_min > distance:
            distance_min = distance
    xn.append(distance_min)

qn = x[np.random.choice(x.shape[0],3,replace=False),:]
#print(qn)

#随机选出3个
yn = []
for i in qn:
    distance_min = 1000000
    for j in x:
        if np.array_equal(j,i):
            continue
        distance = np.linalg.norm(j - i)
        if distance_min > distance:
            distance_min = distance

h = float(np.sum(yn))/(np.sum(xn) + np.sum(yn))
print(h)

