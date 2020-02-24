# import  numpy as np
#
# a1 =np.array([1,2,3,4,5] , dtype=complex)
# print(a1)
#
# a2 =np.array([[1,2], [3,4]])
# print(a2)
#
#
#
#
# dp = np.dtype('i4')
# print(dp)
# #
# # dp1 = np.dtype([('age' , np.int8)])
# # dp2 = np.array([10 , 20 ,30] , dtype=dp1 )
# # print(dp2)
# #
# # student = np.dtype([('name' , 'S20'),('age' ,'i1'),('marks', 'f4')])
# # z= np.array([('abc',25,35) ,('xyz',10,20)],dtype=student)
# # print(z)
# #
# # ar = np.array([[1,2,3] ,[4,5,6]])
# # print(ar.shape)
# #
# # ar.shape =(3,2)
# # print(ar)
# #
# #
# arrange1= np.arange(24)
# print(arrange1)
# it = iter(arrange1)
# x = np.fromiter(it , dtype=float)
# print(x)
# #
# # b =arrange1.reshape(2,3,4)
# # f =arrange1.reshape(2,3,4)
# # print(f)
# #
# print(np.char.add(['abc::','xyz::'] ,['cba','zyx']))
# #
# # nn = np.zeros((5,), dtype=np.int)
# # print(nn)
# #
#
#
# tr = np.arange(12).reshape(3,4)
# print(' my matrix is :')
# print(tr)
# print("After transposing\n")
# print(np.transpose(tr))
#
import numpy as np

aa1 = np.arange(9, dtype =float).reshape(3,3)
aa2 = np.array([10,20,30])

print('first matrix \n')
print(aa1)

print('second matrix \n')
print(aa2)
#additiom
print(np.add(aa1,aa2))
print('addition \n ')
#substraction
print(np.add(aa1,aa2))
print('substraction above \n ')
#multiplication
print(np.add(aa1,aa2))
print('multiplication \n ')
#division
print(np.divide(aa1,aa2))