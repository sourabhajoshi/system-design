# Parent class
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def info(self):
        return f"This is a ${self.brand} device and priced at ${self.price}."
    
# Intermediate class
class SmartPhone(Device):
    #this class can have accees of device attribute and methods
    def __init__(self, brand, price, camera):
        super().__init__(brand, price)
        self.camera = camera
        
    def details(self):
        return f"{self.brand} smart phone with a {self.camera}MP camera priced at ${self.price}."
    
# create object of smart phone
iphone = SmartPhone("Apple", 499, 12)
print(iphone.info())
print(iphone.details())

# Child class
class ProSmartPhone(SmartPhone):
    def __init__(self, brand, price, camera, stylus):
        super().__init__(brand, price, camera)
        self.stylus = stylus
        
    def pro_details(self):
        return f"{self.brand} pro module with a {self.camera}MP camera, {self.stylus} enabled stylus and priced at ${self.price}."

# create object of pro smart phone
galaxy_pro = ProSmartPhone("Samsung", 999, 108, "s-115")
print(galaxy_pro.info())
print(galaxy_pro.details())
print(galaxy_pro.pro_details())