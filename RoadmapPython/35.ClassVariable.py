class allies:
    
    threat = "toplevel" #variabel class
    
    member = 0
    
    def __init__(self, input_role,position):
        self.role = input_role # self is stick variabel instances
        self.post = position

        allies.member += 1 # increment in variabel instaces 'member'
        
army = allies("AirForce","Country")
police = allies("Police Traffic Light", "City")
blackops = allies("Assasins", "Dark")

army.threat = "spacelevel" # replace/override variabel class to variabel instances


print(allies.threat)
print(army.threat)
print(police.threat)

print(army.__dict__) # dict is for look dictionary instances 'army'

print(allies.member) # adding role member