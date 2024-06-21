
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
