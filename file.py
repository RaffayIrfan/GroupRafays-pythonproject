def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Use '+', '-', '*', or '/'."

result_add = calculate(10, 5, '+')
print(f"10 + 5 = {result_add}")

result_sub = calculate(50.5, 12, '-')
print(f"50.5 - 12 = {result_sub}")

result_mul = calculate(7, 8.5, '*')
print(f"7 * 8.5 = {result_mul}")

result_div = calculate(100, 4, '/')
print(f"100 / 4 = {result_div}")

result_zero_div = calculate(9, 0, '/')
print(f"9 / 0 = {result_zero_div}")

result_invalid = calculate(15, 3, '%')
print(f"15 % 3 = {result_invalid}")