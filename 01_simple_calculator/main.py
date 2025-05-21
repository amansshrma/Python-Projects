# Using try block to catch any invalid input errors (e.g., non-integer inputs)
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    # Asking user to select an operation
    print("What kind of operation do you want to perform?")
    print("Press + for Addition")
    print("Press - for Subtraction")
    print("Press * for Multiplication")
    print("Press / for Division\n")

    oper = input()  # Reading the operation from user

    # Matching the user's operation choice using match case
    match oper:
        case "+":  # If user selected addition
            print(f"Your calculated value of {a} + {b} is: {a+b}")
        case "*":  # If user selected multiplication
            print(f"Your calculated value of {a} * {b} is: {a*b}")
        case "-":  # If user selected subtraction
            print(f"Your calculated value of {a} - {b} is: {a-b}")
        case "/":  # If user selected division
            if(b == 0):
                print(f"You can't divide {a} with 0")  # Handling division by zero
            else:
                print(f"Your calculated value of {a} / {b} is: {a/b}")
        case _:  # Default case if invalid operator is entered
            print("You entered wrong operation")

except Exception as e:
    # Catching and handling any exceptions (e.g., if input is not an integer)
    print("Invalid input: please enter integers only.")
