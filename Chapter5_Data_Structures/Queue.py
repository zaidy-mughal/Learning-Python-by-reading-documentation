#Queue
# as adding and removing from left is very fast in collections.deque so we use its functions to perform FiFo
from collections import deque

Queue = deque([2,3,4,5,6])

print(Queue)

Queue.append(7)

print(Queue.popleft())