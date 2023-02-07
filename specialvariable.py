from specialvariable2 import *
def func1():
    add()
    print("Function1",__name__)
def func2():
    print("Function3")
def func3():
    print("Function4")

def main():
    func1()
    func2()
    func3()

if __name__ == '__main__':
    main()