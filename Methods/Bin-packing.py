import numpy as np
import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt
# q_k capacity. k\in K  The Number of room
# i \in N
# s_i service time for each group.
# p_i demand number of people.
# Length for time.          24 for K. s_i for N.  product
# Width for the capacity.   q_k for K. p_i  for N.
# variable x_ik
# help(gp.Model.addMVar)

def binPacking(s,p,n,q):
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
        print('Main-Encountered an attribute error')

def capRatio(route, n):
    capacity_ratio = [0]*n
    for i in range(len(route)):
        cap1 = capacity[i]
        for j in route[i][1:]:
            capacity_ratio[j-1] = p[j-1]/cap1
    return capacity_ratio

def finishTime(route, n):
    finish_time = [0]*n
    for i in range(len(route)):
        k = -0.5
        for j in route[i][1:]:
            finish_time[j-1] = k + 0.5 + s[j-1]
            k = finish_time[j-1]  # record the finish time
    return finish_time

def inv(route, n):

    machineNum = [0]*n
    # because the first one is 0 for route.
    for i in range(len(route)):
        for j in route[i][1:]:
            machineNum[j-1] = i +1

    return machineNum

def gantt(macInfo, flow, macStartTime, Capacity, workpiece):
    for j in range(len(macInfo)):
        i = macInfo[j]
        plt.bar(i, flow[j], Capacity[j], bottom=macStartTime[j])
        plt.text(i,macStartTime[j] + flow[j] / 8, 'G%s' % (workpiece[j]), color = "black", size = 15)

n = 10   # The number of group

ss = np.random.randint(1,4,n)
s = list(ss)   # The time length of each group

pp = np.random.randint(10,60,n)
p = list(pp)   # The number of people for each group

capacity = [100,150,150,100]  # The capacity for the room.
route = binPacking(s,p,n,capacity)

capacity_ratio = capRatio(route, n)  # The capacity ratio

machineNum = inv(route, n)  # The ordinal number.

finish_Time = finishTime(route, n)

J = list(range(1,n+1))  # Job List

StartTime = [finish_Time[i] - s[i] for i in range(0,n)]

gantt(machineNum, s, StartTime,capacity_ratio ,J)
# QUESTION:  is How to Generate the sequence you need.
#  How to change a  list  1[ 2 3 5 7]
                #         2[ 1 6  ]
                #         3[ 4 8  ]
# i.e. route = [[2,3,5,7], [1,6], [4,8]]
#  To  [2 1 1 3 1 2 1 3 ]
#  At first, generate the list is full of zeros.

room_num = len(capacity)

for i in range(room_num):
    plt.vlines(i + 1.5, 0, 15, colors = "c", linestyles = "dashed")

plt.yticks(np.arange(0, 16, step =1))

plt.xticks(np.arange(0.5, room_num + 0.5, step =1))

plt.show()
