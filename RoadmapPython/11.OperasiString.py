data = "this is string"
print(data)
print("type data is = ",type(data))

print('\n==========1. How To create String==========')
'''
    1. with using single quote '...'
    2. with using double quote "..."
'''

data = 'String Using Single Quote'
print(data)

data = "String Using Duoble Quote"
print(data)

print('"I Noob"')
print("'Your Pro'")
print("We're Shit")

print('\n==========2. String Using Symbol( \ )==========')

# making symbol ' to String
print('Let\'s go for Jum\'at Pray')

#backslash
print("C:\\user\\Ricky")

#tab
print("Ricky\t\tRinaldy") # \t is tab

#backspace
print("Ricky \bRinaldy") # \b is for close between string

#newline
print("WITH N ---first line. \nsecond line.") # LF(line feed) -> Unix, MacOS, Linux
print("WITH R ---first line. \rsecond line.") # CR(Carriage Return) -> commodoore, acorn, lisp
print("WITH RN---first line. \r\nsecond line.") # CRLF(line feed Carriage Return) -> Windows

print('\n==========3. String Literal/RAW==========')

# careful (hati-hati)
print('C:\new folder') # wrong path

# using raw string
print(r'C:\new folder')

# multiline literal string and raw
print(r"""
Name    : Ricky
Major   : Associate Degree
Website : ricky-blip.github.io\
""")