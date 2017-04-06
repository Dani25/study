# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:17:20 2017

@author: saia12
"""

from matplotlib import pyplot as plt
from matplotlib import style

#style.use('ggplot')

x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2= [6,7,2,6]
print(len(x))
print(len(y))

plt.bar(x,y, color='c')

plt.bar(x2,y2, color='g')

plt.title('chart')

plt.ylabel('Y axis')
plt.xlabel('X axis')





plt.show()


