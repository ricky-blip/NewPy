# Input User

# data yang dimasukkan pasti STRING
data = input("Ketikkan Apapun : ")
print("Inputan anda =", data, "tipe datanya = ", type(data))

# ---------------INTEGER--------------
# jika kita ingin mengambil int, maka
angka_int = int(input("Masukkan Angka Integer : "))
print("Inputan anda =", angka_int, "tipe datanya = ", type(angka_int))

# ---------------FLOAT--------------
# jika kita ingin mengambil float, maka
angka_float = float(input("Masukkan Angka Float : "))
print("Inputan anda =", angka_float, "tipe datanya = ", type(angka_float))

# ---------------BOOLEAN--------------
# jika kita ingin mengambil boolean, maka harus casting ke Integer dahulu
databool = bool(int(input("Masukkan Nilai Boolean : ")))
print("Inputan anda =", databool, "tipe datanya = ", type(databool))
