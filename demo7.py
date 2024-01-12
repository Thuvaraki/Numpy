import numpy as np

a= np.array([1,2,3,4])
print(a)   #[1 2 3 4]
print(a+2) #[3 4 5 6]
print(a-2) #[-1  0  1  2]
print(a*2) #[2 4 6 8]
print(a/2) #[0.5 1.  1.5 2. ]
print(a//2) #[0 1 1 2]
print(a**2) #[ 1  4  9 16]
print(np.sin(a)) #[ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
print(np.cos(a)) #[ 0.54030231 -0.41614684 -0.9899925  -0.65364362]

b=np.array([1,0,1,0])
print(a+b) #[2 2 4 4]