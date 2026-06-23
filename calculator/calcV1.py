import math

print("calculator v1.0")

input1 = float(input("First number: "))
operation = input("operation: ")
input2 = float(input("Second number: "))

Operationlist = [
    "+",
    "-",
    "*",
    "^",
    "/",
    "//",
    "%",
]
if operation not in Operationlist:
    print("not valid operation")
    exit()

end: float | None = None

if operation == "+":
    end = input1 + input2
elif operation == "-":
    end = input1 - input2
elif operation == "*":
    end = input1 * input2
elif operation == "^":
    end = float(math.pow(input1, input2))
elif operation == "/":
    end = input1 / input2
    if input2 == 0:
        print("division by zero")
        exit()
elif operation == "//":
    if input2 == 0:
        print("division by zero")
        exit()
    end = input1 // input2
elif operation == "%":
    if input2 == 0:
        print("division by zero")
        exit()
    end = input1 % input2

if end is not None:
    print(end)
