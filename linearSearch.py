POS = -1

def search(list, n):
    i =0
    for data in range(i,len(list)):
        if list[data] == n:
            globals() ['POS'] = data
            return True
    return False

list = [4,5,6,8,3,10,9,12]
n =12

if search(list, n):
    print("Found at position",POS+1)
else:
    print("Not Found")