# Casting = merubah satu tipe data ke tipe data lain

print("--------------INTEGER----------------")

data_int = 9;
print("data = ", data_int, ",type = ", type(data_int))

# cara konversinya
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0

print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

print("---------------FLOAT-----------------")
data_float = 7.1;
print("data = ", data_float, ",type = ", type(data_float))

# cara konversinya
data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0   

print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

print("---------------STRING-----------------")
data_str = "0";
print("data = ", data_str, ",type = ", type(data_str))

# cara konversinya
data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str)  # false jika string kosong

print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_bool, ",type = ", type(data_bool))

print("---------------BOOLEAN-----------------")
data_bool = True;
print("data = ", data_bool, ",type = ", type(data_bool))

# cara konversinya
data_int = int(data_bool)
data_float = float(data_bool)
data_str = bool(data_bool)  

print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_str, ",type = ", type(data_str))