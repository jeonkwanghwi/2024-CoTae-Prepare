import queue
queue = queue.Queue()

queue.put(1) # push 1
queue.put(2) # push 2

print(queue.get()) # pop() -> FIFO구조이기 때문에 맨 앞의 원소가 삭제