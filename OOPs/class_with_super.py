# class_with_super.py

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def message(self):
        print(self.name, self.color)

class Car1(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

model2 = Car1("X2", "Yellow")
model2.message()

model3 = Car1("X3", "Green")
model3.message()
