class Student:
    ''' A class inside a class can be create but why we need class inside a class for example student details you have
    mentioned now you need detail of student laptop but not only name we required whole config detail which we can pass through
    argument also but it wont looks good hence other way create inner class and call it. to call inner class we have to define
    or create object in outer class consturator '''

    def __init__(self, name, rollno):
        self.name = name
        self.rollnumber = rollno
        self.lap = self.Laptop("windows","OS5","8")

    def show(self):
        print(self.name, self.rollnumber)
        self.lap.show()

    '''Now need a laptop detail of student'''

    class Laptop:
        def __init__(self, name, os, ram):
            self.name = name
            self.os = os
            self.ram = ram

        def show(self):
            print(self.name, self.os, self.ram)


s1 = Student("Vishal", 59)
s1.show()
#Student.Laptop("Window","5","8").show()
