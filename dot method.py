import numpy as np

# dot method
# Example 1: 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product_1d = np.dot(a, b)
print(dot_product_1d)  # Output: 32

# Example 2: 
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product_2d = np.dot(A, B)
print(dot_product_2d)  # Output: [[19 22], [43 50]]

# Example 3: 
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
dot_product_2d_1d = np.dot(A, b)
print(dot_product_2d_1d)  # Output: [17 39]
