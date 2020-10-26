#coding:utf-8
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

def multibag(backpack, item, c):

    space_backpack = np.random.randint(10,80,backpack)  # space for each backpack
    service = np.random.randint(1,4,item) # service time for each item
    service_item = list(service) # list service time for each item
    length = np.random.randint(10,60,item)   # space for each item
    length_item = list(length) # list space for each item
    # total_product = np.dot(length, servce)
    # total_space = 24 * sum(space_backpack)
    # c = 24 * ratio  # Capacity of time   # ratio 的方案不太行  至少对于room 和 group space 差距过大的情况 不适合
    # ratio = total_product/ total_space   # The ratio between item space and backpack space
    value_item = list(np.multiply(service,length)) # value for each item
    print('共有', backpack, '个背包')
    print('共有', item, '个物品')

    rest_service = service_item
    rest_value = value_item
    rest_item = item

    ordinal_item = [i for i in range(item)]

    for i in range(backpack):

        value = bag(rest_item, c, rest_service, rest_value)
        print('\n最大价值为:', value[rest_item][c])
        rest_x,cut_num = show(rest_item, c, rest_service, value)  #list
        print('第', i+1, '个背包中所装物品为:')

        for k in range(rest_item-1,-1,-1): # 注意这里要倒序  删除的时候才不会出问题
            if not rest_x[k]:
                sel = ordinal_item.pop(k) # 删除第k个元素
                print('第', sel, '个,', end='')

        rest_service = [rest_service[num] for num in range(rest_item) if rest_x[num]]

        rest_value = [rest_value[num] for num in range(rest_item) if rest_x[num]]

        rest_item = rest_item - cut_num

        if rest_item == 0:
            print('\nDecrease c')
            return True

    if rest_item > 0:
        print('\nIncrease c')
        return False

def mutemultibag(backpack, item, c):  # ignore the print

    space_backpack = np.random.randint(10,80,backpack)  # space for each backpack
    service = np.random.randint(1,4,item) # service time for each item
    service_item = list(service) # list service time for each item
    length = np.random.randint(10,60,item)   # space for each item
    length_item = list(length) # list space for each item
    # total_product = np.dot(length, servce)
    # total_space = 24 * sum(space_backpack)
    # ratio = total_product/ total_space   # The ratio between item space and backpack space
    # c = 24 * ratio  # Capacity of time   # ratio 的方案不太行  至少对于room 和 group space 差距过大的情况 不适合
    value_item = list(np.multiply(service,length)) # value for each item
    # print('共有', backpack, '个背包')
    # print('共有', item, '个物品')
    rest_service = service_item
    rest_value = value_item
    rest_item = item
    ordinal_item = [i for i in range(item)]

    for i in range(backpack):
        value = bag(rest_item, c, rest_service, rest_value)
        # print('\n最大价值为:', value[rest_item][c])
        rest_x,cut_num = show(rest_item, c, rest_service, value)  #list
        # print('第', i+1, '个背包中所装物品为:')
        for k in range(rest_item-1,-1,-1): # 注意这里要倒序  删除的时候才不会出问题
            if not rest_x[k]:
                sel = ordinal_item.pop(k) # 删除第k个元素
                # print('第', sel, '个,', end='')

        rest_service = [rest_service[num] for num in range(rest_item) if rest_x[num]]

        rest_value = [rest_value[num] for num in range(rest_item) if rest_x[num]]

        rest_item = rest_item - cut_num

        if rest_item == 0:
            # print('\nDecrease c')
            return True

    if rest_item > 0:
        # print('\nIncrease c')
        return False

def multibag2(backpack, item, c):  # 从小到大根据c依次排, 可选集改变方式是去掉选出的物品,然后并上下一个范围的可选集
# 排不下时, 就增大c.
    space_backpack = np.random.randint(10,80,backpack)  # space for each backpack
    service = np.random.randint(1,4,item) # service time for each item
    service_item = list(service) # list service time for each item
    length = np.random.randint(10,60,item)   # space for each item
    length_item = list(length) # list space for each item
    # total_product = np.dot(length, servce)
    # total_space = 24 * sum(space_backpack)
    # ratio = total_product/ total_space   # The ratio between item space and backpack space
    value_item = list(np.multiply(service,length)) # value for each item
    rest_service = service_item
    rest_value = value_item
    rest_item = item
    ordinal_item = [i for i in range(item)]

#  segmentation 分别是每个背包间隔 第一个可选集为segmentation[0]  到下一个背包时, 可选集为 segmentation[0] - selected + segmentation[1]

    rest_item = length(segmentation[0])  # 初始值

    for i in range(backpack):

        value = bag(rest_item, c, rest_service, rest_value)
        rest_x,cut_num = show(rest_item, c, rest_service, value)  # list
        for k in range(rest_item-1,-1,-1): # 注意这里要倒序  删除的时候才不会出问题
            if not rest_x[k]:
                sel = ordinal_item.pop(k) # 删除第k个元素

        rest_service = [rest_service[num] for num in range(rest_item) if rest_x[num]]

        rest_value = [rest_value[num] for num in range(rest_item) if rest_x[num]]
# list(set(a).union(set(b)))  用于求并集
        rest_item = rest_item + length(segmentation[i])
a = [1,2,3,4]

b =[1,2,3]
list(set(a).union(set(b)))
list(a.union(b))

        if rest_item == 0:
            # print('\nDecrease c')
            return True

    if rest_item > 0:
        # print('\nIncrease c')
        return False



def di(a, b):  # 二分法(0,24)  用于调用 mutemultibag 返回c值
    c = round((a+b)/2)

    while c < (b-0.5):
        flag = mutemultibag(backpack, item, c)  # 这里还需要写一个 mute 的函数用于 隐藏输出
        if flag > 0.5:  # Decrease c
            b = c
            c = round((a+b)/2)

        else:       # Increase c
            a = c
            c = round((a+b)/2)
    return c

# Print c  but need to enlarge to 24, this in fact don't need
length = np.random.randint(10,60,item)
space_backpack = np.random.randint(10,80,backpack)
# 还需要写一个 pretreatment 的函数 进行预处理
def pretreatment(length, space_backpack):
#   This function is used to convert the group into a list according to the capacity of all backpacks
# Example:  Input: two vectors  items: [2,4,5,6,7]  room capacity:   [2,6,8]
# Output:  List:  [[2],[4,5,6],[7]]
    sorted_space = sorted(space_backpack)
    sorted_length= sorted(length)
    segmentation = []
    index = 0   #  indicate the ordinal
    for c in sorted_space:
        segmentation.append([])
        for a in sorted_length:
            if a <= c:
                segmentation[index].append(a)
                del sorted_length[0]
            else:
                continue
        index = index + 1

    return segmentation

pretreatment(length, space_backpack)


# if __name__ == '__main__':

# 直接按从小到大的顺序 先将room 进行排序
# 然后对于每个背包利用单背包问题进行求解即可
# 需要注意的是 每次单个背包结束后, 需要减去用掉的item 同时加上下个阶段需要用到的item

def binPacking(s,p,n,q):
    # s is ServiceTime, p Groupspace, n is GroupNumber, q is space
    try:
        pp = np.random.randint(10,60,n)
        p = list(pp)

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
        m.addConstrs((gp.quicksum(x[i, k]*s[i] for i in range(subscript_i)) <= gp.quicksum(24.5-0.5*x[i, k] for i in range(subscript_i))) for k in range(subscript_k))

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
                    route[k].append(i+1)

        # for i in range(subscript_i):
        #     print('Group {0} service time is {1}'.format(i+1, s[i]))
        #     print('The number of people is {0}'.format(p[i]))

        for i in range(len(route)):
            print('The room {0} serves: {1}'.format(i+1, route[i][1:]))

        print(m.objVal)

        return route

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')   # 输出最优情况
