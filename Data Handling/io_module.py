# io_module.py

import io

# Using io module
new_text = "Learning python and data analysis"
file = io.StringIO(new_text)

# Reading from the StringIO object
print(file.read())  # Output: Learning python and data analysis

# Writing to the StringIO object
file.write(" Master the Data handling concepts")
file.seek(0)  # Move cursor to the start
print(file.read())  # Output: Learning python and data analysis Master the Data handling concepts
