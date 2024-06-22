
# #FunctionDefinition
# def fib(n):
#     """Print the fibounacci series upto n"""
#     a,b = 0,1
#     while a < n:
#         print(a,end=' ')
#         a,b = b,a+b
#     print()

# fib(100)

# #in Python we can point another name to the same function object
# f = fib
# f(100)


#returning funtion
def fib2(n):
    """returns the list of fibounacci series"""
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b= b,a+b
    return result

f100 = fib2(100)
print(f100)

#default values
#default values evaluated only once. it effects mutable objects(lists,tuples,instances of most classes)
def f(n,l=[]):
    l.append(n)
    return l

#If you don’t want the default to be shared between subsequent calls
def f1(n,l=None):
    if l is None:
        l = []
    l.append(n)
    return l

#calling a function by keyword arguments
f1(5)       #positional argument
f1(n=5)     #keyword argument

#These are the error while calling functions
# f1()                     # required argument missing
# f(n=5.0, [1,2,3])        # non-keyword argument after a keyword argument
# f(110, n=220)            # duplicate value for the same argument
# f(voltage = 23)          # unknown keyword argument


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    for arg in arguments:
        print(arg)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# the names of positional-only parameters can be used in **kwds without ambiguity.

def foo(name, /, **kwds):
    return 'name' in kwds

print(foo(1,**{'name':2}))

# For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

#this is the call when we have arguments of range singly...
print(list(range(3,6)))

#if we have the arguments in list or tuple form then we do this
#unpacking argument list
args = [3,6]
print(list(range(*args)))

#we can also unpack dictionaries using **args
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedi' demised", "action": "VOOM"}
parrot(**d)

#LAMBDA
#lambda as returning funtion and funtion nesting
def increament(n):
    return lambda x: x+n

#this will assign the lambda function to f
f = increament(20)
#this will give value to lambda function and will print 25.
print(f(5))

#lambda as passing funtion... 
#this sort method sort the value in ascending order
#pairs contain a list of tuples which have one integer and one string value
#lambda function returns the second value of each pair in the pairs list
#sort function will sort the list of tuples on the basis of strings
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)