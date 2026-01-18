while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Choose an Operation (1 -5): ")

    if choice == '5':
        print("Calculator closed.")
        break

else:
    print("Invalid choice. Please try again.")