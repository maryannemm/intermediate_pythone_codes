import queue

q=queue.Queue() 
l=queue.LifoQueue()
r=queue.PriorityQueue()
numbers = [1,2,3,4,5,6,7,20]
for n in numbers:
    q.put(n)
    l.put(n)
print(q.get())
print(l.get())
#priority queues section i.e the lower the priority number the higher the priority syntax put( priority_number, assigned value)
r.put((0, 'user2'))
r.put((8, 'user7'))
r.put((6, 'user5'))
r.put((2, 'user10'))
print(r.get())
print(r.get())
print(r.get())
print(r.get())