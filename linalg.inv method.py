import numpy as np

# linalg.inv

# Example 1: 
A = np.array([[1, 2], [3, 4]])
inv_A = np.linalg.inv(A)
print(inv_A)
# Output: [[-2.   1. ]
#          [ 1.5 -0.5]]

# Example 2: 
B = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
inv_B = np.linalg.inv(B)
print(inv_B)
# Output: [[-24.  18.   5.]
#          [ 20. -15.  -4.]
#          [ -5.   4.   1.]]

# Example 3: 
C = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
inv_C = np.linalg.inv(C)
print(inv_C)
# Output: [[0.75 0.5  0.25]
#          [0.5  1.   0.5 ]
#          [0.25 0.5  0.75]]
