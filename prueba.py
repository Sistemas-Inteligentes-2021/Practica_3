from queue import PriorityQueue
import math
q = PriorityQueue()

q.put((4, 'Read'))
q.put((2, 'Play'))
q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))

while not q.empty():
    next_item = q.get()
    print(next_item[1])


a=[1,2,3,4,5,6,7,8,9]


for i in a:
    print(i)
    if i % 2 ==0 :
        print("1 if")
        if i % 3 ==0 :
            run_code