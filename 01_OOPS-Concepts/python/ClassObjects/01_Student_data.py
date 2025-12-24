class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        
    # def get_details(self):
    #     return "name is {0}, age is {1} and {2} marks scored".format(self.name, self.age, self.marks)
    
    def get_details(self):
        return f"name is {self.name}, age is {self.age} and {self.marks} scored"
    
std1 = Student('Joshi', 25, 85)
print(std1.get_details())