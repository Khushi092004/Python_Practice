# errors_and_exceptions.py

# Errors and Exceptions Handling
# SyntaxError: Missing parentheses in call to 'print'
# print "Py"

# IndexError: list index out of range
# x = [0, 1, 2]
# x[5]

# NameError: name 'discovery' is not defined
# import discovery

# TypeError: Can't concatenate str to int
# '3' + 4

# NameError: name 'hi' is not defined
# hi

# ZeroDivisionError: division by zero
# 59/0

try:
    x = 4
    y = 1
    print(x / y)
except:
    print("There is an error here!")

print("The operation is completed!")

try:
    x = 4
    y = 0
    print(x / y)
except TypeError:
    print("There is an error here!")
except ZeroDivisionError:
    print("You can't divide the number by zero!")

print("The operation is completed!")
