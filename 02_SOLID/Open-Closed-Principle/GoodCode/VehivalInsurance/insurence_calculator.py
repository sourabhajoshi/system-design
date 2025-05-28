from vehical import Vehical
from car import Car
from truck import Truck

class InsurenceCalculator:

    # we can add 
    def insurance_amount(self, vehical:Vehical):
        # print(isinstance(vehical, Car))
        if isinstance(vehical, Car):
            return 1000
        elif isinstance(vehical, Truck):
            return 2000
        else:
            return 100