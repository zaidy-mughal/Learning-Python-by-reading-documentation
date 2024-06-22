#Lists
books = ['dsa', 'pf', 'oop', 'report writing', 'calculus', 'software engineering']
books.append('statistics')

for book in books:
    print(book,end='.')
print()

#returns the number of times the given value appeared in the list
print(books.count('pf'))

#reverse the list
books.reverse()
print(books)

# attack the new list or iterable object
books.extend(['physics','islamic studies'])
print(books)

#inserts the new item in the list at given index
books.insert(2,'english')
print(books)

#removes the first item in the list equal to the given item
books.remove('report writing')
print(books)

#remove the item at given index and return it
print(books.pop(2))
#if we do not write index then it will pop and return last element
print(books.pop())

##clear all elements of the list
# books.clear()
# print(books)

#index returns the first index of the given value
print(books.index('statistics'))


#it sorts the list in the ascending or descending order with the given key of comparison
books.sort()
print(books)


#list comprehensions
#the concise way to create lists - if the elements of list are the result of some operation than we use list comprehensions

squares = []

for s in range(10):
    squares.append(s**2)

print(squares)

#we can also use this to save space of s in the previous technique...
squares = list(map(lambda s: s**2, range(10)))
#also this equals to 
squares = [x**2 for x in range(10)]
#this comprehension combines 2 list elements if these are not equal
combine = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#we can apply a function to all the elements
positive = [abs(x) for x in squares]

#we can create a list of 2-tuples like (number, square)
# the tuple must be parenthesized otherwise it generate error
tuplelist = [(x, x**2) for x in range(6)]

#we can flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
flatedlist = [num for elem in vec for num in elem]


#NESTED LIST COMPREHENSIONS
matrix = [
    [1,2,3],
    [3,4,5],
    [6,7,8]
]

transposed = [[row[i] for row in matrix] for i in range(3)]

print(transposed)

transposed2 = []
for i in range(3):
    transposed2_row = []
    for row in matrix:
        transposed2_row.append(row[i])
    transposed2.append(transposed2_row)

print(transposed2)

#there is also a build-in function that do the transpose that is zip-zip return object so to get list we use list before zip
print(list(zip(*matrix)))


#DEL STATEMENT
#it is different from pop and it is used to remove element at the given index or slices of elements from list
del transposed2[0]
print(transposed2)
#it is also used to delete whole variable
del transposed2
print(transposed2)

