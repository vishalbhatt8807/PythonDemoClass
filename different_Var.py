class Car:
    # There are 2 variable Instance and class (static) Var. If define inside the INIT is class Instance var and if
    # define inside class is called Class or static var.
    wheel = 4  # Class or static var

    def __init__(self):
        self.mil = 10  # instance var
        self.com = "BMW"



c1 = Car()
c2 = Car()

c1.wheel = 5 
print(c1.mil, c1.com, c1.wheel)
print(c2.mil, c2.com, c2.wheel)
