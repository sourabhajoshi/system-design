class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height