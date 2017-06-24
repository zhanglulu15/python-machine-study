import matplotlib.pyplot as plt
plt.plot([1,2,3,4])  #给ploy()一个列表数据[1,2,3,4]，matplotlib假设它是y轴的数值序列，
                    # 然后会自动产生x轴的值，因为python是从0作为起始的，所以这里x轴的序列对应为[0,1,2,3]。
plt.ylabel('some numbers')   #为y轴加注释
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])  #axis()函数给出了形如[xmin,xmax,ymin,ymax]的列表，指定了坐标轴的范围。
plt.show()

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')   #红色短划线，蓝色方块和绿色三角形
plt.show()


