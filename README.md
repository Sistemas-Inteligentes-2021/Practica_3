# Practice 3
## 1. Describing the Problem
- The main problem that we want to solve is the N_Puzzle, finde the best and optimally solution given and initial state and defined a Goal State

## 2. Describing the Solution

To do

## 3. Experiments & Results
### 8 Puzzle (N = 8)

With Heuristic function 1:

Steps | Time | Initial State
:---: | :---: | :---: 
6 | 0.0149993896484375 seconds | [1, 4, 2, 3, 5, 8, 0, 6, 7]
7 | 0.01600050926208496 seconds | [1, 4, 2, 0, 5, 8, 3, 6, 7]

8 | - | [1, 4, 2, 5, 0, 8, 3, 6, 7]
9 | - | [1, 0, 2, 5, 4, 8, 3, 6, 7]
10 | - | [1, 2, 0, 5, 4, 8, 3, 6, 7]
14 | - | [1, 2, 8, 5, 4, 7, 0, 3, 6]


With Heuristic function 2:

Steps | Time | Initial State
:---: | :---: | :---: 
6 | 0.008000373840332031 seconds | [1, 4, 2, 3, 5, 8, 0, 6, 7]
7 | 0.008000850677490234 seconds | [1, 4, 2, 0, 5, 8, 3, 6, 7]
8 | 0.009000062942504883 seconds | [1, 4, 2, 5, 0, 8, 3, 6, 7]

9 | - | [1, 0, 2, 5, 4, 8, 3, 6, 7]
10 | - | [1, 2, 0, 5, 4, 8, 3, 6, 7]
14 | - | [1, 2, 8, 5, 4, 7, 0, 3, 6]


With Heuristic function 3:

Steps | Time | Initial State
:---: | :---: | :---: 
6 | 0.0059967041015625 seconds | [1, 4, 2, 3, 5, 8, 0, 6, 7]

7 | - | [1, 4, 2, 0, 5, 8, 3, 6, 7]
8 | - | [1, 4, 2, 5, 0, 8, 3, 6, 7]
9 | - | [1, 0, 2, 5, 4, 8, 3, 6, 7]
10 | - | [1, 2, 0, 5, 4, 8, 3, 6, 7]
14 | - | [1, 2, 8, 5, 4, 7, 0, 3, 6]


### 15 Puzzle (N = 15)

With Heuristic function 1:

Steps | Time | Initial State
:---: | :---: | :---: 
6 | - | [1,5,2,3,4,6,10,7,8,9,14,11,12,0,13,15]
7 | - | [1,5,2,3,4,6,10,7,8,0,14,11,12,9,13,15]
8 | - | [1,5,2,3,4,6,10,7,0,8,14,11,12,9,13,15]
9 | - | [1,5,2,3,0,6,10,7,4,8,14,11,12,9,13,15]
10 | - | [1,5,2,3,6,0,10,7,4,8,14,11,12,9,13,15]
14 | - | [1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]


With Heuristic function 2:

Steps | Time | Initial State
:---: | :---: | :---: 
6 | - | [1,5,2,3,4,6,10,7,8,9,14,11,12,0,13,15]
7 | - | [1,5,2,3,4,6,10,7,8,0,14,11,12,9,13,15]
8 | - | [1,5,2,3,4,6,10,7,0,8,14,11,12,9,13,15]
9 | - | [1,5,2,3,0,6,10,7,4,8,14,11,12,9,13,15]
10 | - | [1,5,2,3,6,0,10,7,4,8,14,11,12,9,13,15]
14 | - | [1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]


With Heuristic function 3:

Steps | Time | Initial State
:---: | :---: | :---: 
6 | - | [1,5,2,3,4,6,10,7,8,9,14,11,12,0,13,15]
7 | - | [1,5,2,3,4,6,10,7,8,0,14,11,12,9,13,15]
8 | - | [1,5,2,3,4,6,10,7,0,8,14,11,12,9,13,15]
9 | - | [1,5,2,3,0,6,10,7,4,8,14,11,12,9,13,15]
10 | - | [1,5,2,3,6,0,10,7,4,8,14,11,12,9,13,15]
14 | - | [1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]

## 4. Conclusions
---
TIME COMPARISSON   N = 8

Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---:
6 | - |  - |  -
7 | - |  - |  -
8 | - |  - |  -
9 | - |  - |  -
10 | - |  - |  -
14 | - |  - |  -


---

TIME COMPARISSON   N = 15


Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---:
6 | - |  - |  -
7 | - |  - |  -
8 | - |  - |  -
9 | - |  - |  -
10 | - |  - |  -
14 | - |  - |  -

In the end we could observe that according to the heuristic function we used, the number of states that expanded varied. This was due to the shuffle function that we have when there is a tie in priority. 

We use 'Live Share' extension of VSCode to develop the code.
## 5. Bibliography

➡️  Manual Tests, 8 Puzzle & 15 Puzzle : [Miro][miro]

➡️  Copy a Queue: [Stackoverflow][copy_queue]

➡️  Priority Queue: [Python Docs][priority_queue]


[miro]: https://miro.com/welcomeonboard/YWcxVk5zcnNsRTVPOFlsaVZlTnhCdzU1MjNzU3VMbnJHOFdadndBOVV6TVBwY29GOXNZbjg5QndkNTc3OTZnc3wzMDc0NDU3MzQ5MzA5MzU1OTMx

[copy_queue]: https://stackoverflow.com/questions/32488533/how-to-clone-a-queue-in-python

[priority_queue]: https://docs.python.org/3/library/asyncio-queue.html
https://docs.python.org/3/library/heapq.html
pip install heapq