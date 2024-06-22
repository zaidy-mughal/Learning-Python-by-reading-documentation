#Dictionaries and Looping Technique

# dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 
# Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.

# It is best to think of a dictionary as a set of key: value pairs

#to create an empty dictionary we use {}
dictionary = {}

dictionary = {'zaid':135,'saad':143, 'muneeb':125}
#this will print all the keys of Dictionary
print(list(dictionary))
#we can also sort keys
print(list(sorted(dictionary)))

# to search key in a dictionary we use in keyword
print('zaid' in dictionary)
print('haris' not in dictionary)

#dict() funtion directily builds the dictionaries from a sequence of key:value pairs
list1 = [('zaid',123),('haris',456),('zobia',789)]
dictionary_from_list = dict(list1)
print(dictionary_from_list)

#dict comprehensions can also be used to create dictionaries
list2 = {x:x**2 for x in range(5)}
print(list2)

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
list3 = dict(zaid=342,haris=532,layiba=2342)
print(list3)






#Looping Technique
#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
for k,v in list3.items():
    print(k,v)

# we can also iterate over the list using an enumerate() function

for i,v in enumerate(list2):
    print(i,v)

#to iterate over 2 sequences at one time we use zip function to link/pair each lists entities
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#to reverse a sequence we use reversed keyword in for loop
for i in reversed(range(1,10,2)):
    print(i)


#to loop in a sorted order
for i in sorted(list2,reverse=True):
    print(i)

# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


#Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.
#The operators is and is not compare whether two objects are really the same object. 

# The Boolean operators (not,and,or) and and or are so-called short-circuit operators: 
# When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


# Using walrus operator to assign and check the condition in a while loop
numbers = [1, 2, 3, 4, 5]
i = 0

while (num := numbers[i]) < 5:
    print(num)
    i += 1



#Sequence comparison

# Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. 
