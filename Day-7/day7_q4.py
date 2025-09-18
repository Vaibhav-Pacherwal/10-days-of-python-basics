# create student class which takes name and 
# marks of 3 subjects as arguments and also create a method to return average.

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg_marks(self):
        return (self.m1+self.m2+self.m3)/3
    
s1 = Student("Vaibhav", 12, 13, 14)
print(s1.avg_marks())