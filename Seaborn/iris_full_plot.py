import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
new_iris = sns.load_dataset('iris')
print(new_iris.head(3))
new_iris.plot()
plt.title("Iris Dataset Overview")
plt.show()
