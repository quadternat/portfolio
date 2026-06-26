import math
# incomplete
print("Calculator V2.0")
running = True
print(f"running: {running}")
menu = 0
operation = False

listOfViableOperations = {
    "+": "Adds 2 numbers together",
    "-": "Subtracts the second number from the first",
    "*": "Multiplies 2 numbers",
    "/": "Divides the first number by the second",
    "//": "Floor division",
    "%": "Modulo (returns the remainder)"
}

listOfViableSpecialOperations = {
    "ls": "lists all functions which are usable",
    "help": "provides description of all operations and which Operation it is (sp or reg)",
    "exit": "exits the program"
}

while running:
    if menu == 0:
        print('''welcome to calculator Version 2 - if you need help just use "help" ''')
        menu += 1

    operation = False
    inputEQ = input("> ")
    print(len(inputEQ))

    if inputEQ == "exit":
        running = False
    
    if inputEQ == "ls":
        print("math")
        for i, op in enumerate(listOfViableOperations, 1):
            print(f"{i}. {op}")
        print("special")
        for i, op in enumerate(listOfViableSpecialOperations, 1):
            print(f"{i}. {op}")
        operation = True

    if inputEQ == "help":
        print("help will show every operation")
        for operation in listOfViableOperations:
            print(operation, listOfViableOperations[operation])
        for operation in listOfViableSpecialOperations:
            print(operation, listOfViableSpecialOperations[operation])
        operation = True

    if len(inputEQ) >= 4 and inputEQ[0:4] == "help":
        # print("help func used")
        # print(inputEQ[5])
        if inputEQ[5:] in listOfViableOperations:
            print(inputEQ[5:], listOfViableOperations[inputEQ[5:]])
        operation = True
        
    if inputEQ not in listOfViableOperations and inputEQ not in listOfViableSpecialOperations and not operation:
        print("invalid input")