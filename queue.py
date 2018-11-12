from collections import deque
queue = deque(['Eric','John','Michel'])
queue.append('Graham')
queue.popleft()
queue.popleft()
print(queue)