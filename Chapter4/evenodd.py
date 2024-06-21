#print the even and odd numbers from 2 to 10(excluded)
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        #continue statement skips one iteration
        continue
    print("Found an odd number", num)