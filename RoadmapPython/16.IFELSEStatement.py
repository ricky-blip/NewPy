# If and Else Statement

print(5*"=" + "IF" + 5*"=")

name = input("Who's your name ")

'''
before program
if condition: action
next program
'''

if name == "Ricky": print(f"Your Name is {name}")
print(f"Welcome back {name}")

print("\n" + 5*"=" + "IF Indentation" + 5*"=")

maname = input("Who's your name ")

if maname == "Rush":
    print(f"Thanks {maname}")
    print(f"Danke {maname}")
print(f"Thanks For Your Service {maname}")

print("\n" + 5*"=" + "ELSE" + 5*"=")

imya = input("Who's your name ")

if imya == "Masha":
    print(f"Thanks {imya}")
    print(f"Danke {imya}")
else:
    print("Wrong Username")
    
print(f"Thanks For Your Time")
