from abc import ABC, abstractmethod

# Now we can not create Vehical object. Bcz we used ABC class.
class Vehical(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    @abstractmethod
    def calculate_insurance_cost(self):
        pass