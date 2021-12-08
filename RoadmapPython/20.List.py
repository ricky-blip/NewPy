# List 

Data1 = [1,7,4,6,3,2,8,4,1] # start from 0
print(f'Data List = {Data1}' + "\n")

print(5*"=" + "Access List" + 5*"=")
Subdata1 = Data1[2] 
Subdata2 = Data1[-5] # start from 1 end

print(f'Data 2nd  = {Subdata1}')
print(f'Data -5th = {Subdata2}')

print("\n" +5*"=" + "Slicing List" + 5*"=")
Subdata3 = Data1[3:8] # Output start 3 until 8, in 8 not count
Subdata4 = Data1[-3:] # start from end 3
Subdata5 = Data1[:5]  # start until 5 

print(f'Slicing Data from 3 to 8  = {Subdata3}')
print(f'Slicing Data from end 3   = {Subdata4}')
print(f'Slicing Data from first 5 = {Subdata5}')

print("\n" +5*"=" + "Extend Data List" + 5*"=")
Data2 = [100,200,300,400,500,600,700,800,900] # start from 0

Data3 = Data1 + Data2
print(Data3)

print("\n" +5*"=" + "Change Data List" + 5*"=")
print(f'Before Change = {Data1}')
Data1[1] = 94 # Change Data 1 = 94

print(f'After Change  = {Data1}')

print("\n" +5*"=" + "Change Data List with Slicing" + 5*"=")
print(f'Before Change = {Data1}')
Data1[1:4] = [55,66,77] # Change Data 1-4 to 55,66,77

print(f'After Change  = {Data1}')

print("\n" +5*"=" + "Copy Data List" + 5*"=")
print(f'Original Data = {Data2}')

x = Data2 [:] # Copying Data2 to x with code --> [:]
x[3] = 888 # Change Data 3 = 888

print(f'Original Data = {Data2}')
print(f'Copy Data     = {x}')

print("\n" +5*"=" + "List inside List (Multidimensional)" + 5*"=")
y = [Data1,Data2]
print('[Index-0 = Data1] , [Index-1 = Data2]')
print(y)

print("\n" +5*"=" + "How to Access List Multidimensinal" + 5*"=")

z = y [0] [3]
print(f'Your Access Data from Index-0 Data-3 = {z}')

print("\n" +5*"=" + "Method List" + 5*"=")
Data4 = [11,22,33,44,55]
print(f'Data4             = {Data4}')

Data4.append(99) # ADD data
print(f'Add data in Data4 = {Data4}')

print(50*"-")
Data4.extend('extnd') # EXTEND data
print(f'Extend data in Data4 = {Data4}')

print(50*"-")
Data4.insert(6,'PC') # INSERT data
print(f'INSERT data in Data4 = {Data4}')

print(20*"-" + "Count" + 20*"-")
totalPC = Data4.count('PC')
print(f"Total PC is : {totalPC}")

print(20*"-" + "Remove" + 20*"-")
Data4.remove('PC')
print(f"REMOVE data in Data4 = {Data4}")

print(20*"-" + "Reverse" + 20*"-")
Data4.reverse()
print(f"REVERSE data in Data4 = {Data4}")

print(20*"-" + "COPYING" + 20*"-")
stuffs = Data4.copy()
stuffs.append('Calculator')
print(f"Data in stuffs with append = {stuffs}")
print(f"Data original              = {Data4}")

print("\n" +5*"=" + "Function List" + 5*"=")
Length_list = len(Data4)

print(f'Total Value List in Data4 = {Length_list}')





