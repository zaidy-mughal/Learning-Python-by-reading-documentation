#Chapter 4

#if...elif...else  else and elif are optional
#if we write this sequence (if...elif...elif...elif) than it is substitute for swith case
x = int(input("write an integer: "))
if x<0:
    x=0
    print('Negative converted into zero.')
elif x==0:
    print("zero")
elif x==1:
    print('one')
else:
    print('more')


#for statements are differ in python. it iterates over the items of any sequence(list or string)
words = ['zaid','haris','raoqasim']
for w in words:
    print(w,len(w))



#in this example users is a class type so i cannot run

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

#enumerate is used to iterate over a sequence
season = ['spring','fall','winter','automn']
print(list(enumerate(season)))

arr = [1,2,3,4,5,6]
for i in range(len(arr)):
    print(arr[i])


#return the iterable object
print(range(10))

#sum function takes iterable objects
#range with three parameters used to interate from, to, step(increament)
print(sum(range(0,10,3)))

