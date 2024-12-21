#Tuple and Sequences
#it is a type of sequence
#it consists of number of values seperated by commas
#it is not possible to assign values to tuple's elements (immutable) although the mutable objects(values) can be stored in tuples
#tuples usually contain hetrogeneous sequence of elements

#empty tuple
t = ()

# single valued tuple is created using a comma at the end of value
t = ('zaid',)

t = 1234,3453,'zaid'
print(t[0])

#tuples may be nested
p = 2345, t
print(p[1])

#tuple containing mutable objects
s = [23,43,45],[235,345,632]
print(s)

#we can also unpack the tuple or any other list same as multiple assignment
list, list1 = s
print(list)