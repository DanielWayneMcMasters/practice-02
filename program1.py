# Nicholas Seward
# Cirle Calculatr
# AI Disclaimer: This code was written without the use of AI tools.

# Enter the radius of the circl: 6.4
# Area: 83.29 square units
# Circumference: 42.52 units

import math

PI = math.pi

radius = float(input("Enter the radius of the circle: "))

area = PI * radius ** 2
circumference = 2 * PI * radius

print(f"Area: {area:.2f} sqaure units")
print(f"Circumference: {circumference:.2f} units")