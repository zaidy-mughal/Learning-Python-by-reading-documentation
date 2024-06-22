#Chapter 7 
#Fancier Outputs in Python

year = 2016
event = 'Referendum'
#we use f before the string's starting apostrofi or inverted comma -to write variable's value in the string.
print(f'Results of the {year} {event}')

#str.format() funtions format the string but need some more info
#like 
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
#{:-9} do left align the variable value
#{:2.2%} do 2 digits before (.) and 2 digits after point is shown in output


name = 'zaid'
# str funtion write the name value without '' , / , \ , etc
print(str(name))
# repr function write the name value including '' , / , \ , etc
# The argument to repr() may be any Python object
print(repr(name))

# rounds pi to three places after the decimal
import math
print(f'The value of pi is approximately {math.pi:.3f}.')


# Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
print(f'My hovercraft is full of {name!r}.')


# A number in the brackets can be used to refer to the position of the object passed into the str.format() method.
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

#positional and keyword arguments can be arbirarily used in format funtion
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='george'))

#we can also format by passing dict and using [] to access the keys
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

#this can also done by refering to dict by **
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#it is also useful in making columns
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))