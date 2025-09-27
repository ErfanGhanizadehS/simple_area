def circle_perimeter(r):
    pi = 3.14
    result = 2 * pi * r
    return result

radius_input = float(input("Please enter the radius: "))
perimeter = circle_perimeter(radius_input)
print("Your result is:", perimeter)
print("*"*70)

def circle_area(r):
    pi = 3.14
    result = (r*r)*pi
    return result


radius_input = float(input("Please enter the radius: "))
perimeter = circle_area(radius_input)
print("Your result is:", perimeter)
print("*"*70)

def rectangle_perimeter(length, width):
    result = 2 * (length + width)
    return result

length_input = float(input("Please enter the length: "))
width_input = float(input("Please enter the width: "))
perimeter = rectangle_perimeter(length_input, width_input)
print("Your result is:", perimeter)
print("*"*70)

def rectangle_area(length, width):
    result = length * width
    return result

length_input = float(input("Please enter the length: "))
width_input = float(input("Please enter the width: "))
area = rectangle_area(length_input, width_input)
print("Area is:", area)