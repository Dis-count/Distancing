#coding:utf-8
# 是 DP_me 的加强版，把随机数都写在了函数的外层，而DP_me 中间有函数重复使用了 service = random.,  unnecessary.
# 随机得到的变量。
# 背包数量：backpack 物品数量：item
# 每个背包容量：space_backpack  每个物品占据空间：length  每个物品服务时间：service.
# 然后该程序的实现顺序是
# 函数 bag 得到动态规划(DP)求解 n*c 的value 值。
# 函数 show 返回 逻辑向量表示是否选中(0) 和 选中数量
# 函数  pretreatment 用于预处理
#  [2,6,5,4,7] by [2,6,8]  to [[2],[4,5,6],[7]] 分组 和 [[0],[3,2,1],[4]] 下标.
# 函数 multibag2  用于求 时间给定情况下的分配结果。
# 在我们的情况中，先求解 平均 ratio,  
# 函数 di  用于二分求解
# 函数 printmultibag2 用于打印结果。

# 这里需要定义一个面积函数，用于代替时间和空间的直接乘积

import numpy as np
import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt

def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    # for x in value:
    #     print(x)
    return value

def show(n, c, w, value):
    # Set the selected one as false  选了是 0 没选是1
    x = [True for i in range(n)]
    j = c
    k = 0  # Record the selected number
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            k = k+1
            x[i - 1] = False
            j -= w[i - 1]
    # for i in range(n):
    #     if x[i]:
    #         print('第', i+1, '个,', end='')
    return x,k

backpack = np.random.randint(3,7)  # 3-6 integer / number of backpacks
item = np.random.randint(10,21)   # 10-20 /Number of total items
space_backpack = np.random.randint(10,80,backpack)   # space for each backpack
service = np.random.randint(1,4,item) # service time for each item
length = np.random.randint(10,60,item)   # space for each item

# 还需要写一个 pretreatment 的函数 进行预处理
def pretreatment(length, space_backpack):
#   This function is used to convert the group into a list according to the capacity of all backpacks and return the ordinal number
# Example:  Input: two vectors  items: [2,6,5,4,7]  room capacity:   [2,6,8]
# Output:  List:  [[2],[4,5,6],[7]], [[0],[3,2,1],[4]]
    sorted_space = sorted(space_backpack)
    sorted_length= sorted(length)

    ordinal_length = np.argsort(length)  # obtain the ordinal number if we finish sort.
    ordinal_list = ordinal_length.tolist()

    segmentation = []
    order_list = []
    index = 0   #  indicate the ordinal

    for c in sorted_space:
        del_num = 0
        segmentation.append([])
        order_list.append([])

        for a in sorted_length:
            if a <= c:
                segmentation[index].append(a)
                order_list[index].append(ordinal_list[del_num])
                del_num = del_num + 1
            else:
                continue
        del sorted_length[0:del_num]
        del ordinal_list[0:del_num]
        index = index + 1

    return segmentation, order_list

def multibag2(backpack, item, c, space_backpack, service, length):
    # 从小到大根据c依次排, 可选集改变方式是去掉选出的物品,然后 加上 下一个范围的可选集
# 排不下时, 就增大c.
    service_item = list(service) # list service time for each item
    length_item = list(length) # list space for each item
    segmentation, order_list = pretreatment(length, space_backpack)
    segmentation.append([])
    order_list.append([])
    value_item = list(np.multiply(service,length)) # value for each item

    # ordinal_item = [i for i in range(item)]

#  segmentation 分别是每个背包间隔 第一个可选集为 segmentation[0]  到下一个背包时, 可选集为 segmentation[0] - selected + segmentation[1]

    rest_service = [service_item[i] for i in order_list[0]]  # 相当于 item 容量
    rest_value   = [value_item[i] for i in order_list[0]]    # 相当于 item 价值

    rest_item = len(segmentation[0])  # 初始 item 数量

    for i in range(backpack):

        value = bag(rest_item, c, rest_service, rest_value)
        rest_x,cut_num = show(rest_item, c, rest_service, value)  # list
        # for k in range(rest_item-1,-1,-1): # 注意这里要倒序  删除的时候才不会出问题
        #     if not rest_x[k]:
        #         sel = ordinal_item.pop(k) # 删除第k个元素

        rest_service = [rest_service[num] for num in range(rest_item) if rest_x[num]] + [service_item[j] for j in order_list[i+1]]

        rest_value = [rest_value[num] for num in range(rest_item) if rest_x[num]] + [value_item[j] for j in order_list[i+1]]

        rest_item = rest_item - cut_num + len(segmentation[i+1])

        if rest_item == 0:
            # print('\nDecrease c')
            return True

    if rest_item > 0:
        # print('\nIncrease c')
        return False

def di(a, b):  # 二分法(0,24)  用于调用 mutemultibag 返回c值
    c = round((a+b)/2)
    con = 0
    while c < (b-0.5) or (con < 10):
        flag = multibag2(backpack, item, c, space_backpack, service, length)  # 这里还需要写一个 mute 的函数用于 隐藏输出
        if flag > 0.5:  # Decrease c
            b = c
            c = round((a+b)/2)

        else:       # Increase c
            a = c
            c = round((a+b)/2)
        con +=1
    return c

c = di(0,24)
c = 6
multibag2(backpack, item, c, space_backpack, service, length)

def printmultibag2(backpack, item, c, space_backpack, service, length):
    #  用于输出 各个背包的占比结果. 需要 backpack space 是升序的.
    space_backpack = sorted(space_backpack)
    service_item = list(service) # list service time for each item
    length_item = list(length) # list space for each item

    segmentation, order_list = pretreatment(length, space_backpack)
    segmentation.append([])
    order_list.append([])

    value_item = list(np.multiply(service, length)) # value for each item

    rest_service = [service_item[i] for i in order_list[0]]  # 相当于 item 容量
    rest_value   = [value_item[i] for i in order_list[0]]    # 相当于 item 价值

    rest_item = len(segmentation[0])  # 初始 item 数量
    order_record = order_list[0]
    capa_ratio = [0] * backpack

    for i in range(backpack):

        value = bag(rest_item, c, rest_service, rest_value)
        # print('\n最大价值为:', value[rest_item][c])
        rest_x,cut_num = show(rest_item, c, rest_service, value)  # list
        print('\n第', i+1, '个背包中所装物品为:')
        for k in range(rest_item-1,-1,-1): # 注意这里要倒序  删除的时候才不会出问题
            if not rest_x[k]:
                sel = order_record.pop(k) # 记录并删除第k个元素
                print('第', sel+1, '个,', end='')

        rest_service = [rest_service[num] for num in range(rest_item) if rest_x[num]] + [service_item[j] for j in order_list[i+1]]

        rest_value = [rest_value[num] for num in range(rest_item) if rest_x[num]] + [value_item[j] for j in order_list[i+1]]
        capa_ratio[i] = value[rest_item][c] / (24 * space_backpack[i])
        rest_item = rest_item - cut_num + len(segmentation[i+1])
        order_record = order_record + order_list[i+1]

    return capa_ratio
c = 6
capa_ratio = printmultibag2(backpack, item, c, space_backpack, service, length)
capa_ratio
# Print c  but need to enlarge to 24, this in fact don't need

# if __name__ == '__main__':

# 直接按从小到大的顺序 先将room 进行排序
# 然后对于每个背包利用单背包问题进行求解即可
# 需要注意的是 每次单个背包结束后, 需要减去用掉的item 同时加上下个阶段需要用到的item

def binPacking(s,p,n,q): # s is ServiceTime, p Groupspace, n is GroupNumber, q is space

    try:
        p = list(p)

        subscript_i = len(s)
        subscript_k = len(q)

        m = gp.Model("Bin")

        x = m.addVars(subscript_i, subscript_k, vtype=GRB.BINARY, name="open")
        t = m.addVar(lb=0, name="min")
        m.update()

        # Set objective
        m.setObjective(t, GRB.MAXIMIZE)

        # Add constraints
        # constraint 1
        m.addConstrs((x[i, k]* p[i]) <= q[k] for i in range(subscript_i) for k in range(subscript_k))

        # constraint 2
        # m.addConstrs((gp.quicksum(x[i, k]*s[i] for i in range(subscript_i)) <= gp.quicksum(24.5-0.5*x[i, k] for i in range(subscript_i))) for k in range(subscript_k))
        m.addConstrs((gp.quicksum(x[i, k]*s[i] for i in range(subscript_i)) <= 24) for k in range(subscript_k))
        # constraint 3
        m.addConstrs((gp.quicksum((x[i, k]*s[i]*p[i])/(24*q[k]) for i in range(subscript_i)) >= t) for k in range(subscript_k))

        # constraint 4
        m.addConstrs((gp.quicksum(x[i, k] for k in range(subscript_k)) == 1) for i in range(subscript_i))

        m.write('BinPacking.lp')

        m.params.outputflag = 0
        m.optimize()

        x_ik =  m.getAttr('X', x)

        route = []

        # Generate the route for each room

        for k in range(subscript_k):
            route.append([0])

            terminate = True

            for i in range(subscript_i):
                if x_ik[i,k] >= 0.5:
                    route[k].append(i)

        # for i in range(subscript_i):
        #     print('Group {0} service time is {1}'.format(i+1, s[i]))
        #     print('The number of people is {0}'.format(p[i]))

        for i in range(len(route)):
            capa_ratio[i] = np.dot([s[j] for j in route[i][1:]], [p[j] for j in route[i][1:]])/ (24* q[i])
            print('The room {0} serves: {1}'.format(i+1, route[i][1:]))

        print(m.objVal)

        return route, capa_ratio

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')   # 输出最优情况

binPacking(service, length, item, space_backpack)
