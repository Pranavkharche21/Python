# Exercise 2 - Faulty Calculator


# Step 1: Take user inputs for the operator and two numbers
print("enter the first number")
num1 = input()
operator = input( "enter the operator(+,-,/,*,%): ")
print("enter the second number")
num2 = input()

# Step 2: Check for the faulty conditions first
if operator == "*" and num1 == "45" and num2 == "3":
    print("the answer is 555")
elif operator == "+" and num1 == "56" and num2 =="9" :
    print("the answer is 77")
elif operator == "/" and num1 == "56" and num2 == "6":
    print( "the answer is 4")
elif operator == "+":
    print("the answer is:", int(num1) + int(num2))
elif operator == "-":
    print("the answer is:", int(num1) - int(num2))      
elif operator == "*":
    print("the answer is:", int(num1) * int(num2))
elif operator == "/":
    print("the answer is:", int(num1) / int(num2))
elif operator == "%":
    print("the answer is:", int(num1) % int(num2))
else : 
    print("invalid operator")
