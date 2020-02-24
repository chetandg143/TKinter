import numpy as np
from matplotlib import pyplot as plt
import  pandas as pd

x = np.arange(1,11)
y = 2 * x + 5

# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
# plt.title("sine wave form")
#
#
# plt.plot(x,y,'ob')
# plt.show()
#

# x =[5,8,10]
# y = [12 ,16, 6]
#
# x2 =[6,9,11]
# y2 = [6,15,7]
# plt.bar(x ,y ,color = 'r')
# plt.bar(x2,y2, color = 'b' ,align= 'center')
# plt.title('Bar Graph')
# plt.ylabel(' Y axis ')
# plt.ylabel(' X axis ')
# plt.show()
#
#
# import numpy as np
#
# a = np.array([1,2,3,4,5])
# np.save('outfile' ,a)
# print(a)
#
# b = np.load('outfile.npy')
# print(b)
#

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()