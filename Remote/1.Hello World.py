'''
Semua Sintaksis Dasar bahasa Pemrograman terdiri dari:
1. Sekuensial   : Langkah Berurutan
2. Percabangan  : Langkah melompat jika kondisi terpenuhi
3. Perulangan   : Mengulang Langkah yang sama berkali-kali sampai kondisi terpenuhi
'''

#Sekuensial example code
# a = 'Ricky'
# print(f"Hallo Universe, {a}")

'''
2000 leap year
2100 not leap year
2400 leap year
1990 not leap year
1992 leap year
'''

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == True or year % 100 == leap and year % 400 == True:
        pass
    
    return leap

year = int(input())
print(is_leap(year))

