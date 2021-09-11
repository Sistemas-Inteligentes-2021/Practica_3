from os import read
from numpy import genfromtxt
from queue import PriorityQueue
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



# Where the magic start,
def A_star(initial_state, actions, goal_state,n):
    path=[initial_state.list]
    closed=[]
    state_counter=1 #count the initial state 
    q.put(0,initial_state)
    while not q.empty():
        state=q.get()
        f=state[0] #obtengo la prioridad
        state=state[1] #obtengo el nodo
        closed.append(state.list)
        if compare(goal_state,state.list):
            return state_counter,state,path
        for action in actions:
            sucessor=State()
            sucessor.list=TF(state,action,path,n)
            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                if list_in_lists(sucessor.list,closed):
                    continue
                sucessor.h=h1(sucessor.list,goal_state) #Aqui va nuestra funcion heuristica
                sucessor.g=state.g+1
                sucessor.f=sucessor.h+sucessor.g
                sucessor.setFather(state)
                state_in_open=state_in_queue(sucessor,q)
                if state_in_open!=None:
                    if sucessor.g >= state_in_open.g:
                        continue
                q.put(sucessor.f, sucessor)
                path.append(sucessor.list)
    return state_counter,None,path



# The last step show the steps
def show_path (path):
    for item in path:
        print("[ ",end="")
        for number in item:
            print(number,"  ",end="")
        print("]")

def read_from_csv ():
    data = genfromtxt('Data_Files/Data_15_Puzzle.csv', usecols= range(1, 17) , delimiter=",", dtype=int)
    initial_state_parsed = [x for x in data[0]]
    goal_state_parsed = [x for x in data[1]]
    return initial_state_parsed, goal_state_parsed

# State consist of a list of 16 numbers(0 to 15) tahth indicates the position of each box. Being the 0 the blank space
if __name__ == '__main__':
    n=input("Escriba el n del puzzle n x n")
    start_time = time.time()
    initial_state, goal_state = read_from_csv() # We define the goal and initial state
    actions=['L','U','R','D'] # We define the actions LURD (Left, Up, Right, Down) 
    first_node=State()  # Define Initial State
    first_node.setList(initial_state)
    first_node.setFather(None)
    first_node.g=0
    counter,objective,path=A_star(first_node,actions,goal_state,n)

    print("\nNumber of space states are:",counter)
    #show_path(path)
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


