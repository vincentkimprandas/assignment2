import numpy as np
 
 # transpose method

# Example 1: 
A = np.array([[1, 2], [3, 4]])
transpose_2x2 = np.transpose(A)
print(transpose_2x2)  # Output: [[1 3], [2 4]]

# Example 2: 
B = np.array([[1, 2], [3, 4], [5, 6]])
transpose_3x2 = np.transpose(B)
print(transpose_3x2)  # Output: [[1 3 5], [2 4 6]]

# Example 3: 
C = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
transpose_3d = np.transpose(C, (1, 0, 2))
print(transpose_3d)
# Output: 
# [[[ 1  2  3]
#   [ 7  8  9]]
#  [[ 4  5  6]
#   [10 11 12]]]
