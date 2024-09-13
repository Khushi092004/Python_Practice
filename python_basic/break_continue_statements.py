# Using break statement
for x in range(0, 5):
    if x == 3:
        break
    print(x)
print(f"The last number in the loop is {x}")

# Using continue statement
for x in range(0, 7):
    if x == 3:
        continue
    print(x)
print(f"The last number in the loop is x = {x}")
