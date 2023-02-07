#anonymous or lambda function

def squre(n):
    return n * n

result = squre(5)
print(result)

#To simplify above method into lambda function
#square function
f = lambda n: n*n

result = f(5)
print(result)

#Addition function

f = lambda a,b: a+b

result= f(4,5)
print(result)

#Filter , map and reduce function using lambda operation
#filter will filter out value like even and odd
#map will perform any operation like double the value of evens
#reduce will be perform a single value like add all doubles value import functools

from functools import reduce
lst = [4,3,5,6,7,8,8,9,12,35,56,2]

even = list(filter(lambda i:i%2==0,lst))
print(even)
doubles = list(map(lambda i:i*2,even))
print(doubles)
reduce =  reduce(lambda a,b:a+b,doubles)
print(reduce)