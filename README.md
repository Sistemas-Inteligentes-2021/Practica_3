# Practice 3
## Members

- Daniel Camacho
- Adrian Mendoza
- Juslan Vargas

## 1. Describing the Problem
- The main problem that we want to solve is the N_Puzzle, finde the best and optimally solution given and initial state and defined a Goal State

## 2. Describing the Solution

To solve the problem in this laboratory we are using A star algorithm, we will prove that A star algorithm (that is a Informed search) is better than the not informed algorithms, also we are going to use differents heuristics functions to try to get the solution in the shortest time and we are going to compare this heuristic functions and how affect the optimeless in algorithm. The first heuristic function is the number of boxes missplaced of the objetive, the second heuristics function is the summatory of manhattan distance between all boxes and finally the third heuristic is the sumatory of inverse permutations

## 3. Experiments & Results

We use the file "A_star_list_version.py" for running the experiments and saving the results, you can see an example of how we annote the data in "Print_view.png" in Assets/Images/Prints folder, the algorithm works with n puzzle the only thing that we need to run the program is create the csv with the name "Data_NPuzzle.csv" with the initial and goal state, finally the results that we get are:
### 8 Puzzle (N = 8)

With Heuristic function 1:

Initial State | Time (seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 0.004999876022338867  |  19  |  6  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 0.006999969482421875 |  25  |  7  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 0.011001110076904297 |  40  |  8  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 0.017000675201416016 |  56  |  9  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 0.0260159969329834 |  73  |  10  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 0.8903868198394775 |  478  |  14  |  14
[4, 6, 1, 5, 0, 8, 7, 2, 3] | 352.85682916641235 |  9177  |  20  |  20


With Heuristic function 2:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 0.0050008296966552734 |  13  |  6  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 0.005003452301025391 |  15  |  7  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 0.006999015808105469 |  21  |  8  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 0.009000062942504883 |  30  |  9  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 0.009001016616821289 |  32  |  10  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 0.01399993896484375 |  44  |  14  |  14
[4, 6, 1, 5, 0, 8, 7, 2, 3] | 1.4729995727539062 |  560  |  20  |  20


With Heuristic function 3:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 0.004999637603759766 |  13  |  6  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 0.007002592086791992 |  24  |  7  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 0.0069997310638427734 |  26  |  8  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 0.007000923156738281 |  22  |  9  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 0.00799870491027832 |  27  |  10  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 0.04492330551147461 |  101  |  14  |  14
[4, 6, 1, 5, 0, 8, 7, 2, 3] | 1.9899470806121826 |  712  |  20  |  20


*OPTIONAL

With Heuristic function 4:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 0.008001565933227539 |  19  |  6  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 0.008000373840332031 |  22  |  7  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 0.01199960708618164 | 29  |  8  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 0.010999917984008789 |  30  |  9  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 0.012001991271972656 |  32  |  10  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 0.020999670028686523 |  48  |  14  |  14
[4, 6, 1, 5, 0, 8, 7, 2, 3] | 3.747187376022339 |  886  |  20  |  20



### 15 Puzzle (N = 15)

With Heuristic function 1:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | 0.005007028579711914 | 17 | 6 |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | 0.0059986114501953125 | 20 | 7 |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | 0.007999658584594727 | 28 | 8 |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.0070002079010009766 | 24 | 9 |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.010000944137573242 | 36 | 10 |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | 0.02500009536743164 | 67 | 14 |  14


With Heuristic function 2:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | 0.004999637603759766 | 17 | 6 |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | 0.005998849868774414 | 20  | 7 |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | 0.006999969482421875 | 22 |  8 |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.007999420166015625 | 24 | 9 |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.008999109268188477 | 30 | 10 |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | 0.013000726699829102 | 38 | 14 |  14
[1, 10, 0, 2, 6, 8, 5, 11, 14, 13, 3, 7, 4, 12, 9, 15] | 44.222795724868774 | 2832 | 30 |  30
[1, 0, 10, 2, 6, 8, 5, 11, 14, 13, 3, 7, 4, 12, 9, 15] | 213.93165183067322 | 6120 | 31 |  31


With Heuristic function 3:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | 0.004999637603759766 | 17 | 6 |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | 0.007999658584594727 | 26 | 7 |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | 0.009000539779663086 | 28  | 8 |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.009999752044677734 | 32 | 9 |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.014998435974121094 | 43 | 10 |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | 0.03399968147277832 | 77 |  14 |  14


*OPTIONAL

With Heuristic function 4:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | 0.007999897003173828 | 17 | 6 |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | 0.008999824523925781 | 20 | 7 |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | 0.012999773025512695 | 28 | 8 |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.014999151229858398 | 31 |  9 |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 0.024000167846679688 | 47 | 10 |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | 0.01923823356628418 | 38 | 14 |  14
[1, 10, 0, 2, 6, 8, 5, 11, 14, 13, 3, 7, 4, 12, 9, 15] | 732.7299716472626 | 11219 | 30 |  30

## 4. Conclusions
---
TIME COMPARISON   N = 8

Initial State | Ideal Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 6 | 0.004999876022338867  | 0.0050008296966552734  |  0.004999637603759766 
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 7 | 0.006999969482421875  | 0.005003452301025391  |  0.007002592086791992 
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 8 | 0.011001110076904297  | 0.006999015808105469  |  0.0069997310638427734 
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 9 | 0.017000675201416016  | 0.009000062942504883  |  0.007000923156738281 
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 10 | 0.0260159969329834  | 0.009001016616821289  |  0.00799870491027832 
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 14 | 0.8903868198394775  | 0.01399993896484375  |  0.04492330551147461 
[4, 6, 1, 5, 0, 8, 7, 2, 3] | 20 | 352.85682916641235  | 1.4729995727539062  |  1.9899470806121826 

SPACE COMPARISON N = 8

Initial State | Ideal Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 6 |  19 | 13  | 13  
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 7 | 25  | 15 |  24
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 8 | 40  | 21 |  26
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 9 | 56  | 30 |  22
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 10 | 73  | 32 | 27
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 14 | 478 | 44 |  101
[4, 6, 1, 5, 0, 8, 7, 2, 3] | 20 | 9177  | 560 | 712

---

TIME COMPARISON   N = 15

Initial State | Ideal Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | 6 | 0.005007028579711914  |  0.004999637603759766   |  0.004999637603759766  
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | 7 | 0.0059986114501953125  |  0.005998849868774414   |  0.007999658584594727 
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | 8 | 0.007999658584594727  |  0.006999969482421875   |  0.009000539779663086  
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 9 | 0.0070002079010009766  |  0.007999420166015625   |  0.009999752044677734 
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 10 | 0.010000944137573242  |  0.008999109268188477   |  0.014998435974121094  
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | 14 | 0.02500009536743164  |  0.013000726699829102   |  0.03399968147277832 

SPACE COMPARISON   N = 15

Initial State | Ideal Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | 6 | 17  |  17   |  17
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | 7 | 20  |  20   |  26 
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | 8 | 28  |  22   |  28  
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 9 | 24  |  24   |  32 
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | 10 | 36  |  30   |  43  
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | 14 |  67 |  31   |  77 


In the end we could observe that according to the heuristic function we used, the number of states that expanded varied considerally. This is because the node that we choose to expand depends completelly in the heuristics function (h+g), also we prove that A star is a efficient algorith that is faster and more efective than BFS, ID or other not informed search. We can conclude that A star is an completeness and optimally algorithm because it finds a solution and it find the optimally solution because minimize the cost beetwen the initial state and goal state, unfortunetly no all is great  A star algorithm still having a  big problem the memory that uses looking for the best solution still being a big number. Finally we found that the best heuristic is the heuristic of Manhatan distance, next the inverse heuristic and finally the box in missplace heuristic. The heroustic that uses more space is h1 then h3 and finally h2 and the heuristic that solve the problem in shortest time is h2 then h3 then h1. All this because with Manhattan distance

We use 'Live Share' extension of VSCode to develop the code.

### Porotos h4 Heuristic : Euclidean Distance

To develop this heuristic function we get inspired in the las class where the Mg. Gerard explained

What we do was find the euclidean distance beetwen the node visited and the goal state, we get the initial position of the element in the current node and the same position of the same element in goal state, then we substract them and get the absolute value of the substract and finally with Pitagoras equation we get the eucliden distance

We afirm that this heuristic is admisible beacause:  
1. Our nodes do not have an infinite number of successors
2. The cost of going from one state to another is 1, in no case do we have a cost of 0
3. Our estimation of the cost (ĥ) is less or equal than the real cost (h)

With this we guaranteed than A*, with our heuristic function, is optimality and complete

### Comments

When we are developing the algorithm we get noticed that the priority queue librarie that python documentation give has not the problem that we experimented, we used both libraries thinking that the problem may be just one, but we have the same issue (the issue can see it in assets Images/Error "Error heap.png" and "Error Priority queue.png"), we really try to find a way to solve the problem looking at forums like in stack overflow, github or looking for examples with that library but we didnt solve anything at the end we just simply decided to use a list and make a function to pick the best heuristic and we did that, the algorithm that we used for a star was the algorithm that we saw in classes and we comprobe it looking for another algorithm and we found the same.

We use 'Live Share' extension of VSCode to develop the code.

### Porotos h4 Heuristic : Euclidean Distance

Para desarrollar esta heuristica nos inspiramos en una clase donde vimos este metodo.

Lo que hicimos fue obtener la posicion inicial del elemento y la posicion del mismo elemento en el goal state, luego restamos ambas coordenadas obteniendo el valor absoluto, finalmente con la ecuacion de pitagoras obteniamos the euclidean distance. 
## 5. Bibliography

➡️  Manual Tests, 8 Puzzle & 15 Puzzle : [Miro][miro]

➡️  Copy a Queue: [Stackoverflow][copy_queue]

➡️  Priority Queue: [Python Docs][priority_queue]

➡️  Priority Queue: [Python Docs][heapq]

➡️  A* Algorithm: [Medium][a_star_algorithm]


[miro]: https://miro.com/welcomeonboard/YWcxVk5zcnNsRTVPOFlsaVZlTnhCdzU1MjNzU3VMbnJHOFdadndBOVV6TVBwY29GOXNZbjg5QndkNTc3OTZnc3wzMDc0NDU3MzQ5MzA5MzU1OTMx

[copy_queue]: https://stackoverflow.com/questions/32488533/how-to-clone-a-queue-in-python

[priority_queue]: https://docs.python.org/3/library/asyncio-queue.html

[heapq]: https://docs.python.org/3/library/heapq.html

[a_star_algorithm]: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
