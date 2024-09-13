import pandas as pd

# Reading a table from a webpage
new_url = "https://en.wikipedia.org/wiki/Academy_Awards"
new_html = pd.read_html(new_url, header=0, index_col=0)[3]

# Displaying the first 5 rows of the HTML table
print(new_html.head(5))
