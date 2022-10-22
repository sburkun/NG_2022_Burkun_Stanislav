import math

print("ax^2 + bx + c = 0")
print("Enter a:")
firstnumber = float(input())
print("Enter b:")
secondnumber = float(input())
print("Enter c:")
thirdnumber = float(input())


discriminant = (secondnumber ** 2 - 4 * firstnumber * thirdnumber)
print("discriminant =", discriminant)

if discriminant > 0:
    x1 = (-secondnumber + math.sqrt(discriminant) / (2*firstnumber))
    x2 = (-secondnumber - math.sqrt(discriminant) / (2*firstnumber))
elif discriminant == 0:
    x0 = (-secondnumber / (2*firstnumber))
else:
    print("Roots not found")