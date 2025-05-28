from car import Car
from truck import Truck
from insurence_calculator import InsurenceCalculator
from object_formatter import ObjectFormatter

def main():
    car = Car("Tata", "Tiago", 2020)
    truck = Truck("AL", "Al-10115", 2015)
    insurance_calculator = InsurenceCalculator()
    formatter = ObjectFormatter()
    
    print(insurance_calculator.insurance_amount(car))
    print(formatter.vehical_to_json(car))
    
    print(f"truck details : {formatter.vehical_to_json(truck)}")
    print(f"Truck insurance amount : {insurance_calculator.insurance_amount(truck)}")

if __name__ == "__main__":
    main()