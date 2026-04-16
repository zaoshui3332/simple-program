import numpy as np
arr1 =np.array([1,2,3,4,5,6])
arr2 =np.array([[2,3],[4,5],[6,7]])
print(arr1)
print(arr2)
print(arr2.dtype)

print(np.arange(0,30,3))

print(np.linspace(0,20,8))

print(np.zeros((4,5)))

print(np.ones((3,4)))

print(np.eye(5))

print(np.diag((5,10,15,20)))

arr3 =np.array([[1,2,3],[3,4,5],[6,7,8]])
print('维数:',arr3.ndim,'\n','形状:',arr3.shape,'\n','元素总数:',arr3.size,'\n','数据类型:',arr3.dtype,'\n','每个字节元素数:',arr3.itemsize)

print('生成的随机数为:\n',np.random.uniform(size=[2,4]))

print('生成一个1~200之间的6列6行随机整数矩阵:\n',np.random.randint(1,200,(6,6)))

print('使用shuffle函数打乱的以为数组:\n',np.random.shuffle([1,2,3,4,5,6,7,8]))
