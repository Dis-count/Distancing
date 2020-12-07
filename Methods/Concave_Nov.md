- $q_k$ capacity. $k\in K$  The Number of room
- $s_i$ service time for each group.
- $p_i$ demand number of people.  $i \in N$
- Length for time.          24 for K. $s_i$ for N.
- Width for the capacity.   $q_k$ for K. $p_i$  for N.
- variable $x_{ik}$ indicates group i served by room k.

Now we change the objective function $q_k$ to a concave function $f(q_k)$. How to influence the result?

Search for the minimization makespan problem. (最小最大完工时间)

To be specific, how to deal/handle with minimax format?

基本想法是比较两种方法，minimax is what we want, and maxmin will provide a lower bound, but we are still not sure how this method can improve our results.

Define 面积： S = F(t,s)  t for time, s for space.
For example, at here, F(t,s) can be t*f(s), where f(s) is a concave function.

具体方法和需要注意的细节：
1. 将 items 根据实际的 room size 按从小到大的顺序排列。(如 [4,4,4,6],[8,8],[10,10,10]  room size [6,8,10])
2. 从小到大 装 room ，用 DP 求解. (矛盾点在于如果要用DP 需要知道时间 这个时候就不能用占比控制时间，一个可行的方法是 先求出占比r, 用 DP 在24 小时内进行求解 占比会大于r 利用二分求解时间，找到最接近的 r 的方案，要么大要么小(可以用反证证明只有这两种选择)。可以把大小作为每个room 分出来的枝，前面的 room 分支会影响后面 room 的分支。如果可以证明前者的序列是最优的，则后面也是最优的，这样遍历的复杂度是2^(|room|).)
3. 减去使用过的 item 加入新的 item, 继续用 DP 求解.
4. 如何在求解过程中剪去前面得到的分支而不是使用遍历的方法还需要思考。(比如 当room 很大时，这个时候取大会较好，因为如果它小的话，别的小的room 超出会更大，这样 minmax 就会变大。)

The Original model:
最小化 (最大 占据空间 k \in K)
$$
\begin{align*}
\min \quad (\max & (\sum_i { x_{ik} s_i p_i})/(24 * f(q_k)),\quad \forall k \in K) \\
s.t. \quad  & x_{ik} p_i \leq q_k,\quad  \forall i \in N, \forall k \in K  \\
& \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (\sum_{i\in N} x_{ik} - 1)*0.5,\quad \forall k \in K \\
& \sum_{k} x_{ik} =1,\quad \forall i \in N
\end{align*}$$

To:
$$
\begin{align}
(M1) = max \quad & t \\
s.t. \quad  & x_{ik} p_i \leq q_k, \quad \forall i \in N,  \forall k \in K  \\
& \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (\sum_{i\in N} x_{ik} - 1)*0.5,\quad\forall k \in K \\
& t \leq \sum_i{x_{ik} s_i p_i}/(24 * q_k),\quad  \forall k \in K \\
& \sum_{k} x_{ik} =1,\quad \forall i \in N
\end{align}$$

$$
\begin{align}
(M2) = min \quad & t \\
s.t. \quad  & x_{ik} p_i \leq q_k, \quad \forall i \in N,  \forall k \in K  \\
& \sum_{i\in N} x_{ik} s_i \leq T_k = 24 - (\sum_{i\in N} x_{ik} - 1)*0.5,\quad\forall k \in K \\
& t \geq \sum_i{x_{ik} s_i p_i}/(24 * q_k),\quad  \forall k \in K \\
& \sum_{k} x_{ik} =1,\quad \forall i \in N
\end{align}$$

At first, it is clear that M1(max min) < M2(min max).
Thus, the true value will be between M1 and M2.


So what is the difference?

The constraint (1) Capacity ratio.

The constraint (2) Capacity constraints |N|*|K|.

The constraint (3) Time constraints |K|.

The constraint (4) Objective capacity ratio constraints |K|.

The constraint (5) Every group is served once |N|.

Virables: |N|*|K|+1, refers to $x_{ik},t$
