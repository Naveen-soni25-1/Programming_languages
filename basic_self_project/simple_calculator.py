num1 = float(input("Put first number: "))
operation = input("Select operation (+, -, /, *):")
num2 = float(input("Put second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2  # Fixed: `num` should be `num1`
elif operation == "/":
    result = num1 / num2  # Fixed: `//` should be `/` for float division
elif operation == "*":
    result = num1 * num2
else:
    result = "Invalid operation"

print(result)
  