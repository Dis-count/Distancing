##  Rules:
Time Distancing :  Maximize the time gap of each used room.

Space Distancing:  Maximize the space distancing of each room as much as possible. That is, if we have a room contains s_i seat numbers, and distance ratio is r, then the number of customers who can be served g_i is less than s_i/r.  This thing can be set as constraints.


##  Virable:
a room contains seat number s_i = {3 ,5, 8 ...}

room numbers owned n_j = {6, 4, 3 ...}  \sum_j n_j

group of customers g_k = {....}

group numbers |g_k| = g , at least \sum_j {n_j}, or this question would be meanless.

start time t_k for each group , but it satisfy the time constraints during opening time [t_start, t_end].

time enduration [1, 2, 3] hours.


##  Soluiton:

1. At first, sort the customers' group start time. Then assign them to the corresponding room by the space distancing rule.

2. Set the Maximize time distancing as the objective function.

Define the distance d_l for each room, l \in {1,2,...,\sum_j n_j}

Define a binary variable b_l for each room. If the room is used then b_l = 1, else b_l = 0.

Define the Usage time of each room u_l :

if u_l == 1, then gap ==0
if u_l > 1, then max gap
if u_l == 0, then 

max \sum_l d_l


3. How to set it as the constraints?


##  Analysis:

More customers, less time gap we can realize.


##  Expected result:

Show the specific assignment for the coming people.


Benchmark: First in First out.
