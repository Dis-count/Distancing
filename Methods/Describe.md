##  Rules:
Time Distancing :  Maximize the time gap of each used room.

Space Distancing:  Maximize the space distancing of each room as much as possible. That is, if we have a room contains q_k seat numbers, and distance ratio is r, then the number of customers who can be served p_i is less than q_k/r.  This thing can be set as constraints.


##  Virable:
a room contains seat number $q_k = \{3 ,5, 8 ...\}$

room numbers $k \in \{1,2,...,K\}$

number of group customers $p_i = \{....\}$ for each $i \in \{1,...N\}$.

feasibility:

time window constraints



time window $[a_{i},b_{i}]$ for each group, but it satisfy the time constraints during opening time [E, L] for the room.

$w_{ik}$ is the group i's start time in the room k.

$s_i$ is the service time for each group.(Given)

##  Soluiton:

1. At first, sort the customers' group start time. Then assign them to the corresponding room by the space distancing rule.

2. Set the Maximize time distancing as the objective function.

Define the time distance $t_{ij}$ for each room. Time interval we set it as 0.5 hours.

Define a binary variable $x_{ijk}$ for each room. If the room is used by (i,j) and i followed by j, then $x_{ijk} = 1$, else $x_{ijk} = 0$.


3. How to set it as the constraints?

Set it as a timewindow VRP problem and add the constraints of distance.

##  Analysis:

More customers, less time gap we can realize.


##  Expected result:

Show the specific assignment for the coming people.

Benchmark: First in First out.

Question: how to realize it under time window?

****************************************************
##MODEL :

$$
\begin{align}
min_{i,j,k} \quad & \sum_{(i,j) \in A} \sum_{k \in K} c_{ij} x_{ijk} \\
s.t. \quad  & \sum_{k \in K} \sum_{j \in \delta^+ (i)} x_{ijk} =1 & \forall i \in N  \\
& \sum_{i \in \delta^- (j)} x_{ijk} - \sum_{i \in \delta^+ (j)} x_{ijk} = 0  & \forall k \in K, j \in N \\
& w_{ik} + s_i + t_{ij} - w_{jk} \leq (1-x_{ijk}) M_{ij}, & \forall k \in K (i,j) \in A \\
& a_i \sum_{j \in \delta^+ (i)} x_{ijk} \leq w_{ik} \leq b_i \sum_{j \in \delta^+ (i)} x_{ijk} & \forall k \in K, j \in N \\
& E \leq w_{ik} \leq L  & \forall k \in K, i \in N \\
& t_{ij} \geq 0.5 x_{ijk}  & \forall k \in K, (i,j) \in A  \\
& p_i \sum_{j \in \delta^+ (i)} x_{ijk} \leq 0.3 q_k & \forall k \in K, i \in N \\
\end{align}$$

The constraint (1) minimize the cost resulted by opning a

The constraint (2)

The constraint (3)

The constraint (4)

The constraint (5)

The constraint (6)

The constraint (7)

The constraint (8)
