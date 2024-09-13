import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

new_d = pd.Series(np.random.rand(7), index=list('ABCDEFG'))
print(new_d)
new_d.plot.bar(color='g', alpha=0.1)
plt.title("Bar Plot with Alpha")
plt.show()

new_d.plot.barh(color="y", alpha=0.7)
plt.title("Horizontal Bar Plot with Alpha")
plt.show()
