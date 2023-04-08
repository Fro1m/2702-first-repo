import math


def radians_to_degrees():
    angle_in_radians = input('Please enter an angle in Radians: ')
    angle_in_degrees = float(angle_in_radians) * (180/math.pi)
    return angle_in_degrees

x = radians_to_degrees()
print(x)
