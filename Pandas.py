

import numpy as np
import pandas as pd

#
# # a = np.array(['a','b','c','d','e'])
# b =pd.Series(['a','b','c','d','e'] , index=[101,102,103,104,105])
# print(b[101])
#
#
# a = [1,2,3,4,5]
# pf = pd.DataFrame(a)
# print(pf)
#
# data =[['alex' ,30 ,18000], ['abc' , 23 ,25000], ['xyz',55,15000]]
# pg = pd.DataFrame(data , columns=['name','age' ,'salary'] )
# print(pg)
# print('\n')
#
#
# d = { 'One':pd.Series([1,2,3] , index=['a','b','c']) ,
#      'Two':pd.Series([1.5,2.5,3.5 ,4.5] , index=['a','b','c','d'])}
# dd =pd.DataFrame(d)
# print(dd,'\n')
# print(dd.iloc[1],'\n')
#
# dd['Three'] = pd.Series([10,20,30] , index=['a','b','c'])
# dd['four'] = dd['Three'] + d['Two']
#
# print(dd)
#
#
# d1 = pd.DataFrame([[1,2],[3,4]] ,columns=['a','b'] )
# d2 =pd.DataFrame([[4,5],[6,7]] , columns = ['a','b'])
#
# d1 = d1.append(d2)
# print(d1)
#
# p = pd.Series(np.random.randn(4))
# print(p)
# print()

#
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#      'Age':pd.Series([25,26,25,23,30,29,23]),
#      'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
#
# # Create a DataFrame
# d1 = pd.DataFrame(d)
# print(d1.sum(1))
#
# print ("The transpose of the data series is:")
# print (d1.T)




tr = pd.DataFrame()

j = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
                       'Lee','David','Gasper','Betina','Andres']),
     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
     }

#Create a DataFrame
k = pd.DataFrame(j)
print (k.sum())

print(k.min)


s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s)

print(s.str.lower(),'\n')

print(s.str.islower())

pd.set_option('display.max_rows',80)
print(pd.get_option('display.max_rows'))

print(pd.Timedelta(days=2))

print(pd.date_range('24/2/2020' ,periods=5 , freq='M'))


gf =pd.DataFrame(np.random.randn(10,4) , index= pd.date_range('1/1/2000' , periods=10 ), columns =list('ABCD'))
gf.plot()
df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
                                                            periods=10), columns=list('ABCD'))

df.plot()