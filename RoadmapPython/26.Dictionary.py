# Dictionary 
# is structure data associatif used mapping

# member1 = {key:value,key:value}

print(15*"=" + "How to Print Dictionary" + 15*"=" + "\n")
member1 = {"ID":1, "Name":'Ricky', "Jobs":'Freelancer'} 

print(f"Type Data is = {type(member1)}")
print(member1)

print("\n" + 10*"=" + "How to Access Dictionary" + 10*"=" + "\n")
member2 = {"ID":2, "Name":'Ucup', "Jobs":'Service'} 

print(member2)

print(f"\nPrint Spesific   = {member2['Name']}") # print from value ID(Key)
print(f"Print only key   = {member2.keys()}") # print all only keys
print(f"Print only value = {member2.values()}") # print all only values
print(f"Print all items  = {member2.items()}") # print all items

print("\n" + 10*"=" + "Create List with Dictionary" + 10*"=" + "\n")

memberlist = {1:member1,2:member2}

print(memberlist)
