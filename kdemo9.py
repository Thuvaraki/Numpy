import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print(stats)
# [[1 2 3]
#  [4 5 6]]

# axis=0: Indicates that the operation should be performed along the columns (vertically).
# axis=1: Indicates that the operation should be performed along the rows (horizontally).
print(np.min(stats)) #1
print(np.max(stats)) #6
print(np.max(stats,axis=1)) #[3 6]
print(np.sum(stats,axis=0)) #[5 7 9]
print(np.sum(stats,axis=1)) #[ 6 15]

