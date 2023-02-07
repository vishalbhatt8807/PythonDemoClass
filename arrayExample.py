from array import *

# vals = array('i',[5,2,3,5,5,4])
#
# print(vals.extend([1,2,3,4,4]))
# print(vals.reverse())
# print(vals)
# newArr = array(vals.typecode)
# i =0
# while i < len(newArr):
#     print(i)
#     i +=1

from array import *

newArray = array('i',[])
vals = int(input("Enter the size of array"))

for i in range(vals):
   x = int(input("Enter the input"))
   newArray.append(x)
print(newArray)

s = int(input("Search the number: "))
k =0
for e in newArray:
    if e == s:
        print(k)
        break
    k +=1
else:
    print("Not found")

print(newArray.index(s))

