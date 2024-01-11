import numpy as np

# 1D array
a = np.array([1,2,3] ,dtype='int32')
print(a)
print(a.ndim) #Get dimension
print(a.shape) #Get shape->num of rows amd columns
print(a.dtype) #Get type
print(a.itemsize) #Get size
print(a.nbytes) #Get total size

# 2D array
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
print(b.ndim) #Get dimension
print(b.shape) #Get shape->num of rows amd columns
print(b.dtype)
print(b.itemsize)
print(b.nbytes)