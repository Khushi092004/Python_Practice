import numpy as np

# Creating a NumPy array
x = np.array([1, 2, 3, 4])
print(x)

# Creating arrays of zeros and ones
print(np.zeros(5))  # Output: [0. 0. 0. 0. 0.]
print(np.ones(5))   # Output: [1. 1. 1. 1. 1.]

# Generating random values
print(np.random.random(5))  # Output: Random values

# Basic math operations
new_math = np.array([1, 2, 3])
new_ones = np.ones(3)

print(new_math + new_ones)  # Output: [2. 3. 4.]
print(new_math * 2)         # Output: [2 4 6]
print(new_ones * 3)         # Output: [3. 3. 3.]

# Accessing array elements
print(new_math[0])  # Output: 1
print(new_math[1])  # Output: 2

# Array methods
print(new_math.max())  # Output: 3
print(new_math.min())  # Output: 1
print(new_math.sum())  # Output: 6
