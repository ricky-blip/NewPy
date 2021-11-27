print("----Operasi Tambah ( + )----")
a = 1 
b = 2
tambah = a + b
print(a, "+", b, "=", tambah)

print("----Operasi Kurang ( - )----")
c = 5 
d = 2
kurang = c - d
print(c, "-", d, "=", kurang)

print("----Operasi Kali ( * )----")
e = 10 
f = 2
kali = e * f
print(e, "*", f, "=", kali)

print("----Operasi Bagi ( / )----")
g = 20 
h = 7
bagi = g / h
print(g, "/", h, "=", bagi)

print("----Operasi Eksponen atau Pangkat ( ** )----")
i = 5 
j = 5
pangkat = i ** j
print(i, "**", j, "=", pangkat)

print("----Operasi Modulus atau sisa bagi ( % )----")
k = 20 
l = 3
mod = k % l
print(k, "%", l, "=", mod)

print("----Operasi Floor Division kebalikan dari MOD ( // )----")
m = 20 
n = 3
mod = m // n
print(m, "//", n, "=", mod)

print ("==========================================")
print ("prioritas operasi, operational precendence")
print ("==========================================")

'''
    1. ()
    2. exponen atau pangkat **
    3. perkalian *
    4. pembagian /
    5. modulus %
    6. floor divison //
    7. tambah +
    8. kurang -
'''
a = 3
b = 2
c = 4

hasil = a ** b * c + a / b - b % c // a

print(a,'**',b,'*',c,'+',a,'/',b,'-',b,'%',c,'//',a,'=',hasil) 

