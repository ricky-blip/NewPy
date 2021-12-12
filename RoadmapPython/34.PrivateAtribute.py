# How To Private Atribute

class allies:
    
    __score = 0 # private
    
    def count_score(self, input_score):
        self.__score += input_score
        
    def check_status(self):
        if self.__score >= 500:
            print(f"{self.role} You Are Amazing")
        else:
            print(f"{self.role} You're Totally Weak") 
    
    def __init__(self, input_role,position):
        self.role = input_role 
        self.post = position
        
    def defends(self,argument1):    
        print(f"{self.role} : Defending {argument1}")
        
    def chilling(self,argument2):
        print(f"{self.role} : Slepping {argument2}")

army = allies("AirForce","Country")
police = allies("Police Traffic Light", "City")

print(f"{army.role} in {army.post}")


print(f"{police.role} in {police.post}")


army.defends('Seriously')
police.chilling('Beauty')


print(f"\nThis is Private Atribute=================")

army.count_score(750)
army.check_status()

police.count_score(150)
police.check_status()