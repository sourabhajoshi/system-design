from object_formatter import ObjectFormatter
from vehical import Vehical
from insurence_calculator import InsurenceCalculator

def main():
    vehical = Vehical("Tata", "Tiago", 2020)
    insurence_calculator = InsurenceCalculator()
    formatter = ObjectFormatter()
    
    print(f"Insurence cost : {insurence_calculator.calculate_insurence(vehical)}")
    
    
if __name__ == "__main__":
    main()