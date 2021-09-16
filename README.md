# Practice 3
## 1. Describing the Problem
- The main problem that we want to solve is the N_Puzzle, finde the best and optimally solution given and initial state and defined a Goal State

## 2. Describing the Solution

To do

## 3. Experiments & Results
### 8 Puzzle (N = 8)

With Heuristic function 1:

Initial State | Time | Steps | Ideal Steps
:---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | - |  - |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | - |  - |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | - |  - |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | - |  - |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | - |  - |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | - |  - |  14


With Heuristic function 2:

Initial State | Time | Steps | Ideal Steps
:---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | - |  - |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | - |  - |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | - |  - |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | - |  - |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | - |  - |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | - |  - |  14


With Heuristic function 3:

Initial State | Time | Steps | Ideal Steps
:---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | - |  - |  6
[1, 4, 2, 0, 5, 8, 3, 6, 7] | - |  - |  7
[1, 4, 2, 5, 0, 8, 3, 6, 7] | - |  - |  8
[1, 0, 2, 5, 4, 8, 3, 6, 7] | - |  - |  9
[1, 2, 0, 5, 4, 8, 3, 6, 7] | - |  - |  10
[1, 2, 8, 5, 4, 7, 0, 3, 6] | - |  - |  14


### 15 Puzzle (N = 15)

With Heuristic function 1:

Initial State | Time | Steps | Ideal Steps
:---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  14


With Heuristic function 2:

Initial State | Time | Steps | Ideal Steps
:---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  14


With Heuristic function 3:

Initial State | Time | Steps | Ideal Steps
:---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - |  - |  6
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - |  - |  7
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - |  - |  8
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  9
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  10
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  14

## 4. Conclusions
---
Time Comparassion   N = 8

Initial State |  h1  | h2 | h3 
:---: | :---: | :---: | :---:
[1, 4, 2, 3, 5, 8, 0, 6, 7] | - |  - |  -
[1, 4, 2, 0, 5, 8, 3, 6, 7] | - |  - |  -
[1, 4, 2, 5, 0, 8, 3, 6, 7] | - |  - |  -
[1, 0, 2, 5, 4, 8, 3, 6, 7] | - |  - |  -
[1, 2, 0, 5, 4, 8, 3, 6, 7] | - |  - |  -
[1, 2, 8, 5, 4, 7, 0, 3, 6] | - |  - |  -


---

TIME COMPARISSON   N = 15


Initial State |  h1  | h2 | h3 
:---: | :---: | :---: | :---:
[1, 5, 2, 3, 4, 6, 10, 7, 8, 9, 14, 11, 12, 0, 13, 15] | - |  - | -
[1, 5, 2, 3, 4, 6, 10, 7, 8, 0, 14, 11, 12, 9, 13, 15] | - |  - |  -
[1, 5, 2, 3, 4, 6, 10, 7, 0, 8, 14, 11, 12, 9, 13, 15] | - |  - |  -
[1, 5, 2, 3, 0, 6, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  -
[1, 5, 2, 3, 6, 0, 10, 7, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  -
[1, 2, 10, 3, 6, 5, 7, 0, 4, 8, 14, 11, 12, 9, 13, 15] | - |  - |  -

In the end we could observe that according to the heuristic function we used, the number of states that expanded varied. This was due to the shuffle function that we have when there is a tie in priority. 

We use 'Live Share' extension of VSCode to develop the code.

### Porotos h4 Heuristic : Euclidean Distance

Para desarrollar esta heuristica nos inspiramos en una clase donde vimos este metodo.

Lo que hicimos fue obtener la posicion inicial del elemento y la posicion del mismo elemento en el goal state, luego restamos ambas coordenadas obteniendo el valor absoluto, finalmente con la ecuacion de pitagoras obteniamos the euclidean distance. 
## 5. Bibliography

➡️  Manual Tests, 8 Puzzle & 15 Puzzle : [Miro][miro]

➡️  Copy a Queue: [Stackoverflow][copy_queue]

➡️  Priority Queue: [Python Docs][priority_queue]


[miro]: https://miro.com/welcomeonboard/YWcxVk5zcnNsRTVPOFlsaVZlTnhCdzU1MjNzU3VMbnJHOFdadndBOVV6TVBwY29GOXNZbjg5QndkNTc3OTZnc3wzMDc0NDU3MzQ5MzA5MzU1OTMx

[copy_queue]: https://stackoverflow.com/questions/32488533/how-to-clone-a-queue-in-python

[priority_queue]: https://docs.python.org/3/library/asyncio-queue.html