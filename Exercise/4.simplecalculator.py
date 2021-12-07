# Simple Calculator

print(15*"=" + "Simple Calculator" + 15*"=")

num1        = int(input("Type first number = ")) or float(input("Type first number = ")) 
operator    = input("Type Operator (+,-,x,/) : ")
num2         = int(input("Type second number = ")) or float(input("Type second number = "))

if operator == "+":
    total = num1 + num2
    print(f"Your Input is : {num1} {operator} {num2} = {total} ")
elif operator == "-":
    total = num1 - num2
    print(f"Your Input is : {num1} {operator} {num2} = {total} ")
elif operator == "x" or operator == "*":
    total = num1 * num2
    print(f"Your Input is : {num1} {operator} {num2} = {total} ")
elif operator == "/":
    total = num1 / num2
    print(f"Your Input is : {num1} {operator} {num2} = {total} ") 
else:
    print("ERROR!!!!")

print("\n-----THANKS FOR COMING")
