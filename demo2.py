import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#Get a specific element
print(a[1,5])

#Get a specific row
print(a[1,:])

#Get a specific column
print(a[:,5])

#[start index, end index, step size]
print(a[0, 1:6:2])

#changing a specific element
a[1,5] = 20
print(a)

#changing all elements of a column
a[:,3]= 5
print(a)


