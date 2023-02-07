values = [10,20,230]

it = iter(values)
print(it.__next__())

print(next(it))

for i in values:
    print(i)

class TopTen:
    def __init__(self):
        self.count = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count <= 10:
            val = self.count
            self.count +=1
            return val
        else:
            raise StopIteration

t1 = TopTen()

print(next(t1)) # if one time next it call here than in below loop value will be start from next value like 2.
for i in t1:
     print(i)