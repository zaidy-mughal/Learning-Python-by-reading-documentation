# (#)Used for comment
# (=) used for assignment
a = 16
b = 3
c = a+b
# used to print anything
print(c)

#this // operator gives Floored Output
c = a//b
print(c)

#gives the remainder value of calculation
c = a%b
print(c)

# gives the a to the power of b
c = a**b
print(c)

# operators within the mixed operands convert the integer to floating point
c = a*3.75-1
print(c)

# in the interactive mode (_)variable automatically stores the last calculation

# round(var, upto) round off the variable to the given (upto) value
print(round(3.748564,2))

#Python has built-in data types to support complex numbers it is written in (j) OR (J)
# if we have numbers we can do d=3+4j but in variables case below method is used
d = a + b *1j
print(d)
print(type(d))



#STRINGS
#can be written in single or double quotes
name = 'zaid'
name = "zaidy"
print(name)

# (\) is used to skip special characters or quotes
# it will print zaidy's computer
name = 'zaidy\'s computer'
print(name)

# if outer sign is used inside the string then skip that otherwise there is no need
name = "zaidy's computer"
print(name)

# (\n) represents a new line character.
name = 'zaid amjad\ncomputer science'
print(name)

#if we want to skip the effect of backslash(\) then simply write (r) before the first quote
name = r'zaid amjad\ncomputer science'
print(name)

#we can write multiline String using tripe double/single quotes ("""...""") or ('''...''')
#we can also skip the first line if we write \.
name = '''\
Zaid 
Amjad
Mughal
'''
print(name)

#Concatination in a String is done by + operator and Strings are repeated using * operator
name = 'zaid'
fname = ' amjad'
#it means 3 times name + 1 time fname
print(3*name+fname)

#there is another way of doing concatination that word with only literals not variable or expressions
#this method is useful in breaking strings to write more lines
name = 'za' 'id' ' amjad'
print(name)

#in python there is not a specific character type the string of length 0 is character.
#String can be indexed and sliced
print(name[0])

#prints the last character of the string
print(name[-1])

#Slicing is used to get the subString from the String
#in slicing first always included and last always excluded in this 0th index included and 2nd index excluded
print(name[0:2])

#useful Defaults of Slicing [:2] get the substring from start to 2nd pos and [2:] gives substring from 2nd to end of String
#that is why name[:2]+name[2:] is always equals to (name)
print(name[:2])
print(name[2:])

#when writing out of bound index this will generate error
#print(name[35])
#but if we used out-of-bound index in slicing it will handle very efficiently
print(name[42:])
print(name[5:35])

#we cannot assign values using String index or slicing (IMMUTABLE)

#len(name) gives the total length of string
print(len(name))
print([1,2,3,4,5,6])


