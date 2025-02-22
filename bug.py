def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  #Correct handling of zero division
    elif b == 0:
        return float('inf') # This will not throw an error, but could result in unexpected behavior in other calculations. 
    else:
        return a / b

result = function_with_uncommon_error(10,0)
print(result)