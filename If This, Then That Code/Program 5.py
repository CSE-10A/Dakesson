# get all three sides of the triangle
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

# an equilateral triangle has all three sides equal
if side1 == side2 == side3:
    print("This is an equilateral triangle.")
else:
    print("This is not an equilateral triangle.")

