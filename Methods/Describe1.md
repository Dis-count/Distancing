##  Rules:

Maximize the distance.

Time Distancing:  The time gap of each used room.

Space Distancing:  Enlarge the space distancing of each room as much as possible. That is, if we have a room contains $q_k$ seat numbers, and distance ratio is r, then the number of customers who can be served $p_i$ is less than $q_k\cdot r$.  This condition can be set as a constraint.

##  Virables:
Room numbers $k \in K = \{1,2,...,|K|\}$.

A room contains seat number $q_k = \{....\}$.

Number of group customers $p_i = \{....\}$ for each $i \in N = \{1,...,n\}$.

$w_{ik}$ is the group i's start time in the room $k$.

$s_i$ is the service time for each group.(Given.)

Feasibility:
<!-- Time window constraints: -->
<!--
Time window $[a_{i},b_{i}]$ for each group, but it satisfies the time constraints during opening time [E, L] for the room. -->

Capacity constraint:

The largest number of customers in a group $p_i^*$ cannot exceed the product of the largest room capacity and ratio r, that is $p_i^* \leq q_k^*\cdot r$.

##  Solution:

<!-- Define the time distance $t_{i}$ for group i. It can be variable or the constant. In our case, we set the
time interval as the variable and it should be larger than half an hour. -->

Define a binary variable $x_{ijk}$ for each room. If the room k is used by (i,j) and i followed by j, then $x_{ijk} = 1$, else $x_{ijk} = 0$.

Define
$w_{ik}$ is the group i's start time in the room k.

$s_i$ is the service time for each group.(Given)

Set it as a time window VRP problem and add the distance constraints.

##  Analysis:

Add two virtual nodes (0,n+1) for each room. One is the start node, its time window can be a time point E meaning the room is open; the other is the end node, its time window is also a time point L meaning the room is closed.

##  Expected result:
Show the specific assignment for the coming people.

Give the sequence of each room, and the corresponding service start time.

Benchmark: Manual work.

Question: How to determine the distance for the only one group in a room?

          How to compare the result with the benchmark?

Input: Appointment hours $s_i$ for each group instead of the time window [a,b].

Add $p_0 = 0, s_0 = 0, E = 0/8, L=24.$

****************************************************
##MODEL :

$$
\begin{align}
max_{i,j,k} \quad & \sum_{(i,j) \in A} \sum_{k \in K} \frac{p_i}{q_k} x_{ijk} + \frac{1}{24} T_{ijk} \\
s.t. \quad  & \sum_{k \in K} \sum_{j \in \delta^+ (i)} x_{ijk} =1 & \forall i \in N  \\
& \sum_{j \in \delta^+ (0)} x_{0jk} =1 & \forall k \in K \\
& \sum_{i \in \delta^- (n+1)} x_{i,n+1,k} =1 & \forall k \in K \\
& \sum_{i \in \delta^- (j)} x_{ijk} - \sum_{i \in \delta^+ (j)} x_{ijk} = 0  & \forall k \in K, j \in N \\
& y_{ijk} \geq (x_{ijk}-1) M_{ij} & \forall k \in K, (i,j) \in A \\
& w_{0k}=E, w_{n+1,k}=L  & \forall k \in K \\
& x_{ijk} \in \{0,1\} & \forall k \in K, (i,j) \in A
\end{align}$$

The constraint (1) Minimizes the cost resulted by opening rooms.

--------------------------------------------

How to change the quadratic terms to the linear terms(linearization)

Note that the
$y =x_1 x_2$  where $x_1 \in \{0,1\}, x_2 \in [l,u] \to$
$$
\begin{align*}
& y \leq x_2 \\
& y \geq x_2 - u(1-x_1)    \\
& l x_1 \leq y \leq u x_1
\end{align*}$$

Let $(w_{jk}-w_{ik}-s_i) = y_{ijk}$ and $T_{ijk} = x_{ijk} y_{ijk}$

多加三个 i*j*k 数量的约束. Let $l = 0$.

$$
\begin{align}
& T_{ijk} \leq y_{ijk} \\
& T_{ijk} \geq y_{ijk} - u(1-x_{ijk})    \\
& T_{ijk} \leq u x_{ijk}
\end{align}$$


The constraint (2) Every group i which is followed by group j is only served once by one room k.

The constraint (3) For every room k, start from group 0.

The constraint (4) For every room k, end at group (n+1).

The constraint (5) For every room k, group j will leave when it is served.

The constraint (6) i start time + service time + interval(required) < next j start time. M for linearization.

<!-- The constraint (7) Time window constraints for every group. -->

The constraint (7) Add two node which indicate the start node and end node.
