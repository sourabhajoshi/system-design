#base class
class Vehical:
    def accelerate(self):
        print("The vehical accelarte")
        
class Car(Vehical):
    def accelerate(self):
        print("The Car accelarte")
        
class Train(Vehical):
    def accelerate(self):
        print("The Train accelarte")
        
class Aeroplane(Vehical):
    def accelerate(self):
        print("The Aeroplane accelarte")
        
vehicals = [Car(), Train(), Aeroplane()]

for vehical in vehicals:
    vehical.accelerate()