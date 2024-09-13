# Set Data Structure
set_nums = set((2, 4, 6, 8, 10))
set_nums1 = {1, 2, 3, 4, 5, 6}
print(type(set_nums))
print(type(set_nums1))

# Set operations
print(set('Python'))

x = set({1: "name", 2: "age"})
print(type(x))

# Deleting a set
del x
try:
    print(x)
except NameError as e:
    print(f"Error: {e}")
