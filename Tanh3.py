import numpy as np
import matplotlib.pyplot as plt
d = np.random.randn(1000,500)

hideen_layer_size = [500] * 10

nonlinerities = ['tanh'] *len(hideen_layer_size)



act = {'relu':lambda x:np.maximum(0,x),'tanh':lambda x:np.tanh(x)}
hs = {}
for i in range(len(hideen_layer_size)):
     x = d if i == 0 else hs[i-1]
     fan_in = x.shape[1]
     fan_out = hideen_layer_size[i]
     w = np.random.randn(fan_in,fan_out) * 1.0
     h = np.dot(x,w)
     h = act[nonlinerities[i]](h)
     hs[i] = h

print('input layer had mean %f and std %f' % (np.mean(d),np.std(d)))
layer_means = [np.mean(h) for i ,h in hs .items()]    #均值
layer_stds = [np.std(h) for i,h in hs.items()]      #方差
for i ,h in hs.items():

    print('hidden layer %d had mean %f and std %f' % (i + 1,layer_means[i],layer_stds[i]))

    print(hs.keys(), layer_stds)

    # plt.figure()
    # plt.subplot(121)
    # plt.plot(hs.keys(), layer_means, 'ob-')
    # plt.title('layer mean')
    # plt.subplot(122)
    # plt.plot(hs.keys(), layer_stds, 'or-')
    # plt.title('layer std')

    plt.figure()
    for i, h in hs.items():
        plt.subplot(1, len(hs), i + 1)
        plt.hist(h.ravel(), 30, range=(-1, 1))
    plt.show()