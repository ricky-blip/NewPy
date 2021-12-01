# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

# Operasi Aritmatika
a = 10 # adalah assignment
print("nilai a =", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi",a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi",a)

a /= 5 # artinya adalah a = a / 5
print("nilai a /= 5, nilai a menjadi",a)

b = 20
print("nilai b =",b)

b %= 3 # artinya adalah b = b % 3
print("nilai b %= 3, nilai b menjadi",b)

b = 20
print("nilai b =",b)

b //= 3 # artinya adalah b = b // 3
print("nilai b //= 3, nilai b menjadi",b)

c = 20
print("nilai c =",c)

c **= 3 # artinya adalah c = c ** 3
print("nilai c **= 3, nilai c menjadi",c)

print("\n=============================Bitwise\n")
# Operasi Bitwise
#OR
d  = True
print("nilai d=",d)
d |= False # artinya adalah d = d | False
print("nilai d |= False, nilai c menjadi",d)
d |= True # artinya adalah d = d | True
print("nilai d |= True, nilai c menjadi",d)

#AND
d  = True
print("nilai d=",d)
d &= False # artinya adalah d = d & False
print("nilai d &= False, nilai c menjadi",d)
d &= True # artinya adalah d = d & True
print("nilai d &= True, nilai c menjadi",d)

#XOR
d  = True
print("nilai d=",d)
d ^= False # artinya adalah d = d ^ False
print("nilai d ^= False, nilai c menjadi",d)
d ^= True # artinya adalah d = d ^ True
print("nilai d ^= True, nilai c menjadi",d)

#SHIFT
e = 0b0101000
print("nilai e =",format(e,'07b'))
e >>= 2 # artinya adalah e = e >> 2
print("nilai e >>= 2, nilai e menjadi",format(e,'07b'))
e <<= 1 # artinya adalah e = e << 1
print("nilai e <<= 1, nilai e menjadi",format(e,'07b'))



