import pandas as pd

# Reading a CSV file
df_csv = pd.read_csv("sample10.csv", low_memory=False)

# Displaying basic information about the DataFrame
print(df_csv)
print(df_csv.shape)  # Shape of the DataFrame (rows, columns)
print(df_csv.info())  # Summary of the DataFrame
print(df_csv.describe())  # Statistical description of the numerical columns

# Finding the row with the maximum price and minimum price
print(df_csv.loc[df_csv["price"].argmax()][["Cars", "price"]])  # Row with max price
print(df_csv.loc[df_csv["price"].argmin()][["Cars", "price"]])  # Row with min price
