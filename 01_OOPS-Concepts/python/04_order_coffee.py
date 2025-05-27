class CoffeeOrder:
    def __init__(self, customer_name, drink_type, size):
        self.customer_name = customer_name
        self.drink_type = drink_type
        self.size = size
        
        #private attribute (start with __name (double underscore))
        self.__price = 5.0
        
    # public method to display order summary
    def get_order_summary(self):
        return f"{self.customer_name} ordered a {self.drink_type} {self.size}."
    
    # private method to calculate price
    def __calculate_price(self):
        return f"Total : ${self.__price}"
    
    # public method to safely access the price
    def get_price(self):
        return self.__calculate_price()

# create an ordered
order = CoffeeOrder("Joshi", "Coffee", "L")
print(order.get_order_summary()) #access public methods

# access private attributes : Raise ERROR
# print(order.__price)
# print(order.____calculate_price())
    
    