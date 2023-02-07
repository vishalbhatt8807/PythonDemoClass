class A:
    '''Single and multiple inheritance and mutli level example: B inherit A and C clas inherit B ite multi level and
    if class C inherit property of A and B its called Multiple . To inherit property of parent class we have to just define
    class name with another class'''

    def feature1(self):
        print("Feature 1 is working")


    def feature2(self):
        print("Feature 2 is working")

class B (A):

    def feature3(self):
        print("Feature 1 is working")


    def feature4(self):
        print("Feature 2 is working")


class C(B):

    def feature5(self):
        print("Feature 1 is working")

    def feature6(self):
        print("Feature 2 is working")

# Multiple inheritance
class D:
    '''Single and multiple inheritance and mutli level example: B inherit A and C clas inherit B ite multi level and
    if class C inherit property of A and B its called Multiple . To inherit property of parent class we have to just define
    class name with another class'''

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class E:

    def feature3(self):
        print("Feature 1 is working")

    def feature4(self):
        print("Feature 2 is working")


class F(D,E):

    def feature5(self):
        print("Feature 1 is working")

    def feature6(self):
        print("Feature 2 is working")
