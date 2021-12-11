# Use __init__()

class allies:
    
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