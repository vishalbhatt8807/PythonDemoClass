# 0,1,1,2
# a,b,c
#   a,b,c

def feb(n):
    a =0
    b =1
    if n < 0:
        print("Invalid value")
    elif n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print(a)
        print(b)
        c =0
        for i in range(2,n):
            c = a + b
            if c < 100:

                a = b
                b = c
                print(c)
            else:
                 print("Value is greater than 100 hence break loop")
                 break

feb(20)


def fact(x):

    f = 1
    for i in range(1,x+1):
        f = f * i

    return f




x = 5
f = fact(x)
print ("Factorial Value is : {}".format(f))


# Recursion -> function call itself
#bydefault limit is 1000 is set how to t check - check below code

# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# i =0
#
# def greet():
#     global i
#     i +=1
#     print ("Hello",i)
#    # greet()
#
# greet()

#Factorial function using recusion method

def fact(n):
    if n==0:
        return 1

    return n * fact(n-1)

result = fact(5)

print("Factorial using recusive method and value is : {} ".format(result))