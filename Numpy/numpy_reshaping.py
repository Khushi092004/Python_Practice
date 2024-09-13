import numpy as np

# Reshaping arrays
new_data = np.array([1, 2, 3, 4, 5, 6])

# Reshaping to 2x3 and 3x2 arrays
print(new_data.reshape(2, 3))  # Output: [[1 2 3] [4 5 6]]
print(new_data.reshape(3, 2))  # Output: [[1 2] [3 4] [5 6]]
