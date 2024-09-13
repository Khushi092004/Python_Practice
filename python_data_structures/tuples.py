# Tuples in Python
nums = tuple((1, 2, 3, 4, 5))
nums1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(type(nums))
print(type(nums1))

print(len(nums1))
print(nums1[0])
print(nums1[0:3])

# Tuples are immutable
try:
    nums[1] = 10
except TypeError as e:
    print(f"Error: {e}")

# Tuple operations
new_fruits = tuple(("Orange", "Cherry", "Lemon"))
print("Orange" in new_fruits)
print("Cherry" not in new_fruits)

# Deleting a tuple
del new_fruits
try:
    print(new_fruits)
except NameError as e:
    print(f"Error: {e}")
