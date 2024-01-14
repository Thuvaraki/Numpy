import numpy as np

# content in data.txt file
# 1,20,30,55,98,100,56
# 4,2,3,9,71,85,96
# 45,86,96,35,12,54,45

# np.genfromtxt -> The function attempts to load data from the file into a NumPy array.
fileData = np.genfromtxt('data.txt',delimiter=',')
print(fileData)
# [[  1.  20.  30.  55.  98. 100.  56.]
#  [  4.   2.   3.   9.  71.  85.  96.]
#  [ 45.  86.  96.  35.  12.  54.  45.]]
print(fileData.astype('int32'))
# [[  1  20  30  55  98 100  56]
#  [  4   2   3   9  71  85  96]
#  [ 45  86  96  35  12  54  45]]

# Boolean masking and advanced indexing
print(fileData>50)
# [[False False False  True  True  True  True]
#  [False False False False  True  True  True]
#  [False  True  True False False  True False]]

print(fileData[fileData>50])
# [ 55.  98. 100.  56.  71.  85.  96.  86.  96.  54.]

#  integer array indexing
# creates a new array by selecting elements at the specified indices (1, 2, and 8) from the original array a
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]]) #[2 3 9]

print(~((fileData>50) & (fileData<100)))
# [[ True  True  True False False  True False]
#  [ True  True  True  True False False False]
#  [ True False False  True  True False  True]]