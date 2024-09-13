# class_with_inheritance.py

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def message(self):
        print(self.name, self.color)

model1 = Car("X1", "White")
model1.message()

class Car1(Car):
    pass

model1 = Car1("B1", "Blue")
model1.message()
