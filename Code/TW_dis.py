import numpy as np
import gurobipy as gp
from gurobipy import GRB
import scipy.sparse as sp

# q_k capacity.
# s_i service time for each group.
# p_i demand number of people.
# variable x_ijk  w_ik t_i
def TW(s,q,p):

    try:

        subscript_i = len(s)
        subscript_j = len(s)
        subscript_k = len(q)

        m = gp.Model("TW_dis")

        x = m.addMVar((subscript_i, subscript_j, subscript_k), vtype=GRB.BINARY, name="open")
        w = m.addMVar((subscript_i,subscript_k), lb=0, name="start")
        t = m.addMVar(subscript_i, lb=0, name="start")

        # Set objective
        m.setObjective(x.sum(), GRB.MINIMIZE)

        # Add constraints
        # constraint 1

        for i in range(subscript_i):

            m.addConstr(x[i, :] == 1, name="serve"+str(i))

        # constraint 2

        for i in range(row1):

            m.addConstr(x0*lambda0[i] @ x[i,:]- x0*lambda0[i] @ y[i,:] == (lambda0[i]*b[i] - lambda0[i]* x0 @ xx[i,:]) , name="equal"+str(i))

        # constraint 3
        # constraint 4
        # constraint 5
        # constraint 6
        # constraint 7
        # constraint 8
        # constraint 9

        m.write('TW.lp')

        m.params.outputflag = 0
        m.optimize()

        return m.objVal

    except gp.GurobiError as e:
        print('Main-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Main-Encountered an attribute error')



A = [[-1,1],[6,4],[1,4]]
C = [5,4]
b = [1,24,9]
x0 =[2,3]

def sub(A,C,b):

    try:
        m = gp.Model("sub")

        xx = np.array(A)
        row = xx.shape[0]
        col = xx.shape[1]

        x = m.addMVar(shape=row, lb=0, name="x")
        A = xx.T
        A = sp.csr_matrix(A)
        # Set objective

        obj = np.array(b)
        m.setObjective(obj @ x, GRB.MINIMIZE)

        rhs = np.array(C)
        # Add constraints

        m.addConstr(A @ x >= rhs, name="c")
        m.write('sub.lp')
        # Optimize model
        m.optimize()

        print('The sub-object: %g' % m.objVal)

        return x.X,m

    except gp.GurobiError as e:
        print('Sub-Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError:
        print('Sub-Encountered an attribute error')

lambda0,m = sub(A,C,b)

rmain(A,C,b,x0,lambda0)
