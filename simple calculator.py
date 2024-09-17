# Mini Project of Simple Calculator in Python

# First we Take input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /)")
num2 = float(input("Enter second number: "))

# Check the operator and perform the calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator"

# Output the result
print(result)
