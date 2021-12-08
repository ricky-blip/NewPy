# Looping While

# while condition:
#     action
# end of program

num = 0
print(f"number now -> {num}")

while num < 5: # 0 less than 5 is True
    num += 1   # 0 = 0 + 1 until 5
    print(f"number now -> {num}")
    print("Ricky")

print("OK Enough\n")

print(5*"=" + "With Boolean" + 5*"=")
start = True
number = 0 

while start:
    print(f"number now -> {number}")
    if number == 5:
        start = False
        print("Number Founded")
    number += 1
print("END Program\n")

print(5*"=" + "With Else, Break, Continue, Pass" + 5*"=")
numbero = 0

while numbero < 5:

    if numbero == 3: 
        break #-> stop in 3 
        # continue -> infinite loop
        # pass -> nothing happen
    print(f'Number now -> {numbero}')
    numbero += 1
else:
    print(f"End While : {numbero}")
print("END Program\n")



