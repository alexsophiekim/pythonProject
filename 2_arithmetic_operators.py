import math

x = 3.14
y = -4
z = 5

# result = round(x) output 3
# result = ads(y) output 4 ads - absolute value
# result = pow(4,3) output 64 4x4x4
# result = max(x,y,z) output 5
# result = min(x,y,z) output -4
# print(result)


# print(math.pi)
# print(math.e)
# math.sqrt - square root
# math.ceil(x) - number round up

# print(result)

#Excercise 1
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)}cm")

#Excercise 2

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius,2)

print(f"The area of the circle is: {round(area,2)}cm^2")

