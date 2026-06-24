import math
# incomplete
print("Calculator V2.0")
running = True
print(f"running: {running}")
menu = 0

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
        
    inputEQ = input("> ")

    if inputEQ == "exit":
        running = False
    
    if inputEQ == "ls":
        print("math")
        for i, op in enumerate(listOfViableOperations, 1):
            print(f"{i}. {op}")
        print("special")
        for i, op in enumerate(listOfViableSpecialOperations, 1):
            print(f"{i}. {op}")

    if inputEQ == "help":
        print("help will show every operation")
        for operation in listOfViableOperations:
            print(operation, listOfViableOperations[operation])
        for operation in listOfViableSpecialOperations:
            print(operation, listOfViableSpecialOperations[operation])

    if len(inputEQ) == 2 and inputEQ[0] == "help":
        print("help func used")

    if inputEQ not in listOfViableOperations and inputEQ not in listOfViableSpecialOperations:
        print("invalid input")