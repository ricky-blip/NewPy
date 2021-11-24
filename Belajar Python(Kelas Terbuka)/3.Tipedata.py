# tipe data: Angka satuan (integer)
data_integer = 1
print("data =", data_integer) 
print("bertipe = ", type(data_integer))

print("---------------------------------------")

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data =", data_float) 
print("bertipe = ", type(data_float))

print("---------------------------------------")

# tipe data: kumpulan karakter (string)
data_string = "thanos"
print("data =", data_string) 
print("bertipe = ", type(data_string))

print("---------------------------------------")

# tipe data: biner true/false (boolean)
data_bool = True
print("data =", data_bool) 
print("bertipe = ", type(data_bool))

print("---------------------------------------")
print("---------------------------------------")

## tipe data khusus

# bilangan kompleks
data_complex = complex(1,2) #angka 1 real angka 2 imaginer(j)
print("data =", data_complex) 
print("bertipe = ", type(data_complex))

print("---------------------------------------")

# tipe data dari bahasa C

from ctypes import c_double

data_cdouble = c_double(1.5)
print("data =", data_cdouble) 
print("bertipe = ", type(data_cdouble))








