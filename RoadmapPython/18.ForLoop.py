# Looping FOR

print("---manual loop---")
num = 1
print(num)
num = num + 1
print(num)
num = num + 1
print(num)

print(15*"=" + "For with List" + 15*"=")

# for condition:
#     action

numbers1 = [0,1,2,3,4] # this is list
print(f"Number list : {numbers1} \n")

for i in numbers1:
    print(f"i now -> {i}")
print("End of Program\n")

print(15*"=" + "For with Range" + 15*"=")

for i in range(6):
    print(f"i now -> {i}")
print("End of Program\n")


for i in range(1,3):
    print(f"i now -> {i}")
print("End of Program\n")

for i in range(0,20,5): # 5 is increment
    print(f'i now -> {i}')
print("End of Program\n")

print(15*"=" + "For with Range,if else,break" + 15*"=")
# Find Number you want
findnum = 3

for i in range(0,5):
    print(i)

    if i is findnum:
        print(f'Found Number in Range 0-5 = {i}')
        break # Terminate Loop
else:
    print('Not Found in Range 0-5')
print("End of Program\n")

print(15*"=" + "For with Continue" + 15*"=")
# Checking Number
for i in range(0,5):
    if i == 2:
        print(f'I Found {i}')
        # continue for next step
        pass
    print(f"Loop now -> {i}")
else:
    print("NOT FOUND")

print("End of Program\n")

print(15*"=" + "For with String" + 15*"=")

data_str = "The Best" # looping perAlphabet

for string in data_str:
    print(string)
print("End of Program\n")






