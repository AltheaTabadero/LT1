import math

#define all inputs
radius = int(input("Enter a number: "))

# processing
area = math.pi*math.pow(radius,2)
circumference = 2*math.pi*radius
square_root_of_area = math.sqrt(area)

# outputs
print(area)
print(circumference)
print(square_root_of_area)
print("floor: ", math.floor(area))
print("ceiling: ", math.ceil(area))