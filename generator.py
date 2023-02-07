# Generator function is use when user don't want to use -- Yield keyword use instead of return. It return all value without end funtion and without using memory
class generator:
    def sqroot(self):
        n = 1

        while n <= 10:
            num = n * n
            yield num
            n +=1

g1 = generator().sqroot()

for i in g1:
    print(i)


