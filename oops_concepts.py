class Computer:
    #__Init is a consutrator,
    def __init__(self):
        self.name = "Vishal"
        self.age = 24

    def update(self):
        self.name = "Ashish"
        self.age = 24

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)
