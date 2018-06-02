import numpy as np
import scipy.linalg as lng

N=100
A = np.zeros((N,N))
i,j = np.indices(A.shape)
A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1
#A[i<j]=2
B = np.arange(N)
F = np.linalg.solve (A,B)
print(A)
print(F)
print(B)
