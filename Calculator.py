# Define values of a, b, and o

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
o = input("Enter an Operator: ")

# Checks Addition operator and print addition value
if o == "+":
    print("The sum is", a + b)

# Checks subtraction operator and print value
elif o == "-":
    print("The Subtraction Value is", a - b)

# Checks Multiplication operator and print value
elif o == "*":
    print("The Multiplication Value is", a * b)

# Checks Division operator and print value
elif o == "/":

    if b != 0:
        result = a / b
        print("The Division Value is", result)
    else:
        print("Error! Division by Zero")

else:
    print("Error")
