# 设f[i][v][u]表示前i件物品付出两种代价分别为v和u时可获得的最大价值。
# 状态转移方程就是：f[i][v][u]=max{f[i-1][v][u],f[i-1][v-a[i]][u-b[i]]+w[i]}。
# 如前述方法，可以只使用二维的数组：f[v][u]=max{f[v][u],f[v-a[i]][u-b[i]]+w[i]}
# 当每件物品只可以取一次时，变量v和u采用逆序的循环，当物品有如完全背包问题时采用顺序的循环。

def twodimentional(n, c1,c2, w1,w2, v):
    """
    测试数据：
    n = 6  物品的数量
    c1 = 10 书包能承受的重量1
    c2 = 13 书包能承受的重量2
    w1 = [2, 2, 3, 1, 5, 2] 每个物品的重量1
    w2 = [1, 2, 3, 3, 2, 1] 每个物品的重量2
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c2 + 1)] for i in range(c1 + 1)]
    for k in range(1, n+1):
        for i in range(c1, 0, -1):
            for j in range(c2, 0, -1):
                if j >= w2[k - 1] and i >= w1[k-1]:
                    value[i][j] = max(value[i][j], value[i-w1[k - 1]][j - w2[k - 1]] + v[k - 1])
    return value[-1][-1]

#  还需要思考 装入了哪些 items
#  必须要三维的向量反向才能得到结果

def twodimentional2(n, c1,c2, w1,w2, v):
    """
    测试数据：
    n = 6  物品的数量
    c1 = 10 书包能承受的重量1
    c2 = 13 书包能承受的重量2
    w1 = [2, 2, 3, 1, 5, 2] 每个物品的重量1
    w2 = [1, 2, 3, 3, 2, 1] 每个物品的重量2
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[[0 for j in range(c2 + 1)] for i in range(c1 + 1)] for k in range(n + 1)] # 定义三维向量
    for k in range(1, n+1):
        for i in range(1, c1 + 1):
            for j in range(1, c2 + 1):
                if j >= w2[k - 1] and i >= w1[k-1]:
                    value[k][i][j] = max(value[k][i][j], value[k][i-w1[k - 1]][j - w2[k - 1]] + v[k - 1])
    return value

# test
n = 6
c1 = 10
c2 = 13
w1 = [2, 2, 3, 1, 5, 2]
w2 = [1, 2, 3, 3, 2, 1]
v = [2, 3, 1, 5, 4, 3]
value = twodimentional(n, c1,c2, w1,w2, v)
value2 = twodimentional2(n, c1,c2, w1,w2, v)
value2[-1][-1][-1]

def show(n, c1,c2, w1,w2, value):
    # Set the selected one as false  选了是 0 没选是1
    x = [True for i in range(n)]
    i = c1
    j = c2
    t = 0  # Record the selected number
    for k in range(n, 0, -1):
        if value[k][i][j] > value[k - 1][i][j]:
            t = t + 1
            x[k - 1] = False
            i -= w1[k - 1]
            j -= w2[k - 1]
    # for i in range(n):
    #     if x[i]:
    #         print('第', i+1, '个,', end='')
    return x,t

show(n, c1,c2, w1,w2, value2)
