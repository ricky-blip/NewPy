print("Ibu memberi perintah 'Beli 1 Botol Susu' dan jika ada telur beli 6 butir\n") 

susu = int(input("Masukkan angka 1 untuk membeli 1 botol susu ? "))
telur = int(input("Ada berapa butir telur di toko ? "))

if susu >= 1:
    print("Beli 1 Botol")
     
if telur > 0:
    print(f"Beli Telur {telur} butir")
    
else:
    print(f"Langsung Pulang")
    
print(f"Pulang dengan membawa {susu} botol susu dan {telur} butir telur")
    
    