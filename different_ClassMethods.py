class Student:
    """There are 3 type of methods , Instance method, class method and static method. There are 2 more subtype of method
# Accessor which just return value like getter method and Mutator method is which update value like setter method
# Instance method call using self keyword , class method class using cls and has to define a decorator @classMethod
# which use to class variable and static method has difned to call static var and defined without any argument and
# @staticMethod decorator"""
    schoolName = "AbC"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def get_schoolName(cls):
        return cls.schoolName

    @staticmethod
    def infoClass():
        print("This is a demo class")

    def avg(self):
       return (self.m1 + self.m2 + self.m3)/3

s1 = Student(23,24,24)
s2 = Student(34,34,35)

Student.infoClass()
print(s1.avg(),s2.avg())
print(Student.get_schoolName())


