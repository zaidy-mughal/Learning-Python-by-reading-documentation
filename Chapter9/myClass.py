class myClass:
    """Doc String of My Class used for writing class description"""
    def __init__(self,real,imaginary):
        self.r = real
        self.i = imaginary

    def f(self):
        print('Hello World!')

    
x = myClass(3,-3.5)
print(x.r)
print(x.i)
xf = x.f
x = 1
while x in range(3):
    xf()
    x+=1






#if we define a class variable in wrong place it is shared by all instances of the class. Like here in kind variable...
class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs
print(e.kind)                  # shared by all dogs
print(d.name)                  # unique to d
print(e.name)                  # unique to e




#also it is very cheap in the case for mutable variables
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs



#we can correct this by defining the variable in the __init__method
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(e.tricks)
print(d.tricks)






# Methods may call other methods by using method attributes of the self argument
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)