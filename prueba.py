from queue import PriorityQueue
import copy
import math
q = PriorityQueue()

q.put((4, 'Read'))
q.put((2, 'Play'))
q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))


q2 = PriorityQueue()
q2.queue = copy.deepcopy(q.queue)
#for i in q1.queue: q2.put(i)

q2.put((8, 'Brian'))


while not q.empty():
    next_item = q.get()
    print(next_item[1])

print("---------------------------------------------")

while not q2.empty():
    next_item = q2.get()
    print(next_item[1])
