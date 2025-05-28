from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def get_area(self):
        pass