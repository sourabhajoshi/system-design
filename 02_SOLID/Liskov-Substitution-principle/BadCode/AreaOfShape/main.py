from rectangle import Rectangle
from square import Square

def main():
    rect = Rectangle(10, 20)
    Sqr = Square(2)
    
    rect.set_width(5)
    rect.set_height(10)
    
    print(f"Area of rectangle is {rect.get_area()}")
    
if __name__ == "__main__":
    main()