class StudentData:
    def __init__(self, name, age, marks):
        #  validate parameters, NOT self
        if age <= 0:
            raise ValueError("Age should be positive number")
        
        if marks < 0 or self.marks > 100:
            raise ValueError("Marks should be in b/w 0 and 100")
        
        self.name = name
        self.age = age
        self.marks = marks
        
    def get_details(self):
        return f"Name is {self.name}, age is {self.age} and {self.marks} scored."
    
    
std1 = StudentData("Joshi", -5, 55)
print(std1.get_details())
