import numpy as np
import gurobipy as gp
from gurobipy import GRB

# q_k capacity.
# s_i service time for each group.
# p_i demand number of people.
# variable x_ijk  w_ik t_i
# i \in N (not include 0 and N+1)
help(gp.Model.addMVar)

def TW(s,q,p):

    try:
        M = 1e4
        E = 0
        L = 24

        a = [0,8, 14,10,19,0]
        b = [0,11,15,16,21,0]
        subscript_i = len(s)  # the number of nodes
        subscript_j = subscript_i
        subscript_k = len(q)

        m = gp.Model("TW_dis")

        x = m.addVars(subscript_i, subscript_j, subscript_k, vtype=GRB.BINARY, name="open")
        w = m.addVars(subscript_i,subscript_k, lb=0, name="start")
        t = m.addVars(subscript_i, lb=0, name="interval")
        m.update()

        # Set objective   c_ij =1
        m.setObjective(x.sum(), GRB.MINIMIZE)

        # Add constraints
        # constraint 1
        m.addConstrs((gp.quicksum(x[i,j,k] for j in range(1,subscript_j) for k in range(subscript_k)) == 1) for i in range(1,subscript_i-1))

        # constraint 2

        m.addConstrs((gp.quicksum(x[i,j,k] for i in range(subscript_i)) == gp.quicksum(x[j,i,k] for i in range(subscript_i))) for j in range(1,subscript_j-1) for k in range(subscript_k))

        # constraint 3
        m.addConstrs((gp.quicksum(x[0,j,k] for j in range(1,subscript_j)) == 1) for k in range(subscript_k))

        # constraint 4
        m.addConstrs((gp.quicksum(x[i,subscript_j-1,k] for i in range(subscript_i-1)) == 1) for k in range(subscript_k))

        # constraint 5
        m.addConstrs((w[i,k] + s[i] + t[i] -w[j,k]) <= ((1-x[i,j,k])*M) for k in range(subscript_k) for i in range(subscript_i) for j in range(subscript_j))

        # constraint 6.1
        m.addConstrs((gp.quicksum(x[i,j,k]*a[i] for j in range(1,subscript_j)) <= w[i,k]) for k in range(subscript_k) for i in range(1,subscript_i-1))

        # constraint 6.2
        m.addConstrs((gp.quicksum(x[i,j,k]*b[i] for j in range(1,subscript_j)) >= w[i,k]) for k in range(subscript_k) for i in range(1,subscript_i-1))

        # constraint 7
        m.addConstrs(w[0,k] == E for k in range(subscript_k))
        m.addConstrs(w[subscript_i-1,k] == L for k in range(subscript_k))

        # constraint 8
        m.addConstrs((gp.quicksum(x[i,j,k] for j in range(1,subscript_j)) <= 2*t[i]) for k in range(subscript_k) for i in range(1,subscript_i-1))

        # constraint 9
        m.addConstrs((gp.quicksum(x[i,j,k] for j in range(1,subscript_j)) *p[i] <= 0.3*q[k]) for i in range(1,subscript_i-1) for k in range(subscript_k))

        # constructs 10
        m.addConstrs(x[i,i,k] ==0 for i in range(subscript_i) for k in range(subscript_k))

        m.write('TW.lp')

        m.params.outputflag = 0
        m.optimize()

        x_ijk =  m.getAttr('X', x)

        w_ik = m.getAttr('X', w)

        route = []
        serviceT = []
        # Generate the route and Specific service time
        for k in range(subscript_k):
            route.append([0])
            i = 0
            serviceT.append([w_ik[i,k]])
            terminate = True
            while terminate:
                for j in range(subscript_j):
                    if x_ijk[i,j,k] >= 0.5:

                        route[k].append(j)
                        serviceT[k].append(w_ik[j,k])
                        i = j
                        break
                if (i == subscript_i-1):
                    terminate = False
        print('The route is' + str(route))
        print('The service start time is' + str(serviceT))

        return m.objVal

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')

s = [0,2,2,2,2,0]
q = [100,200]
p = [0,35,30,44,40,0]

TW(s,q,p)
