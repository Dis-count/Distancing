- $q_k$ capacity. k\in K  The Number of room
- $s_i$ service time for each group.
- $p_i$ demand number of people.  $i \in N$
- Length for time.          24 for K. $s_i$ for N.
- Width for the capacity.   $q_k$ for K. $p_i$  for N.
- variable $x_{ik}$ indicates group i served by room k.

The Original model:
$$
\begin{align*}
min  \quad  & (\sum_i {x_{ik} s_i p_i})/(24 * q_k ),\quad \forall k \in K \\
s.t. \quad  & x_{ik} p_i \leq q_k,\quad  \forall i \in N, \forall k \in K  \\
& \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (\sum_{i\in N} x_{ik} - 1)*0.5,\quad \forall k \in K \\
& \sum_{k} x_{ik} =1,\quad \forall i \in N
\end{align*}$$

To:
$$
\begin{align}
max \quad & t \\
s.t. \quad  & x_{ik} p_i \leq q_k, \quad \forall i \in N,  \forall k \in K  \\
& \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (\sum_{i\in N} x_{ik} - 1)*0.5,\quad\forall k \in K \\
& t \leq \sum_i{x_{ik} s_i p_i}/(24 * q_k),\quad  \forall k \in K \\
& \sum_{k} x_{ik} =1,\quad \forall i \in N
\end{align}$$

The constraint (1) Capacity ratio.

The constraint (2) Capacity constraints |N|*|K|.

The constraint (3) Time constraints |K|.

The constraint (4) Objective capacity ratio constraints |K|.

The constraint (5) Every group is served once |N|.

Virables: |N|*|K|+1
