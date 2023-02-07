#suppose you want to perform some action using existing function but you cant be edit it but in python you can using decorator
#in python we can call function into function also we can create method into method
#example predefined function
def div(a,b):
    print(a/b)

#but now user want either if i pass argument 2,4 as well than value should come same but as programmer we cant change in existing
#function hence will create a new function

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner
#assign new function to existing one.
#div inside argument is a function we are passing
div = smart_div(div)
div(2,4)
