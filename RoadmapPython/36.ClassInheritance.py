# Class Inheritance (Turunan Class)

class Uber():
    
    def __init__(self, car, transmision, area):
        self.car = car
        self.transmision = transmision
        self.area = area
        
    def check_id_driver(self):
        print(f"Car : {self.car} | Transmision : {self.transmision} | Area : {self.area}")

class TransportOnline(Uber): # --> Inheritance taking all data from Class 'Uber'
    
    def check_id_driver(self): # replace function from Class 'Uber'
        print("Checking Function in Class TransportOnline")
   
   
Uber1 = Uber('Honda', 'Automatic', 'Palembang')
Uber2 = TransportOnline('Toyota', 'Manual', 'Lampung')

Uber1.check_id_driver()
Uber2.check_id_driver()



