import numpy as np

a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

print(a[0,1,1]) #1st array , 1st row, 1st column

#replace
a[:,1,:]=[[9,9],[8,8]]
print(a)