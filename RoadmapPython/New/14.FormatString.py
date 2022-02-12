# FORMAT STRING

print("==========Example Generic==========")

print("-----STRING-----")
yourname = "luffy"
# str = "hello " + yourname
# print(str)
format_str = f"yow {yourname}" # how to format string
print(format_str)

print("\n-----BOOLEAN-----")
boolean = True
format_str = f"boolean = {True}" # how to format string
print(format_str)

print("\n-----NUMBER(float)-----")
number = 555.5
# thenumber = "number = " + str(number)
# print(thenumber)
format_str = f"float = {number}" # how to format string
print(format_str)

print("\n-----INTEGER-----")
integer = 77
format_str = f"integer = {integer:d}" # "d" is not important just for knowing number
print(format_str)

print("\n-----NUMBER THOUSANDS/million-----")
thousands = 15000000
format_str = f"numberthousands = {thousands:,}" # "," is for dot 
print(format_str)

print("\n-----DECIMAL-----")
decimal = 777.62035
format_str = f"decimal = {decimal:.3f}" # ".3f" is for print behind comma
print(format_str)

print("\n-----LEADING ZERO-----")
decimal = 777.62035
format_str = f"decimal = {decimal:08.3f}" # "08" is for print total number
print(format_str)

print("\n-----SHOWING SYMBOL + or - ------")
minus   = -50.23456
plus    = 40
format_strm = f"minus = {minus:+.1f}"
format_strp = f"plus = {plus:+d}" 
print(format_strm)
print(format_strp)

print("\n-----FORMATING percent------")
percent = 0.75
format_percent = f"percent = {percent:.1%}" 
print(format_percent)

print("=======\nFormating String Aritmatic Operator=======")
price = 1000000
total = 8

format_string = f"price total = Rp.{price*total:,},00"
print(format_string)

print("=======\nFORMAT NUMBER TO BINARY, OCTAL, HEXADECIMAL=======")

number = 256
frmt_binary = f"binary = {bin(number)}"
frmt_octal  = f"octal  = {oct(number)}"
frmt_hexa   = f"hexa   = {hex(number)}"

print(frmt_binary)
print(frmt_octal)
print(frmt_hexa)