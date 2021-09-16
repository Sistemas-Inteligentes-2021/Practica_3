# Practice 3
## 1. Describing the Problem
- The main problem that we want to solve is the N_Puzzle, finde the best and optimally solution given and initial state and defined a Goal State

## 2. Describing the Solution

To do

## 3. Experiments & Results
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


With Heuristic function 2:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 0.0050008296966552734 |  13  |  6  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 0.005003452301025391 |  15  |  7  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 0.006999015808105469 |  21  |  8  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 0.009000062942504883 |  30  |  9  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 0.009001016616821289 |  32  |  10  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 0.01399993896484375 |  44  |  14  |  14


With Heuristic function 3:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 0.004999637603759766 |  13  |  6  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 0.007002592086791992 |  24  |  7  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 0.0069997310638427734 |  26  |  8  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 0.007000923156738281 |  22  |  9  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 0.00799870491027832 |  27  |  10  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 0.04492330551147461 |  101  |  14  |  14


OPTIONAL
With Heuristic function 4:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 4.443898916244507 |  1052  |  92  |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 2.4921889305114746 |  781  |  169  |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 7.421672105789185 | 1356  |  234  |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 4.2287726402282715 |  1009  |  211  |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 2.2364230155944824 |  736  |  250  |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 8.661995649337769 |  1445  |  460  |  14



### 15 Puzzle (N = 15)

With Heuristic function 1:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - | -  |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - | -  |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  14


With Heuristic function 2:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - | -  |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - | -  |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  14


With Heuristic function 3:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - | -  |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - | -  |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  14


*OPTIONAL

With Heuristic function 4:

Initial State | Time(seconds) | Space States | Steps | Ideal Steps
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - | -  |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - | -  |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - | -  |  - |  14
## 4. Conclusions
---
Time Comparassion   N = 8

Initial State | Ideal Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | 6 | 0.004999876022338867  | 0.0050008296966552734  |  0.004999637603759766 
[1, 4, 2, 0, 5, 8, 3, 6, 7] | 7 | 0.006999969482421875  | 0.005003452301025391  |  0.007002592086791992 
[1, 4, 2, 5, 0, 8, 3, 6, 7] | 8 | 0.011001110076904297  | 0.006999015808105469  |  0.0069997310638427734 
[1, 0, 2, 5, 4, 8, 3, 6, 7] | 9 | 0.017000675201416016  | 0.009000062942504883  |  0.007000923156738281 
[1, 2, 0, 5, 4, 8, 3, 6, 7] | 10 | 0.0260159969329834  | 0.009001016616821289  |  0.00799870491027832 
[1, 2, 8, 5, 4, 7, 0, 3, 6] | 14 | 0.8903868198394775  | 0.01399993896484375  |  0.04492330551147461 

---

TIME COMPARISSON   N = 15


Initial State | Ideal Steps |  h1  | h2 | h3 
:---: | :---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - |  -  |  - | -
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - |  -  |  - |  -
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - |  -  |  - |  -
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  -  |  - |  -
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  -  |  - |  -
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - |  -  |  - |  -

In the end we could observe that according to the heuristic function we used, the number of states that expanded varied considerally. This is because the node that we choose to expand depends completelly in the heuristics function (h+g), also we prove that A star is a efficient algorith that is faster and more efective than BFS, ID or other not informed search. We can conclude that A star is an completeness and optimally algorithm. The best heuristic is the heuristic of Manhatan distance, next the inverse heuristic and finally the box in missplace heuristic.

We use 'Live Share' extension of VSCode to develop the code.

### Porotos h4 Heuristic : Euclidean Distance

To develop this heurisitc function we get inspired in the las class where the Mg. Gerard explained

What we do was find the euclidean distance beetwen the node visited and the goal state, we get the initial position of the element in the current node and the same position of the same element in goal state, then we substract them and get the absolute value of the substract and finally with Pitagoras equation we get the eucliden distance

### Comments

When we are developing the algorithm we get noticed that the priority queue librarie that python documentation give has not the problem that we experimented, we used both libraries thinking that the problem may be just one, but we have the same issue, we really try to find a way to solve the problem looking at forums like in stack overflow, github or looking for examples with that library but we didnt solve anything at the end we just simply decided to use a list and make a function to pick the best heuristic and we did that, the algorithm that we used for a star was the algorithm that we saw in classes and we comprobe it looking for another algorithm and we found the same.

## 5. Bibliography

➡️  Manual Tests, 8 Puzzle & 15 Puzzle : [Miro][miro]

➡️  Copy a Queue: [Stackoverflow][copy_queue]

➡️  Priority Queue: [Python Docs][priority_queue]

➡️  Priority Queue: [Python Docs][heapq]


[miro]: https://miro.com/welcomeonboard/YWcxVk5zcnNsRTVPOFlsaVZlTnhCdzU1MjNzU3VMbnJHOFdadndBOVV6TVBwY29GOXNZbjg5QndkNTc3OTZnc3wzMDc0NDU3MzQ5MzA5MzU1OTMx

[copy_queue]: https://stackoverflow.com/questions/32488533/how-to-clone-a-queue-in-python

[priority_queue]: https://docs.python.org/3/library/asyncio-queue.html
[heapq]: https://docs.python.org/3/library/heapq.html

