from rectangle import Rectangle

class Square(Rectangle):
    
    def set_width(self, width):
        self.width = width
        self.height = width #Forces height to be same as width
        
    def set_height(self, height):
        self.width = height #Forces width to be same as height
        self.height = height