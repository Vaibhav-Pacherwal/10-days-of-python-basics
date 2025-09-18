## class.attr and object.attr
class Student:
    college_name = "Netaji Subhas University of Technology"
    name = "anonymous" # class attr
    def __init__(self, name, roll_no):
        self.name = name # obj attr > class attr
        self.roll_no = roll_no

    print("These guy will become the greatest developer in the world.")

s1 = Student("Vaibhav", "2023UCD2139")
print(s1.name)
print(s1.roll_no)
print(s1.college_name)
print()
s2 = Student("Atishay", "2023UCD3034")
print(s2.name)
print(s2.roll_no)
print(s1.college_name)
print()
s3 = Student("Gaurav", "2023UCD2143")
print(s3.name)
print(s3.roll_no)
print(s1.college_name)
print()