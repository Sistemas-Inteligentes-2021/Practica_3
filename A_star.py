from os import read
from numpy import genfromtxt
import numpy as np
from queue import PriorityQueue
from random import shuffle
from numpy.lib.scimath import sqrt
from tabulate import tabulate
import time
import copy

q = PriorityQueue()

class State:
    def __init__(self):
        self.list=[]
        self.g=0
        self.h=0;self.f=0
        self.father=None

    def setList(self, list):
        self.list=list

    def setFather(self, father):
        self.father=father
        

# Compare 2 Lists
def compare(list1,list2):
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
    return True

# Swap position in a list
def swap_positions(list, pos1, pos2):   
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# Search if a list is in a set of lists
def list_in_lists(single_lis, set_lists):
    for singleState in set_lists:
        if compare(singleState,single_lis):
            return True
    return False

def state_in_queue(node,my_queue):
    q = PriorityQueue()
    q.queue = copy.deepcopy(my_queue.queue)
    while not q.empty():
        actualNode=q.get()
        if compare(node.list,actualNode[1].list):
            return actualNode
    return None

def h1 (list,goal_list,n):
    sum=0
    for i in range(n):    
        if list[i] != goal_list[i]:
            print()
            sum=sum+1
    return sum

# Calculate Manhattan Distance
def h2(initial_state, n_parts):
    initial_config = initial_state
    manhattan_distance = 0
    for i,item in enumerate(initial_config):
        if item != 0:
            prev_row,prev_col = int(i/ n_parts) , i % n_parts
            goal_row,goal_col = int(item /n_parts),item % n_parts
            manhattan_distance += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manhattan_distance

def h3 (list):
    sum=0
    for i in range(len(list)):
        aux=i+1
        if list[i] != 0:
            while(aux<len(list)):
                if list[aux] != 0:
                    if list[i] > list[aux]:
                        sum=sum+1                
                aux=aux+1
    return sum

# Heuristic: Euclidean Distance 
def h4_euclidean_distance(initial_state, n_parts):
    initial_config = initial_state
    euclidean_distance = 0
    for i,item in enumerate(initial_config):
        if item != 0:
            prev_row,prev_col = int(i/ n_parts) , i % n_parts
            goal_row,goal_col = int(item /n_parts), item % n_parts
            x_euclidean, y_euclidean = abs(prev_row-goal_row), abs(prev_col - goal_col)
            z_euclidean = round(sqrt((pow(x_euclidean,2) + pow(y_euclidean,2))),2)    
            euclidean_distance += z_euclidean
    euclidean_distance = euclidean_distance * 100
    return int(euclidean_distance)


# Transition function expect a state and an action and will return the possible succesor state in base of the action
def TF(state, action,path,n):
    resulList=[]
    listNew=state.list.copy()
    if action == 'L':
        index=n-1
        for i in range(n):
            if listNew[index]==0:
                return None
            index=index+n
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)+1)                    
    elif action == 'U':
        index=(n*n)-1
        for i in range(n):
            if listNew[index]==0:
                return None
            index=index-1
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)+n)
    elif action == 'R':
        index=0
        for i in range(n):
            if listNew[index]==0:
                return None
            index=index+n
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)-1)
    elif action == 'D':
        index=n-1
        for i in range(n):
            if listNew[index]==0:
                return None
            index=index-1
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)-n)

    return None if list_in_lists(resulList,path) else resulList


def best_option(list_Nodes):
    f_values=[]
    shuffle(list_Nodes)
    for item in list_Nodes:
        f_values.append(item.f)
    index_f=f_values.index(min(f_values))
    return list_Nodes[index_f]


# Where the magic start,
def A_star(initial_state, actions, goal_state,n, n_parts):
    
    closed=[]
    state_counter=1 #count the initial state 
    q.put((0,initial_state))
    while not q.empty():
        it_Nodes=[]
        state=q.get()
        state=state[1] #obtengo el nodo
        closed.append(state.list)
        if compare(goal_state,state.list):
            return state_counter,state,closed
        for action in actions:
            sucessor=State()
            sucessor.list=TF(state,action,closed,n_parts)
            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                sucessor.h=h1(sucessor.list,goal_state,n) #Aqui va nuestra funcion heuristica
                #sucessor.h=h2(sucessor.list,n_parts) #Aqui va nuestra funcion heuristica
                #sucessor.h=h3(sucessor.list) #Aqui va nuestra funcion heuristica
                sucessor.g=state.g+1
                sucessor.f=sucessor.h+sucessor.g
                sucessor.setFather(state)
                state_in_open=state_in_queue(sucessor,q)
                if state_in_open!=None:
                    if sucessor.g >= state_in_open.g:
                        continue
                print(state_counter)
                it_Nodes.append(sucessor)
        sucessor=best_option(it_Nodes)
        q.put((sucessor.f,sucessor))
        closed.append(sucessor.list)                
    return state_counter,None,closed



# The last step show the steps
def show_path (path):
    for item in path:
        print("[ ",end="")
        for number in item:
            print(number,"  ",end="")
        print("]")
        
# Split list to display
def split_list(my_list, wanted_parts):
    length = len(my_list)
    return [ my_list[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

# Display Array in Grid
def display_array(array, n_parts):
    item = split_list(array, n_parts)
    table = tabulate(item, tablefmt="fancy_grid")
    print(table)
    print('\n')

# Display Path in Grids
def display_path(path, n_parts):
    for item in path:
        display_array(item,n_parts)

# Read from Data
def read_from_csv (size):
    file='Data/Data_'+str(size)+'Puzzle.csv'
    data = genfromtxt(file, usecols= range(1, size+2) , delimiter=",", dtype=int)
    initial_state_parsed = [x for x in data[0]]
    goal_state_parsed = [x for x in data[1]]
    return initial_state_parsed, goal_state_parsed

# State consist of a list of N numbers(0 to (N - 1)) that indicates the position of each box. 
# Being the 0 the blank space.
if __name__ == '__main__':
    n=int(input('Insert the size of Puzzle: '))
    n_parts=int(sqrt(n+1))
    start_time = time.time()
    initial_state, goal_state = read_from_csv(n) # We define the goal and initial state
    actions=['L','U','R','D'] # We define the actions LURD (Left, Up, Right, Down) 
    first_node=State()  # Define Initial State
    first_node.setList(initial_state)
    first_node.setFather(None)
    first_node.g=0
    first_node.h=0
    first_node.f=0

    counter,objective,path=A_star(first_node,actions,goal_state,n,n_parts)

    print("\nNumber of space states are:",counter)
    show_path(path)
    print("\n==============================\n")
    goal_path=[]
    state=State()
    if  objective != None:
        state=objective.father
        goal_path.append(objective.list)
        while(state.father != None):    
            goal_path.append(state.list);
            state=state.father
        goal_path.append(state.list);
        goal_path.reverse()
        show_path(goal_path)
        print("\nNumber of steps to find the goal state are:",len(goal_path)-1)
    print("--- Time: %s seconds ---" % (time.time() - start_time))


