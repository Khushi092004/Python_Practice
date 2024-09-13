import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
new_iris = sns.load_dataset('iris')
print(new_iris.head())
new_iris.petal_length.plot()
plt.title("Iris Petal Length")
plt.show()
