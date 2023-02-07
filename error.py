#compile type, logical type and run time error

a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter the number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, you can't divide value by zero",e)
except ValueError as e:
    print("Invalid Input ",e)
except Exception as e:
    print("Something went wrong...")
finally:
    print("Resource Closed")
print("Bye")