# Generators are a simple and powerful tool for creating iterators. 

# It use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


#Anything that can be done with generators can also be done with class-based iterators.
# the __iter__() and __next__() methods are created automatically.



# In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration. 

#GENERATOR EXPRESSIONS
# Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

# these expressions are very similer to list comprehensions in syntax but used () instead of []

sum(i*i for i in range(10))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product


# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))