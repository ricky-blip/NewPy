# Manipulate & Operator String

print("====1. Menyambung String (Concatenate)====")
first_name  = "Ricky"
middle_name = "Noob"
last_name   = "Rinaldy"

full_name   = first_name + " " + middle_name + "'" + (last_name)
print(full_name)

print("\n====2. Calculate length string====")
length = len(full_name)
print("length words" + " " + full_name + " = " + str(length)) # must be casting first to str()

print("\n====3. Operator for string====")
# mengecek apakah ada komponen char/string di dalam string
# checking spesific WORDS in string
r = "z"
status = r in full_name
print("words " + "'" + r + "'" + " there is in " + "\"" + full_name + "\"" +" = " + str(status))

r = "z"
status = r not in full_name
print("words " + "'" + r + "'" + " there is not in " + "\"" + full_name + "\"" +" = " + str(status))

print("\n====4. Repeat string====")
print("hua"*10)
print(15*"hiya")

print("\n====5. Indexing string====")
print("index to-6" + " = " + full_name[6])
print("index to-(-2)" + " = " + full_name[-2])
print("index to-[0:3]" + " = " + full_name[0:3]) #range 0 until 3
print("index to-[1,6,10]" + " = " + full_name[1:18:4]) # 4 is increment

print("\n====6. Smallest & Biggest Item(item terkecil & terbesar)====")
# smallest & biggest string base on ASCII 
print("base on ASCII smallest string : " + min(full_name)) #output is = SPACE
print("base on ASCII biggest string  : " + max(full_name))

print("====how to calculate with ASCII code====")
ascii_code = ord(" ")
print("ASCII code for SPACE is " + str(ascii_code))
ascii_code = ord("y")
print("ASCII code for   y   is " + str(ascii_code))


