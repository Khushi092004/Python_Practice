import matplotlib.pyplot as plt

new_films = ["film1", "film2", "film3", "film4"]
awards = [3, 9, 1, 5]
plt.bar(range(len(new_films)), awards)
plt.title("The top films")
plt.ylabel("No. of awards")
plt.xticks(range(len(new_films)), new_films)
plt.show()
