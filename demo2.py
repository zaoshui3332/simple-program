import numpy as np
from fontTools.varLib.plot import stops

arr1 = np.array([1,2,3,4])
print('创建的数组为：',arr1)

arr2 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print('创建的数组为:\n',arr2)

print('数组形状为:',arr2.shape)

print('数组元素类型为',arr2.dtype)

print('数组元素个数为',arr2.size)

print('数组每个元素储存空间为',arr2.itemsize)

arr2.shape =4,3
print('重新设置后shape后arr2为:\n',arr2)



import numpy as np
print('使用arange函数创建的数组为:\n',np.arange(0,1,0.1))

print('使用linspace函数创建的数组为:\n',np.linspace(0,1,12))

print('使用logspace函数创建的数组为:\n',np.logspace(0,2,20))

print('使用zeros函数创建的数组为:\n',np.zeros((2,3)))

print('使用eye函数创建的数组为:\n',np.eye(3))

print('使用diag函数创建的数组为:\n',np.diag([1,2,3,4]))

print('使用ones函数创建的数组为:\n',np.ones((5,3)))

import numpy as np

print('转换结果为：')

print(np.float64(42))

print(np.int8(42.0))

print(np.bool_(42))

print(np.bool_(0))

print(np.float_(True))

print(np.float_(False))

df=np.dtype([('name',np.str_,40),('numitems',np.int64),('price',np.float64)])