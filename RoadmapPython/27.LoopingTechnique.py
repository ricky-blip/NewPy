# Looping with Structure Data

name_game = ['GOW','Splinter Cell','CTR','GTA','NFS'] #list
publisher = ['Santa Monica','Ubisoft','Activision','Rockstar','EA'] #list


print(10*"=" + "Basic Loop" + 10*"=" + "\n")

i = 0 
for game in name_game:
    print(f"No : {i} NameGame : {game}")
    i += 1 # increment


print("\n" + 10*"=" + "Loop Enumerate" + 10*"=")

for index,game in enumerate(name_game): # index just name variabel # auto return value 
    print(f"{index} : {game}")
    
print("\n" + 10*"=" + "ZIP" + 10*"=")  # Combine List

for game,publish in zip(name_game,publisher):
    print(f"{game} Published by {publish}")
    
print("\n" + 10*"=" + "SET" + 10*"=")

playlist = {'Dota2','LOL','Valo','CS'}

for gg in playlist:
    print(gg)

print(10*"-" + "sorted")
for gg2 in sorted(playlist):
    print(gg2)

print("\n" + 10*"=" + "Dictionary" + 10*"=")

playlistD = {'Dota2':'99','LOL':'66','Valo':'44','CS':'77'}

print(10*"-" + "keys")
for D in playlistD.keys():
    print(D)

print(10*"-" + "values")
for E in playlistD.values():
    print(E)

print(10*"-" + "All Items")
for F in playlistD.items():
    print(F)

print(10*"-" + "Spread Item")
for G,H in playlistD.items():
    print(f"{G} and {H}")