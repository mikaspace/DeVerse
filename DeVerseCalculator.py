def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    while True:
        print("\n3A DeVerse Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Calculator closed.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
            operation = "Division"

        print(f"{operation} Result: {result}")

calculator()
