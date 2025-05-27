class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def appy_discount(self, dic_amount):
        return f"Actual price : {self.price} and after discount {self.price - self.price/10}"
    
book1 = Book("JS", "Joshi", 250)
book2 = Book("CS", "Kulkarni", 300)

result = book1.appy_discount(10)
print(result)