class A:
    def __init__(self):
        print("A in init")

    def feature1(self):
        print("Feature 1")


class B:
    def __init__(self):
        super().__init__()
        print("B in init")

    def feature3(self):
        print("Feature 1")


#a1 = B() # it will print only B class constructor even it inheritance A class but if we have to print class A constructore than
        # use super() keyword

#Method Resolution Order (MRO)-> Alway call from left to right for example class C call A and B inheritance and we use super() keyword
#to extract method or constructor of parent class than it alway start from left to right that means it will call A class

class C(A,B):
    def __init__(self):
        super().__init__()
        super().feature3()
        print("C in init")

    def feature3(self):
        print("Feature 1")

a1 = C()