# How To Input and Output to file Text .txt 

'''
w   = write mode     / mode menulis dan menghapus file lama ,jika file tidak ada maka akan dibuat file baru 
r   = read mode only / hanya bisa baca
a   = appending mode / menambahkan data di akhir baris
r+  = write and read mode
'''

print(15*"=" + " Create File Text " + 15*"=")

file = open("data37.txt",'w')

file.write("This is data text created used by Python")
file.write("\nLine 2")
file.write("\nLine 3")

file.close

print(15*"=" + " Reading File Text " + 15*"=")

file2 = open("data37.txt",'r')

print("\nRead perCharacter---------------------")
# print(file2.read(15)) # mean print 15 character

print("\nRead perLine---------------------")
print(file2.readline()) # 1st line
print(file2.readline()) # 2nd line etc

print(15*"=" + " Appending File Text " + 15*"=")

file3 = open("data37.txt",'a')

file3.write("\nThis line made by appending mode")

file3.close()





