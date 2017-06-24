from numpy import *
import time
import matplotlib.pyplot as plt
#计算欧式距离
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))   #计算欧式距离，且向量为二维向量

#初始质心的选择
def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i,:] = dataSet[index,:]
    return centroids

#k-means集群
def kmeans(dataSet,k):
    numSamples = dataSet.shape[0]

#第一列存储此样本所属的集群，
#第二列存储此样本与其质心之间的误差
    clusterAssment = mat(zeros((numSamples,2)))
    clusterChanged = True
#第一步：初始化中心
    centroids = initCentroids(dataSet,k)
    while clusterChanged:
        clusterChanged = False
## for each sample
        for i in range(numSamples):
            minDist = 100000.0
            minIndex = 0
## for each centroid
## step 2: find the centroid who is closest
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j
## step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist ** 2

## step 4: update centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis=0)

    print('Congratulations, cluster complete!')
    return centroids, clusterAssment


# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print("Sorry! I can not draw because the dimension of your data is not 2!")
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("Sorry! Your k is too large! please contact Zouxy")
        return 1

 # draw all samples
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
# draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()