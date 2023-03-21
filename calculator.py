import math

print("division (-)")
print("Addition (+)")
print("Multiplication (*)")
print("Division (/)")
print("Power (**)")
print("Square roots (sqr)")

operator = input("Enter one of the operators above: ")

if operator == "-":
    x = float(input("Enter first value: "))
    y = float(input("Enter a second value: "))
    minus = x - y
    print(f"It is equal: {minus} ")
elif operator == "*":
    x = float(input("Enter first value: "))
    y = float(input("Enter a second value: "))
    times = x * y
    print(f"It is equal: {times} ")
elif operator == "/":
    x = float(input("Enter first value: "))
    y = float(input("Enter a second value: "))
    if y == 0 :
        print("You can't divide by zero!!!")
    else:
        times = x / y
        print(f"It is equal: {times} ")
elif operator == "**":
    x = float(input("Enter first value: "))
    y = float(input("Enter power value: "))
    power = pow(x,y)
    print(f"It is equal: {power} ")
elif operator == "sqr":
    x = float(input("Enter value you want to square: "))
    sqr = math.sqrt(x)
    print(f"It is equal: {sqr} ")
else:
    print(f"Operator {operator} is not a valid operator.")
