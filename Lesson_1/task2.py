print("Enter a first number:")
numberone = int(input())

print("Enter a second number:")
numbertwo = int(input())

print("Select operation number:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divide")
operation = int(input())

if operation==1:
    print(numberone, "+", numbertwo, "=", numberone + numbertwo)
elif operation==2:
    print(numberone, "-", numbertwo, "=", numberone - numbertwo)
elif operation==3:
    print(numberone, "*", numbertwo, "=", numberone * numbertwo)
elif operation==4:
    print(numberone, "/", numbertwo, "=", numberone / numbertwo)
else:
    print("Invalid operation")