# Exercise 2 - Faulty Calculator

# Step 1: Take user inputs for the operator and two numbers
operator = input("Enter the operator (+, -, *, /): ").strip()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Step 2: Check for the faulty conditions first
if num1 == 45 and num2 == 3 and operator == '*':
    print("Result:", 555)
elif (num1 == 56 and num2 == 9 and operator == '+') or (num1 == 9 and num2 == 56 and operator == '+'):
    print("Result:", 77)
elif num1 == 56 and num2 == 6 and operator == '/':
    print("Result:", 4)

# Step 3: If not faulty, perform correct calculations
elif operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator entered!")