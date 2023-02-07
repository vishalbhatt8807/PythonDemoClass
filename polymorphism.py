'''#Polymorphism types - one way many form
# Duck Typing
# operator Overloading
# Method Overloading - Python has no overloading
# Method Overriding'''

class pyCharm:
    def execute(self):
        print("Compiling")
        print("Executing")


class pyCharm1:
    def execute(self):
        print("Spell check")
        print("Conversion rate")
        print("Compiling")
        print("Executing")

class Laptop:
    def code(self,ide):
        ide.execute()
# in future if need to change execute method than can we do that Yes Duck typing support it pycharm to pycharm1

ide = pyCharm1()

lap1 = Laptop()
lap1.code(ide)

#Operator Overloading

#2 + 3 (2and 3 is operand and + is operator)
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 > m2:
            return True
        else:
            return False



s1 = Student(58,50)
s2 = Student(45,56)

s3 = s1 + s2

print(s3.m1)

if s1 > s2:
    print("S1 is wins")
else:
    print("S2 Win")
#__add__(), __sub()__ etc are magic method which can be over  ride as per over need.

#print(int.__add__())
#print(str.__add__())

#Method Overloading is not concept in python but we can use it by argument value pass as None for example

class Students:

    def total(self,a=None,b=None,c=None):
         if a!= None and b != None and c != None:
             return print(a + b + c)
         elif a!= None and b != None:
             return print(a + b)
         elif a!= None:
            return print(a)
         else:
             return print(0)
a1 = Students()

a1.total()

#Method overriding - for example if i dont have phone and someone ask me which phone you have multiple time than and my papa
# having Nokia phone than ill tell to my friend also as i have Nokia phone but once ill get personal phone like Motorola than
# will tell Motorola i have instead Nokia. hence Motorola has override on Nokia.


class W:
    def show(self):
        print("Nokia")

class X(W):
    def show(self):
        print("Motorola")
a1 = X()
a1.show()
