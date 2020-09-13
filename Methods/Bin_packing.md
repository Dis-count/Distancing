change

# min (\sum_i {x_{ik} s_i p_i})/ (24 * q_k )  k \in K
# capacity  x_ik p_i \leq q_k  \forall i \in N  \forall k \in K
# time      \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (数量-1)*最小distance

\to

# max t
# capacity  x_ik p_i \leq q_k  \forall i \in N  \forall k \in K
# time      \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (\sum_{i\in N} x_{ik} - 1)*最小distance
# t \leq \sum_i{x_{ik} s_i p_i}/(24 * q_k)  k \in K
# \sum_{k} x_{ik} =1   i \in N
