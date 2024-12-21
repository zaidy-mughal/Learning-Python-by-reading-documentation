#CheckPrime
for n in range(2,10):
    for x in range(2,n):
        if(n%x == 0):
            print(n, 'equals', x, '*', n//x)
            break
    #else statement will run if inner for loop does not terminated by break and complete all its iterations
    else:
        print(n, 'is a prime number')
