import math
b = int(input("Enter a number for variable b: "))
c = int(input("Enter a number for variable c: "))
delta = ((b**2) - 4*c)
if delta <0:
    print("This equation has no real roots.")
else:
    root_1 = (-b + math.sqrt(delta))/2
    root_2 = (-b - math.sqrt(delta))/2
    if delta == 0:
        print("Both roots are equal to each other and " + str(round(root_1)) + ".")
    elif delta > 0:
        print("The first root is " + str(round(root_1)) + " and the second root is " + str(round(root_2)) + ".")
# Rounding, because for certain values (e.g. b=2 and c=1) output is displayed as float (-1.0 in this example).