from vehical import Vehical

class InsurenceCalculator:
    def calculate_insurence(self, vehical: Vehical):
        age = 2025 - vehical.year
        if age > 5:
            return 1000
        return 500