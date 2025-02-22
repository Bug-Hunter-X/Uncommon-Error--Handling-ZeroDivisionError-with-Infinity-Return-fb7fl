def function_with_improved_error_handling(a, b):
    if a == 0:
        return 0
    elif b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    else:
        return a / b

try:
    result = function_with_improved_error_handling(10, 0)
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")

#Example of a function using the improved error handling function
def calculate_something(x, y):
    try:
        intermediate_result = function_with_improved_error_handling(x, y)
        final_result = intermediate_result * 2
        return final_result
    except ZeroDivisionError as e:
        print(f"Calculation failed: {e}")
        return None

print(calculate_something(5,2))
print(calculate_something(5,0))