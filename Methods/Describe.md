##  Rules:
Time Distancing :  Maximize the time gap of each used room.

Space Distancing:  Maximize the space distancing of each room as much as possible. That is, if we have a room contains q_k seat numbers, and distance ratio is r, then the number of customers who can be served p_i is less than q_k/r.  This thing can be set as constraints.


##  Virable:
a room contains seat number $q_k = \{....\}$

room numbers $k \in \{1,2,...,K\}$

number of group customers $p_i = \{....\}$ for each $i \in \{1,...,N\}$.

Feasibility:

Time window constraints

Time window $[a_{i},b_{i}]$ for each group, but it satisfies the time constraints during opening time [E, L] for the room.

$w_{ik}$ is the group i's start time in the room k.

$s_i$ is the service time for each group.(Given)

##  Soluiton:

1. At first, sort the customers' group start time. Then assign them to the corresponding room by the space distancing rule.

2. Define the time distance $t_{i}$ for group i. Time interval we set it as 0.5 hours.

Define a binary variable $x_{ijk}$ for each room. If the room is used by (i,j) and i followed by j, then $x_{ijk} = 1$, else $x_{ijk} = 0$.


3. How to set it as the constraints?

Set it as a time window VRP problem and add the distance constraints.

##  Analysis:

More customers, less time gap we can realize.


##  Expected result:

Show the specific assignment for the coming people.

Benchmark: First in First out.

Question: how to realize it under time window?
          how to determine the objective function.

****************************************************
##MODEL :

$$
\begin{align}
min_{i,j,k} \quad & \sum_{(i,j) \in A} \sum_{k \in K} c_{ij} x_{ijk} \\
s.t. \quad  & \sum_{k \in K} \sum_{j \in \delta^+ (i)} x_{ijk} =1 & \forall i \in N  \\
& \sum_{j \in \delta^+ (0)} x_{0jk} =1 & \forall k \in K \\
& \sum_{i \in \delta^- (n+1)} x_{i,n+1,k} =1 & \forall k \in K \\
& \sum_{i \in \delta^- (j)} x_{ijk} - \sum_{i \in \delta^+ (j)} x_{ijk} = 0  & \forall k \in K, j \in N \\
& w_{ik} + s_i + t_{i} - w_{jk} \leq (1-x_{ijk}) M_{ij} & \forall k \in K, (i,j) \in A \\
& a_i \sum_{j \in \delta^+ (i)} x_{ijk} \leq w_{ik} \leq b_i \sum_{j \in \delta^+ (i)} x_{ijk} & \forall k \in K, i \in N \\
& w_{0k}=E, w_{n+1,k}=L  & \forall k \in K \\
& t_{i} \geq 0.5 \sum_{j \in \delta^+(i)} x_{ijk}  & \forall k \in K, i \in N  \\
& p_i \sum_{j \in \delta^+ (i)} x_{ijk} \leq 0.3 q_k & \forall k \in K, i \in N \\
& x_{ijk} \in \{0,1\} & \forall k \in K, (i,j) \in A
\end{align}$$

The constraint (1) Minimizes the cost resulted by opening rooms.

The constraint (2) Every group i which is followed by group j is only served once by one room k.

The constraint (3) For every room k, start from group 0.

The constraint (4) For every room k, end at group (n+1).

The constraint (5) For every room k, group j will leave when it is served.

The constraint (6) i start time + service time + interval(required) < next j start time. M for linearize.

The constraint (7) Time constraints for every group.

The constraint (8) Add two node indicate the start node and end node.

The constraint (9) Time distance constraint.

The constraint (10) Space distance constraint.
