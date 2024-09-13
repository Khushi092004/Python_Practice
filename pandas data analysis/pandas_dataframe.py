import pandas as pd

# Creating a pandas DataFrame
colors = ["red", "orange", "yellow", "white"]
degrees = [30, 40, 50, 60]
numbers = [11, 12, 13, 14]

new_df = pd.DataFrame({
    "colors": colors, 
    "degrees": degrees, 
    "numbers": numbers
}, columns=["colors", "degrees", "numbers"], index=range(1, 5))

print(new_df)
