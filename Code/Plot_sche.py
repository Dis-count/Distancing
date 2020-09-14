import matplotlib.pyplot as plt
import numpy as np


def gantt(macInfo, flow, macStartTime, workpiece, operation):
    for j in range(len(macInfo)):
        i = macInfo[j] - 1
        plt.barh(i, flow[j], 0.3, left=macStartTime[j])
        plt.text(macStartTime[j] + flow[j] / 8, i, 'J%s.%s' % (workpiece[j], operation[j]), color="white", size=15)


if __name__ == "__main__":
    MS = [1, 1, 1, 2, 2, 2, 3, 3, 3]             # 对应的机器号 M1=1,M2=2,…
    T = [3, 2, 4, 3, 3, 3, 3, 5, 3]              # 各工序加工时间
    macStartTime = [0, 3, 5, 0, 5, 8, 3, 8, 13]  # 各工序开始时间
    J = [2, 1, 3, 3, 1, 2, 2, 1, 3]              # 工件号 J1=1,J2=2
    oper = [1, 1, 2, 1, 2, 3, 2, 3, 3]           # 操作序号
    gantt(MS, T, macStartTime, J, oper)
    plt.yticks(np.arange(max(MS)), np.arange(1, max(MS) + 1))
    plt.show()
