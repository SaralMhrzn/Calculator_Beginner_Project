def add(a, b):
    output= a+b
    print(output)
    calculator(output) # Continue with the new result
    
def subtract(a, b):
    output= a - b
    print(output)
    calculator(output)

def multiply(a, b):
    output= a * b
    print(output)
    calculator(output)

def divide(a, b):
    output= a / b
    print(output)
    calculator(output)

def start_calculation():
    first_number= float(input("Enter the first number: "))

    print("+\n-\n*\n/")

    while True:
        operator= input("Enter the operator: ")
        if operator in ["+", '-','*', "/"]:
            break
        else:
            print("please enter valid operator [+, -,*, /]: ")
            continue

    next_number= float(input("Enter next number: "))

    # checking operator and calling function related to operator(function mathi xa)
    if operator == "+":
        add(first_number, next_number)
    elif operator == "-":
        subtract(first_number, next_number)
    elif operator == "*":
        multiply(first_number, next_number)
    elif operator == "/":
        divide(first_number, next_number)

# now mathi 1st time calculation garera aayeko output passed as a first number here.
def calculator(output):
    while True:
        continue_calculating= input(f"Enter 'y' to continue calculator with {output} or 'n' to start new calculator or 'x' to exit: ").lower()
        if continue_calculating in ['y', 'n', 'x']:
            if continue_calculating == 'y':
                while True:
                    operator= input("Enter the operator: ")
                    if operator in ["+", '-','*', "/"]:
                        another_number= float(input("Enter another number: "))
                        if operator == "+":
                            add(output, another_number)
                        elif operator == "-":
                            subtract(output, another_number)
                        elif operator == "*":
                            multiply(output, another_number)
                        elif operator == "/":
                            divide(output, another_number)
                        break
                    else:
                        print("please enter valid operator [+, -,*, /]: ")
                        continue
            elif continue_calculating == "n":
                print("Starting a new calculation.")
                start_calculation()
        
            elif continue_calculating== 'x': 
                print("Thanks for using the calculator.")
                exit()
        else:
            print("please enter valid answer [y/n/x]: ")
            continue
start_calculation()
calculator()






    

    