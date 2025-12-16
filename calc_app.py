# a program to do simple calculation and save them to a file

# a simple calculator
def calculator():
    """
    Do calculation with two numbers and an operator

    Args:
    num1 (float): The first number
    operator ("*", "/", "+", "-")
    num2(float): The second number

    return:
    The result of the calculation

    """

    print("Welcome to the calcutator")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter an operator('+', '-', '*', '/'): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                answer = num1 + num2
            elif operator == "-":
                answer = num1 - num2
            elif operator == "*":
                answer = num1 * num2
            # handle division by zero
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                else:
                    answer = num1 / num2
            # handle the use of wrong operator
            else:
                raise ValueError("Invalid operator. Use '+', '-', '*', '/'")      
        

            equation = f"{num1} {operator} {num2} = {answer}"

            print("result", equation)
        # ask the user for numbers to calculate and then add to a file equations.txt
            with open("equations.txt", "a") as file:
                file.write(equation + "\n")
                print("Equation saved to equations.txt")
                break
        except Exception:
            print("Invalid input")

# print equations from the file
def display_equation():
    """
    Print stored equations when file exists
    """
    try:
        with open("equations.txt", "r") as file:
            content = file.readlines()
            print(type(content))
            if content == "":
                print("No equations found")
            else:
                for line in content:
                    print(line)
    except FileNotFoundError:
        print("file doesn't exist")

# a function for the main menu

def calc():
    """Main menu loop for the calculator app."""
    print("=== Welcome to calc_app ===")

    while True:
        print("\nChoose an option:")
        print("1 - Perform a calculation")
        print("2 - View previous calculations")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            display_equation()
        elif choice == "3":
            print("exiting the calculator app")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    calc()
