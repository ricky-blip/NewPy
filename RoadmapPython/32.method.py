# Method --> is function inside class 

# ======= CLASS ==========
class allies:
    # pass    # use 'pass' is for empty
    friend = 'friend' # -> Atribute
    
    # --> Method # "self" for identify owned -----------
    def defends(self,argument1):    
        # print('Defending')
        print(f"{self.friend} : Defending {argument1}")
        
    def chilling(self,argument2):
        print(f"{self.friend} : Slepping {argument2}")
    
# MAIN PROGRAM ----------------------    
army   = allies()
police = allies()

# change name
army.friend   = "Marine"
police.friend = "Police Departement"

# print 
army.defends('Seriously')
police.chilling('Beauty')

