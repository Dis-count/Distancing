# This one is used to show the vertical bar.

import matplotlib.pyplot as plt
import numpy as np

def gantt(macInfo, flow, macStartTime,Capacity, workpiece):
    for j in range(len(macInfo)):
        i = macInfo[j]
        plt.bar(i, flow[j], Capacity[j], bottom=macStartTime[j])
        plt.text(i, macStartTime[j] + flow[j] / 8, 'G%s' % (workpiece[j]), color = "white", size = 15)

if  __name__ == "__main__":
    MS = [1, 1, 1, 2, 2, 2, 3, 3, 3]             # 对应的机器号 M1=1,M2=2,…
    T  = [3, 2, 4, 3, 3, 3, 3, 1, 3]             # 各工序加工时间
    Capacity = [0.2, 0.5, 0.6, 0.4, 1, 0.6, 0.3, 0.2, 0.4]
    macStartTime = [0, 4, 7, 0, 5, 8, 3, 8, 10]  # 各工序开始时间
    J = list(range(1,10))              # 工件号 J1=1,J2=2
    gantt(MS, T, macStartTime,Capacity, J)

    plt.vlines(1.5, 0, 15, colors = "c", linestyles = "dashed")
    plt.vlines(2.5, 0, 15, colors = "c", linestyles = "dashed")
    plt.yticks(np.arange(0, max(macStartTime) + 5, step =1 ))
    plt.xticks(np.arange(0, 4, step =1 ))
    plt.show()
