import numpy as np
import pylab as plt
import matplotlib.cm as cm

x = np.array([1,4,6,7])
#print(x)
y = np.linspace(1,6,10)
#print(y)
z = np.arange(1,100,10)
print(z)
print('number of dimensions of z:', np.ndim(z))
print('length of array', len(z))

xm=np.ones((3,4))
print(xm)

xm[2,2:3] = 200
print(xm)

xm1 = np.array([[2,5,6,7],
                [5,6,3,9],
                [6,2,1,7]])
#print(xm1)

plt.matshow(xm1)
plt.colorbar(ticks=[2, 4, 6, 8])
#print(xm1)

plt.matshow(xm1, cmap=cm.rainbow)
plt.colorbar(ticks=np.arange(2, 9, 2))



plt.show()
