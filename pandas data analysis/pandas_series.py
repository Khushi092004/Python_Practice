import pandas as pd

# Creating a basic pandas Series
new_s = pd.Series([10, 20, 30, 40])
print(new_s)

# Creating a pandas Series with custom index
put_index = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(put_index)
