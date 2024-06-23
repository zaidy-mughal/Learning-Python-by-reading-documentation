#Iterators in python

s = 'abc'
#iter returns an iterator object that defines the __next__() . this method gives single element at one time
it = iter(s)
it

print(next(it))
print(next(it))
print(next(it))
# it will raise StopIteration error/exception
# next(it)


#in class we can do iterate over class object by defining __iter__() and __next__() methods in that class
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    


rev = Reverse('spam')
print(iter(rev))

for char in rev:
    print(char)