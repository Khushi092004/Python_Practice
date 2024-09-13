# built_in_modules.py

# Built-in Modules
import random

new_randint = random.randint
print("Random Integer:", new_randint(2, 70))

from random import randint, choice
print("Random Integer:", randint(2, 40))
print("Random Choice:", choice([11, 31, 42, 45, 70]))

import math
print("Square Root of 5:", math.sqrt(5))
print("Square Root of 36:", math.sqrt(36))
print("Euler's Number:", math.e)
print("Pi:", math.pi)
print("Radians of 90 degrees:", math.radians(90))
print("Degrees of pi/6:", math.degrees(math.pi/6))

from math import sin, cos, tan, log
print("Sine of 0.5:", sin(0.5))
print("Cosine of 0.5:", cos(0.5))
print("Tangent of 0.5:", tan(0.5))
print("Log of 20:", log(20))
