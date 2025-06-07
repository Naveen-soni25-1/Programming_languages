print("Hello user,\nWelcome to the simple calculator!".title())

guidance = "When done with numbers, enter [done]."
print(guidance.title())

expression = []

# Continue adding numbers and operations
while True:
    value = input("\nWhat is your number: ").strip()
    
    if value.lower() == "done":
        break  # Exit the loop when the user types "done"
    
    try:
        num = float(value)  # Convert input to a number
        expression.append(num)
    except ValueError:
        print("Invalid number, please try again.")
        continue  # Skip this iteration and ask for input again
    
    operation = input("Select operation (+, -, *, /): ").strip()
    if operation.lower() =='done':
        break
    if operation not in {"+", "-", "*", "/"}:
        print("Invalid operation, please try again.")
        continue  # Skip this iteration and ask for input again
    
    expression.append(operation)  # Append the operation to the list

# Perform the calculation
def evaluate_expression(expression):
    """Evaluates the list-based mathematical expression."""
    import operator

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    # Step 1: Handle multiplication and division first
    i = 0
    while i < len(expression):
        if expression[i] in ("*", "/"):
            left = expression[i - 1]
            op = expression[i]
            right = expression[i + 1]
            result = ops[op](left, right)
            expression[i - 1 : i + 2] = [result]
            i -= 1# when we replace slice to result if we don't use this expression we skip to use result in the loop again
        i += 1#maintain normal flow of loop

    # Step 2: Handle addition and subtraction
    i = 0
    while i < len(expression):
        if expression[i] in ("+", "-"):
            left = expression[i - 1]
            op = expression[i]
            right = expression[i + 1]
            result = ops[op](left, right)
            expression[i - 1 : i + 2] = [result]
            i -= 1
        i += 1
# index zero is used because expression convert to a single digit
    return expression[0]

# Check if there are enough elements to calculate
if len(expression) < 3:
    print("Not enough data to calculate.")
else:
    result = evaluate_expression(expression)
    print(f"\nFinal result: {result}")
    
     
    