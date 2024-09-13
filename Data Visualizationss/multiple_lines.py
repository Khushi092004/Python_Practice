import matplotlib.pyplot as plt
import numpy as np

# Plotting multiple lines with different styles
data1 = np.arange(2, 7, 0.3)
plt.plot(data1, data1, "r--",  # Red dashed line
         data1, data1**2, "bs",  # Blue squares
         data1, data1**3, "g^")  # Green triangles

plt.title("Multiple Lines Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
