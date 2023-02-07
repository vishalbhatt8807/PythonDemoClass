#global and globals

a = 10

def func():
    a = 15
    print('in side ', a)

func()

print("Outside" ,a)

#Now we have to define local variable as global so value can change whatever we pass inside method to outside function as well


a = 10

def func():
    global a
    a = 15
    print('in side ', a)

func()

print("Outside" ,a)

# but the problem is if use want to create same variable (name) in same function than it wont allow and that case will using globals func

a = 10


def func():
    #global a
    a = 15
   # globals()[a]
    print('in side ', a)
    print('before in side ', a)
    globals()[a] =20
    print('before in side ', a)
func()

print("Outside", a)

lst =[12,23,12,435,2,12,45,54,36,878,78, 79]

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2==0:
            even +=1
        else:
            odd +=1

    return even,odd

even,odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))

list = ['vish', 'bhat' ,'chit' ,'paya','umh','appu', 'tapan' ,'saep', 'rah' , 'tina']

def countletters(list):
    count = 0
    countlessthan5 =0
    for i in list:
        if len(i) >5 :
            count +=1
        else:
            countlessthan5 +=1

    return count,countlessthan5

count,countlessthan5 = countletters(list)

print("Letter more than 5 chars : {} , Letter less than 5 chars : {}".format(count,countlessthan5))
