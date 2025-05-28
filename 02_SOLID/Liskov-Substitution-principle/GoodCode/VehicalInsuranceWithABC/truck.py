from vehical import Vehical

class Truck(Vehical):
    def calculate_insurance_cost(self):
        age = 2025-self.year
        if age > 5:
            return 1800
        else:
            return 1500
        
    def refuel(self):
        print(f"Refuling truck with deesel.")