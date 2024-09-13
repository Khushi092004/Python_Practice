import numpy as np

# Creating 2D arrays
x = np.array([[10, 20], [30, 40]])
print(x)

# Creating arrays of ones and zeros
print(np.ones((3, 4)))  # 3x4 matrix of ones
print(np.zeros((3, 4))) # 3x4 matrix of zeros

# Generating random values in a 2D array
print(np.random.random((3, 4)))  # Random values in a 3x4 matrix

# Matrix operations
y = np.array([[2, 4], [5, 6]])
print(x + y)  # Element-wise addition
print(x.dot(y))  # Matrix multiplication

# Accessing matrix elements
print(y[0, 1])  # Output: 4
print(y[1, 0])  # Output: 5
print(y[0:2, 1])  # Output: [4 6]
