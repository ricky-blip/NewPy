class allies:
    # pass    # use 'pass' is for empty
    friend = 'friend' # -> Atribute
    
police = allies()
army   = allies()

# change name
police.friend = "Police Departement"
army.friend   = "Marine"

print(police)
print(army)

print(police.friend)
print(army.friend)

