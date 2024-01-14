import numpy as np

#reshaping array
A = np.array([[1,2,3],[4,5,6]])
print((A))
# [[1 2 3]
#  [4 5 6]]
print(A.reshape((3,2)))
# [[1 2]
#  [3 4]
#  [5 6]]

#vertically stacking vectors
# np.vstack function takes a sequence of arrays and stacks them vertically.
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2]))
# [[1 2 3 4]
#  [5 6 7 8]]
print(np.vstack([v1,v2,v2,v1]))
# [[1 2 3 4]
#  [5 6 7 8]
#  [5 6 7 8]
#  [1 2 3 4]]

# horizontal stacking
h1=np.ones((1,4))
h2=np.zeros((1,5))
print(np.hstack((h1,h2)))
# [[1. 1. 1. 1. 0. 0. 0. 0. 0.]]

