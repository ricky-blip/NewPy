# Scope 

print(5*"=" + "Scope Variabel Local" + 5*"=")

nameCat = 'Jimbon'

def changeNameCat(newName):
    nameCat = newName
    print(f"Change Name Cat = {nameCat}")

changeNameCat('Jinbei')
print(f"So I The Cat name is = {nameCat}") # is not change Variabel

print(5*"=" + "Scope Variabel Global" + 5*"=")

nameCat = 'Jimbon'
foodCat = 'Bolt'

def changeNameCat(newName):
    global nameCat # make variabel to global
    nameCat = newName
    print(f"Change Name Cat = {nameCat}")

def feedingCat(food,name):
    global nameCat,foodCat # make variabel to global
    nameCat = name
    foodCat = food

changeNameCat('Jinbei')        # change value Variabel from Default/after
feedingCat('Whiskas','Anabul') # change value Variabel from Default

print(f"So My Cat name is = {nameCat} and Eating {foodCat}")  # Result change value Variabel from Default