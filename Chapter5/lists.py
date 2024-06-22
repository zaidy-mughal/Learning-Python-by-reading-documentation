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