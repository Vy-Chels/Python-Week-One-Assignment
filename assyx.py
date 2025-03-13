#Getting user inputs
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Enter the operation(+, -, *, /):")

#Performing the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    #check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Invalid operation."

#Printing the result
print(f"{num1} {operation} {num2} = {result}")
