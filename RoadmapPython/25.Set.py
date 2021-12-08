# set, himpunan:
# not sequence

print(10*"=" + "HOW TO MAKE \"SET\" " + 10*"=")

print("\n" + 10*"-" + "1" + 10*"-")
supervillain = {"Loki","Thanos","Madara","KANG"}

print(type(supervillain))
supervillain.add("Joker")

print(supervillain)

print("\n" + 10*"-" + "2" + 10*"-")
supervillain = set()

supervillain.add("Joker")
supervillain.add("Galactus")
supervillain.add("Darkseid")
supervillain.add(666)

print(supervillain)

print("\n" + 10*"-" + "3 SLICING" + 10*"-")

odd   = {1,3,5,7,9} 
even  = {2,4,6,8,10}
prime = {2,3,5,7}

print(f"Combine odd and even  = {odd.union(even)}")
print(f"Slicing odd and prime = {odd.intersection(prime)}")


