import json

class Vehical:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        
    def calculate_insurence(self):
        age = 2025 - self.year
        if age > 5:
            return 1000
        return 500
    
    def to_json(self):
        return json.dumps({
            "make" : self.make,
            "model" : self.model,
            "year" : self.year
        })
        
def main():
    vehical = Vehical("Tata", "Tiago", 2020)
    print(f"Vehical details : {vehical.to_json()}")
    print(f"Insurence cost : {vehical.calculate_insurence()}")
    

if __name__ == "__main__":
    main()