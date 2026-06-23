import math

print("calculator v1.1")
input1 = float(input("enter first number: "))
operation = input("(ls -> listing) operation: ")
input2 = float(input("Second number: "))

operations = [
    "+",
    "-",
    "*",
    "/",
    "//",
    "%",
    "^",
    "ls",
]

if operation not in operations:
    print("invalid operation")
    exit()

if operation == "ls":
    print(f"available operations: {', '.join(operations)}")
operation = input("operation: ")

if operation not in operations:
    print("invalid operation")
    exit()

if operation == "+": 
    print(input1 + input2)
if operation == "-":
    print(input1 - input2)
if operation == "*":
    print(input1 * input2)
if operation == "/":
    if (input1 or input2) == 0:
        print("invalid")
        exit()
    print(input1 / input2)
if operation == "//":
    if (input1 or input2) == 0:
        print("invalid")
        exit()
    print(input1 // input2)
if operation == "%":
    if input2 == 0:
        print("division by zero")
        exit()
    print(input1 % input2)
if operation == "^":
    print(math.pow(input1, input2))