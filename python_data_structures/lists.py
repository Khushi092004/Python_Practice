# Lists in Python
# List creation
new_list = []
new_list1 = list()
print(new_list)
print(new_list1)

# Type of list
print(type(new_list))

# List of numbers
nums = [1, 2, 3, 4, 5]
nums1 = list((10, 15, 20))
print(type(nums))
print(type(nums1))

# List of strings
str_list = ["blue", "red", "yellow"]
print(str_list)

# Multiple types in a list
mixed_list = ["Blue", True, 1, 3.5]
print("The mixed list:", mixed_list)

# List in a list
nums = [1, 2, [3, 3.1, 3.5], 4, 5]
print(nums)

# Accessing list items with the index number
print(nums[0])
print(nums[1])
print(nums[2])

# Knowing the number of items in list
print(len(nums))
print(nums[0:3])
print(nums[:3])
print(nums[3:])
print(nums[-1])
print(nums[-2])

# List operations
colors = ["red", "black", "white"]
print("white" in colors)
print("blue" not in colors)
colors.append("yellow")
print(colors)
colors.insert(2, "green")
print(colors)
colors.pop(3)
print(colors)
colors.extend(["indigo", "orange"])
print(colors)
del colors[0]
print(colors)
