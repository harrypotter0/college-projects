from matplotlib import pyplot as plt
from matplotlib import style
####
#import numpy as np
from numpy import genfromtxt


#style.use('ggplot')
'''
x,y = np.loadtxt('exampleFile.csv',
                 unpack=True,
                 delimiter = ',')
'''

data = genfromtxt('example2.csv',delimiter=' ')

plt.plot(data)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')



plt.show()
