import numpy as np
matr1 =np.diag((1,2,3))
print(matr1,'\n',matr1,'\n',matr1,'\n',matr1)
matr2 =np.bmat('matr1,matr1;matr1,matr1')
print('合并为:\n',matr2)
print('转置矩阵为:\n',matr2.T)