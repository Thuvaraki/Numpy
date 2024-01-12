import numpy as np

# Matrice multiplication
a= np.ones((2,3))
b= np.full((3,2),2)
print(np.matmul(a,b))
# [[6. 6.]
#  [6. 6.]]

# find the determinant
z = np.identity(3)
print(np.linalg.det(z))
# 1.0

