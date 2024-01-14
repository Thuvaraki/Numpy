import numpy as np

# np.genfromtxt -> The function attempts to load data from the file into a NumPy array.
fileData = np.genfromtxt('data.txt',delimiter=',')
print(fileData)
print(fileData.astype('int32'))
