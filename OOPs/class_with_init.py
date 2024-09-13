# class_with_init.py

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

model1 = Car("A1", "Black")
print(model1.name)
print(model1.color)
