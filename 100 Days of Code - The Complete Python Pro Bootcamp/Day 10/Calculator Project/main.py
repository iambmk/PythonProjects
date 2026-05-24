import art
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    accumulation = True
    num1 = float(input("what is your first number? "))
    while accumulation:
        for symbol in operations:
            print(symbol)
        selected_operation = input("Pick an operation: ")
        num2 = float(input("what is your next number? "))
        answer = operations[selected_operation](num1, num2)
        print(f"{num1} {selected_operation} {num2} = {answer}")
        continue_calculation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if continue_calculation == "y":
            num1 = answer

        else:
            accumulation = False
            print("\n" * 50)
            calculator()
calculator()







