#   Python Calculator


operator = input("Enter an operator: + - * /: ")

number1 = float(input("Enter first number: "))

number2 = float(input("Enter second number: "))

if operator == "+":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operator == "-":
    print(f"{number1} + {number2} = {number1 - number2}")
elif operator == "*":
    print(f"{number1} + {number2} = {number1 * number2}")
elif operator == "/":
    print(f"{number1} + {number2} = {number1 / number2}")
else: 
    print(f"Envalid operator: {operator}")
