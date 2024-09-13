# User-Defined Functions
def addition(x, y):
    "Return the sum of x and y back to the caller"
    add = x + y
    return add

print(addition(10, 4))  # 14
print(addition(20, 30)) # 50
help(addition)

def new():
    global x
    x = 5
    print(x)

new()
print(x)

def new():
    print("Hi, Programming!")

new()
