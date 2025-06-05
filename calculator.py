# Python Calculator


operator = input("Enter an Operator (+ - * /): ")

num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

# When we accept user input, they are string data types. If the numbers are strings, they 
# will just be joined together, they will not be added etc
# Solution: Typecast the figures into numbers or floats

# print(num1 + num2)

if operator == "+":
    result = num1 + num2
    print(round(result)) # Round to the nearest whole integer
elif operator == "-":
    result = num1 - num2
    print(round(result)) # Round to the nearest whole integer
elif operator == "*":
    result = num1 * num2 
    print(round(result)) # Round to the nearest whole integer
elif operator == "/":
    result = num1 / num2
    print(round(result)) # Round to the nearest whole integer
else:
    print(f"{operator} Invalid , Kindly choose again a valid operator.")


# https://github.com/brucetravis/PYTHON.git