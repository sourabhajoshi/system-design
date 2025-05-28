from vehical import Vehical

class Car(Vehical):
    def calculate_insurance_cost(self):
        age = 2025-self.year
        if age > 5:
            return 800
        else:
            return 500
        
    def refuel(self):
        print(f"Refuling car with petrol.")