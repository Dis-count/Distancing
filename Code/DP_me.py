#coding:utf-8
import numpy as np

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
    # set the selected one as false
    x = [True for i in range(n)]
    j = c
    k = 0
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            k = k+1
            x[i - 1] = False
            j -= w[i - 1]
    # for i in range(n):
    #     if x[i]:
    #         print('第', i+1, '个,', end='')
    return x,k

if __name__ == '__main__':
    backpack = np.random.randint(3,7)  # 3-6 integer / number of backpacks
    item = np.random.randint(10,21)   # 10-20 /Number of total items
    c = 10  # Capacity of time
    service = np.random.randint(1,4,item) # weight for each item
    service_item = list(service) # weight for each item
    length = np.random.randint(10,60,item)
    length_item = list(length) # space for each item
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

        for k in range(rest_item-1,-1,-1): #注意这里要倒序  删除的时候才不会出问题
            if not rest_x[k]:
                sel = ordinal_item.pop(k) # 删除第k个元素
                print('第', sel, '个,', end='') # 有待改进

        rest_service = [rest_service[num] for num in range(rest_item) if rest_x[num]]

        rest_value = [rest_value[num] for num in range(rest_item) if rest_x[num]]

        rest_item = rest_item - cut_num

        if rest_item == 0:
            print('\nDecrease c')
            break

    if rest_item > 0:
        print('\nIncrease c')
