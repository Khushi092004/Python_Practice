import matplotlib.pyplot as plt
import numpy as np

data1 = np.arange(2, 7, 0.3)
plt.plot(data1, data1, "r--", data1, data1**2, "bs", data1, data1**3, "g^")
plt.title("Custom Plot with Lines and Shapes")
plt.show()
