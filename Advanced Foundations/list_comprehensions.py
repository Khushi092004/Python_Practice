# list_comprehensions.py

# List Comprehensions in Python
x = range(6)
evens = [n for n in x if n % 2 == 0]
print("Evens:", evens)

square_nums = [n * n for n in x]
print("Squares:", square_nums)

set_of_squares = {n * n for n in x}
print("Set of Squares:", set_of_squares)
