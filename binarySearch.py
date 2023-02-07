

POS = -1
def binarySearch(n,list):
    l = 0
    u = len(list)

    while l <= u:
        k = (l+u)//2
        if list[k] == n:
            globals()['POS'] = k
            return True
        else:
            if list[k] < n:
                l = k
            else:
                u = k

list = [23, 34, 50, 45, 80, 90, 100,102,103,234,3,4,5,6,7,8,9,10,121,134,143]
list.sort()
print(list)
n = 90

if binarySearch(n,list):
    print("Found at ",POS+1)
else:
    print("Not Found")