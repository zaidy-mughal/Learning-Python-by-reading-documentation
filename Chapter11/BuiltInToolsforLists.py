#this provides array to store homogeneous elements with H (2 bytes) memory allocation at each entry
#normal list uses 16 bytes per entry
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# in Collections module there is a deque module which is used to implement queue and bfs of trees
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)


# the library also offers other tools such as the bisect module with functions for manipulating sorted lists:
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)


#this module is used to use heap functions
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries



# Decimal Floating Point Arithmetic
# The decimal module offers a Decimal datatype for decimal floating point arithmetic. Compared to the built-in float implementation of binary floating point it is very beneficial over normal binary floating point
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))

print(round(.70 * 1.05, 2))



# Exact representation enables the Decimal class to perform modulo calculations and equality tests that are unsuitable for binary floating point:

Decimal('1.00') % Decimal('.10')
print(1.00 % 0.10)
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)

# The decimal module provides arithmetic with as much precision as needed:
getcontext().prec = 36
print(Decimal(1) / Decimal(7))