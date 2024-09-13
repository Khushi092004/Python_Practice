# class_with_method.py

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def message(self):
        print("The car name is " + self.name)

model1 = Car("A1", "White")
model1.message()
model1.color = "Red"
print(model1.color)
