# Operator in methods

print ("====change case in string====")

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)
salam = salam.lower()
print("lower = " + salam)
salam = salam.capitalize()
print("capital = " + salam)

print ("\n====checking with isX method====")
# check case
greeting = "sist!"
isthat_lowercase = greeting.islower() #result must bool
print(greeting + " is that lower = " + str(isthat_lowercase)) # casting to str first
isthat_uppercase = greeting.isupper() #result must bool
print(greeting + " is that upper = " + str(isthat_uppercase)) # casting to str first

# isalpha()     <-- check is all alphabet
# isalnum()     <-- check alphabet and number
# isdecimal()   <-- check only number
# isspace()     <-- check space,tab, newline \n
# istitle()     <-- check every single alpabet capital

print ("\n====checking component startswith() endswith()====")
whocare = "Ricky Rinaldy 007"
cek_start = whocare.startswith("Ricky")
print("start = " + str(cek_start))

#refactoring (make simple code)
cek_end = "Ricky Rinaldy".endswith("Rinaldy")
print("end   = " + str(cek_end))

print ("\n====merging component join() split()====")
#join
separate = ['I','Don\'t','care']
join = ','.join(separate)
print(separate)
print(join)

join = ' '.join(separate)
print(join)

#split
join = "who_are_you"
print(join.split('_'))

print ("\n====character allocation rjust(), ljust(), center()====")

print(9*"-" + "data" + "-"*9)
#right justify
right = "right".rjust(10) #boundary 10 and place in "right" position
print("|" + right + "|")
#left justify
left = "left".ljust(10) # place in "left" position and boundary 10 
print("|" + left + "|")

#center justify
center = "center".center(10,"/") # place in "center" position and remainder 10 
print("|" + center + "|")

print ("====reverse --> strip()====")
center = "center".strip("/") # remove "/" 
print("|" + center + "|")
right = "right".strip(" ") # remove "space" 
print("|" + right + "|")
left = "left".strip(" ") # remove "space" 
print("|" + left + "|")







