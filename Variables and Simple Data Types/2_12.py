from math import pi

r = 12

area = pi* r ** 2

print ("The area of a circle with radius",r,"is",area)

circumference = 2 * pi * r

print("The circumference of a circle with radius",r,"is", circumference)

rounded_area = round(area, 2)
rounded_circumference = round(circumference, 2)

print(rounded_area)
print(rounded_circumference)