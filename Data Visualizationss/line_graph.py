import matplotlib.pyplot as plt
import numpy as np

# Plotting a simple line graph
new_data = np.arange(9)

plt.plot(new_data)
plt.title("The new data graph")
plt.xlabel("x label name")
plt.ylabel("y label name")
plt.show()
