#Sets
#  A set is an unordered collection with no duplicate elements. Its uses include membership testing and eliminating duplicate entries.
#  Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
#curly braces and set() function is used to create sets data type

#to create empty set we must use set() function
#if we use this {} it will create empty dictionary


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testing
print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(a - b)                              # letters in a but not in b (Difference)
print(a | b)                              # letters in a or b or both (Union)
print(a & b)                              # letters in both a and b (Intersection)
print(a ^ b)                              # letters in a or b but not both (Symmetric Difference)

#symmetric difference is also find by function symmetric_difference()
print(a.symmetric_difference(b))
