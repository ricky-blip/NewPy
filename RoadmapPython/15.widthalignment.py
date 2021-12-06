# Width and Multiline

# Data
data_nama = "Tesla"
data_umur = 10
data_tinggi = 200.5
data_nomor_rumah = 488

print(5*">" + "string standard")
data_string = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Rumah ={data_nomor_rumah}"
print(data_string)

print("\n" + 5*">" + "string multiline/enter")
data_string = f"Nama = {data_nama} \nUmur = {data_umur} \nTinggi = {data_tinggi} \nRumah = {data_nomor_rumah}"
print(data_string)

print("\n" + 5*">" + "string multiline/triplets")
data_string = f"""
Nama   = {data_nama} 
Umur   = {data_umur} Years Old
Tinggi = {data_tinggi} cm
Rumah  = {data_nomor_rumah}"""
print(data_string)

print("\n" + 5*">" + "string setting width")
data_string = f"""
Nama   = {data_nama:>12}
Umur   = {data_umur} Years Old
Tinggi = {data_tinggi:>9} cm
Rumah  = {data_nomor_rumah:>12}""" 
print(data_string)