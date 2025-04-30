def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            sign = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if sign == "+":
                print("Your result is:", num1 + num2)
            elif sign == "-":
                print("Your result is:", num1 - num2)
            elif sign == "*":
                print("Your result is:", num1 * num2)
            elif sign == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print("Your result is:", num1 / num2)
            else:
                print("Invalid operation! Please enter only +, -, *, or /")
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

        # Ask user if they want to calculate again
        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            print("Thanks for using the calculator. Goodbye!")
            break

calculator()
