from queue import PriorityQueue
import copy
import math
import heapq


q=[(3,{1:6, 2:"daf"}), (5, {1:6, 2:"daf"}), (5,{1:6, 2:"daf"})]
# heapq.heappush(q,(4, 'Read'))
# heapq.heappush(q,(5, 'Play'))
# heapq.heappush(q,(5, 'Play2'))
# heapq.heappush(q,(2, 'Write'))
# heapq.heappush(q,(1, 'Code'))
# heapq.heappush(q,(7, 'Study'))
# heapq.heappush(q,(5, 'Ad'))
# heapq.heappush(q,(8, 'Go'))
# heapq.heappush(q,(6, 'Test'))



while  q:
    aux=heapq.heappop(q)
    print(aux[0], aux[1])

print(q)

# q = PriorityQueue()

# q.put((4, 'Read'))
# q.put((5, 'Play'))
# q.put((5, 'Write'))
# q.put((1, 'Code'))
# q.put((3, 'Study'))



# while not q.empty():
#     next_item = q.get()
#     print(next_item)


# print(q.get()[0])



# q2 = PriorityQueue()
# q2.queue = copy.deepcopy(q.queue)
# #for i in q1.queue: q2.put(i)

# q2.put((8, 'Brian'))


# print("---------------------------------------------")

# while not q2.empty():
#     next_item = q2.get()
#     print(next_item[1])

# #----- MANHATTAN H2 -----------
# initial_state = [1,5,3,4,2,6,7,8,0]
# goal_state = [0,1,2,3,4,5,6,7,8]

# # Calculate Manhattan Distance
# def h2(initial_state, n_parts):
#     initial_config = initial_state
#     manhattan_distance = 0
#     for i,item in enumerate(initial_config):
#         if item != 0:
#             print('BREAK')
#             print(i)
#             print('Item:',item)
#             prev_row,prev_col = int(i/ n_parts) , i % n_parts
#             goal_row,goal_col = int(item /n_parts),item % n_parts
#             manhattan_distance += abs(prev_row-goal_row) + abs(prev_col - goal_col)
#             print('SUM')
#             print(manhattan_distance)
#             print('------------')
#     return manhattan_distance

# h_manhattan = h2(initial_state, 3)
# print(h_manhattan)


# def h1 (list,goal_list,n):
#     sum=0
#     for i in range(n):
#         print(i)
#         if list[i] != goal_list[i]:
#             sum=sum+1

#     return sum

# initial_state = [0,1,5,3,4,2,6,7,8]
# goal_state = [0,1,2,3,4,5,6,7,8]

# print(h1(initial_state,goal_state,9))

