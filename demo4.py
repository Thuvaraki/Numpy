import numpy as np

a= np.zeros((2,2))
print(a)
# [[0. 0.]
#  [0. 0.]]

b = np.ones((2,2,2))
print(b)
# [[[1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]]]

c = np.full((2,2,),99)
print(c)
# [[99 99]
#  [99 99]]

n = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
d=np.full_like(n,3) #give same shape like array n and fill the all values with 3
print(d)
# [[[3 3]
#   [3 3]]

#  [[3 3]
#   [3 3]]]

e=np.random.rand(4,2) #randomly print numbers between 0 (inclusive) and 1 (exclusive). And its shape is (4,2)
print(e)

# random integer value
# np.random.randint() generates random integers within a specified range.
# In this case, the range is from 0(default) to 6 (7 is exclusive), and the size of the array is specified as (3, 3)
f= np.random.randint(7,size=(3,3))
print(f)

# we can specify the starting point also
g= np.random.randint(4,8,size=(3,3))
print(g)

#identity matrix
print(np.identity(4))

arr=np.array([1,2,3])
r1 = np.repeat(arr,3)
print(r1)
# output - [1 1 1 2 2 2 3 3 3]

arr=np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0) #axis=0 parameter indicates that the repetition should occur along the first axis
print(r1)
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]


