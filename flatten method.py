import numpy as np
# flatten method

# Example 1: 
A = np.array([[1, 2], [3, 4]])
flatten_A = A.flatten()
print(flatten_A)  # Output: [1 2 3 4]

# Example 2: 
B = np.array([[1, 2], [3, 4], [5, 6]])
flatten_B = B.flatten()
print(flatten_B)  # Output: [1 2 3 4 5 6]

# Example 3: 
C = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
flatten_C = C.flatten()
print(flatten_C)  # Output: [1 2 3 4 5 6 7 8]
