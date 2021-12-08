# Stack & Queue
# Tumpukan & Antrian

print(25*"=" + " STACK " + 25*"=")
stack = [1,2,3,4,5]
print(f"Data now : {stack} \n")

# added new data
stack.append(6)
print(f"\nData IN : {6}")
print(f"Data now : {stack}")
stack.append(7)
print(f"\nData IN : {7}")
print(f"Data now : {stack}")

stacking = stack.pop() # stack is taking last data
print(f"\nStacking Data OUT: {stacking}")
print(f"Data now : {stack}")

print("\n" + 25*"=" + " QUEUE " + 25*"=")
from collections import deque #library

queue = deque([1,2,3,4,5])

print(f"Data now : {queue}")

# added new data
queue.append(6)
print(f"\nData IN : {6}")
print(f"Data now : {queue}")
queue.append(7)
print(f"\nData IN : {7}")
print(f"Data now : {queue}")

queueing = queue.popleft() # queue is taking first data
print(f"\nqueueing Data OUT: {queueing}")
print(f"Data now : {queue}")


