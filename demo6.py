# Be careful while copying arrays
import numpy as np
a= np.array([1,2,3])
b=a #here the variable b is pointing the same memory address of and, not copying the array in variable a to variable b
print(a)
b[0]=100
print(b) #[100   2   3]
print(a) #[100   2   3]

#Using copy function
a= np.array([1,2,3])
b=a.copy()
print("a:",a) #[1 2 3]
print("b:",b) #[1 2 3]
b[1]=100
print("a:",a) #[1 2 3]
print("b:",b) #[  1 100   3]
