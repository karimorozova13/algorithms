from queue import Queue

# First In First Out, Черги 
q = Queue()

# add el
q.put('a')
q.put('b')
q.put('c')
print(q.queue)

# delete el
q.get()
print(q.queue)

q1 = Queue(maxsize=3)

print(q1.empty())

q1.put('a')
q1.put('b')
q1.put('c')

# correct just for limited queue
print(q1.full())
print(q1.qsize())
print(q1.get())
print(q1.get())

