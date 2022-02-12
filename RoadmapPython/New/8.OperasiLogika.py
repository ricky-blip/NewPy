# Logical Operator

# not, or, and, xor

print('====NOT====')
a = True
b = not a
print('data a =',a)
print('---------------NOT')
print('data b =',b)

print('====OR====') 
# jika salah satu True maka akan True & jika keduanya False maka akan False
c = True
d = False
e = c or d 
print(c,'OR',d,'=',e)

c = False
d = True
e = c or d 
print(c,'OR',d,'=',e)

c = True
d = True
e = c or d 
print(c,'OR',d,'=',e)

c = False
d = False
e = c or d 
print(c,'OR',d,'=',e)

print('====AND====') 
# akan jadi TRUE ketika True AND True
c = True
d = False
e = c and d 
print(c,'AND',d,'=',e)

c = False
d = True
e = c and d 
print(c,'AND',d,'=',e)

c = True
d = True
e = c and d 
print(c,'AND',d,'=',e)

c = False
d = False
e = c and d 
print(c,'AND',d,'=',e)

print('====XOR====') 
# akan True jika salah satu True, sisanya False 
c = True
d = False
e = c ^ d 
print(c,'XOR',d,'=',e)

c = False
d = True
e = c ^ d 
print(c,'XOR',d,'=',e)

c = True
d = True
e = c ^ d 
print(c,'XOR',d,'=',e)

c = False
d = False
e = c ^ d 
print(c,'XOR',d,'=',e)