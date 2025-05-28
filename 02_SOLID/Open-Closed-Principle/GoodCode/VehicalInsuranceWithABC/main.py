from car import Car
from truck import Truck
from insurance_calculator import InsuranceCalculator
from object_formatter import ObjectFormatter

def main():
    car = Car("Tata", "Tiago", 2020)
    truck = Truck("AL", "AL-150", 2012)
    insurance_amount = InsuranceCalculator()
    object_formatter = ObjectFormatter()
    
    print(insurance_amount.insurance_amount(car))
    print(insurance_amount.insurance_amount(truck))
    
    print(object_formatter.vehical_to_json(car))
    print(object_formatter.vehical_to_json(truck))


if __name__ == "__main__":
    main()