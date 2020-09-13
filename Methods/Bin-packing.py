import numpy as np
import gurobipy as gp
from gurobipy import GRB

# q_k capacity. k\in K  The Number of room
# i \in N
# s_i service time for each group.
# p_i demand number of people.
# Length for time.          24 for K. s_i for N.  product
# Width for the capacity.   q_k for K. p_i  for N.
# variable x_ik
# help(gp.Model.addMVar)
def binPacking(n,q):

    try:

        ss = np.random.randint(1,4,n)
        s = list(ss)

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

        m.write('Bin.lp')

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

        for i in range(subscript_i):

            print('Group {0} service time is {1}'.format(i+1, s[i]))
            print('The number of people is {0}'.format(p[i]))

        for i in range(len(route)):
            print('The room {0} serves: {1}'.format(i+1, route[i][1:]))

        return m.objVal

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')

# s = [0,2,2,2,2,0]
n = 5
q = [100,150,150,100]

# p = [0,35,30,44,40,0]

binPacking(n,q)
