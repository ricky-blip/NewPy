# Error Handling = Try and Exception

# Error Syntax
# Error Runtime

# Error Runtime -------------------

# Example 1
'''
try:
    number = int(input("Input Number"))
except ZeroDivisionError:
    print(f"Angka Lu 0 bos, gak bisa dibagi, coba angka lain")
    
except ValueError:
    print(f"Error BOS, harus angka!!!")

print("end")
'''
# Example 2
while True:
    try:
        number1 = int(input("Input you're first number "))
        number2 = int(input("Input you're second number "))
        total = number1/number2
        break
    # General people use
    except Exception:
        print("Error BRO!")
    '''
    except ValueError:
        print("You're Input is not Number")
    except ZeroDivisionError:
        print("You're Input is 0, Please Input Another Number")
    '''    
print(f"Finally You Did it, {number1} / {number2} = {total}")
    
    
"""
    Type of exception errors:
    1. IOError
    2. ImportError(Package)
    3. ValueError
    4. Division by zero
    5. KeyboardInterupted
    6. EOFError   
"""