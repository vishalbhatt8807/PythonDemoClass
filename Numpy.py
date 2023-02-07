from numpy import *
#arrays
arr = array([1,2,3,5,5.6])
print(arr.dtype)
print(arr)
#linespace - by default it will divide in  50 chucks , last value will difined as chucks
arr  = linspace(1,50,2)
print(arr)
#logspace
arr  = logspace(1,50,5)
print(arr)

#zeros
arr  = zeros(5,int)
print(arr)

#ones
arr  = ones(5,int)
print(arr)

#arange
arr  = arange(1,10,2)
print(arr)

arr1 = array([1,2,3,4,5,6])
arr2 = array([7,8,9,7,4,8])

print(max(arr1))
print(max(arr2))
print(min(arr1))
print(sort(arr2))
print(sinc(arr2))
print(cos(arr2))
#arr3 = arr1 + arr2
print(sum(arr1))

#if has to copy array into another one
#first way
print(arr2)
arr3 = arr2
print(id(arr3))
print(id(arr2))
#second way

arr3 = arr2.view() # this is sallow view address would change but if use dont want its array value should not change than its not work
arr2[2] = 17
print(arr3)
print(arr2)
print(id(arr3))
print(id(arr2))
#Third way
arr3 = arr2.copy() # this is Deep view address would change but if use dont want its array value should change than its  work

# arr2[2] = 14
# print(arr3)
# print(arr2)
# print(id(arr3))
# print(id(arr2))
# arr4 = array([])
# for i in range(len(arr1)):
#     arr4 = arr1[i] + arr2[i]
#     print(arr4)

# Maximum number in array
arr2 = [100,123,12423,32334,2323232]
for i in range(len(arr2)):
    temp = arr2[0]
    if arr2[i] > temp:
        temp = arr2[i]
print(temp)

def maxValue(arr2): #Formal argument
    for i in range(len(arr2)):
        temp = arr2[0]
        if arr2[i] > temp:
            temp = arr2[i]
    print(temp)
maxValue([100, 123, 12423, 32334, 2323232]) # Actual argument

#Type of Arguments

type_of_Argu = ["position","Keyword","default","Variable Length","KeywordVariableArgument"]

type_of_Argu[0]
def postionExample(name, age):
    print("concept is passing argument in same position as it mentioned")
    print(name)
    print(age)


postionExample('vishal',20)

type_of_Argu[1]


def postionExample(name, age):
    print("concept is passing argument with keyword mentioned")
    print(name)
    print(age)


postionExample(age=20,name='vishal')

type_of_Argu[2]


def postionExample(name, age=30):
    print("concept is if user pass single argument still code will work because function already has default value")
    print(name)
    print(age)


postionExample('vishal')

type_of_Argu[3]


def postionExample(name,*age):
    print("concept is Passing argument has no number")
    print(name)
    for i in age:
        print(i)


postionExample('vishal', 20,30,40,50)

type_of_Argu[4]


def postionExample(name,**data):
    print("concept user has to pass the argument in keyword form than use ** as formal argument")
    print(name)
    for i,j in data.items():

        print(i,j)

    for i in data.keys():

        print(i)

    for j in data.values():

        print(j)


postionExample('vishal', age=20, city='Ratlam',country='India')


