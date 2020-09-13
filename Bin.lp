\ Model Bin
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  min
Subject To
 R0: 19 open[0,0] <= 100
 R1: 19 open[0,1] <= 150
 R2: 19 open[0,2] <= 150
 R3: 19 open[0,3] <= 100
 R4: 19 open[1,0] <= 100
 R5: 19 open[1,1] <= 150
 R6: 19 open[1,2] <= 150
 R7: 19 open[1,3] <= 100
 R8: 34 open[2,0] <= 100
 R9: 34 open[2,1] <= 150
 R10: 34 open[2,2] <= 150
 R11: 34 open[2,3] <= 100
 R12: 34 open[3,0] <= 100
 R13: 34 open[3,1] <= 150
 R14: 34 open[3,2] <= 150
 R15: 34 open[3,3] <= 100
 R16: 52 open[4,0] <= 100
 R17: 52 open[4,1] <= 150
 R18: 52 open[4,2] <= 150
 R19: 52 open[4,3] <= 100
 R20: 3.5 open[0,0] + 1.5 open[1,0] + 2.5 open[2,0] + 3.5 open[3,0]
   + 3.5 open[4,0] <= 122.5
 R21: 3.5 open[0,1] + 1.5 open[1,1] + 2.5 open[2,1] + 3.5 open[3,1]
   + 3.5 open[4,1] <= 122.5
 R22: 3.5 open[0,2] + 1.5 open[1,2] + 2.5 open[2,2] + 3.5 open[3,2]
   + 3.5 open[4,2] <= 122.5
 R23: 3.5 open[0,3] + 1.5 open[1,3] + 2.5 open[2,3] + 3.5 open[3,3]
   + 3.5 open[4,3] <= 122.5
 R24: 0.02375 open[0,0] + 0.00791666666666667 open[1,0]
   + 0.0283333333333333 open[2,0] + 0.0425 open[3,0] + 0.065 open[4,0]
   - min >= 0
 R25: 0.0158333333333333 open[0,1] + 0.00527777777777778 open[1,1]
   + 0.0188888888888889 open[2,1] + 0.0283333333333333 open[3,1]
   + 0.0433333333333333 open[4,1] - min >= 0
 R26: 0.0158333333333333 open[0,2] + 0.00527777777777778 open[1,2]
   + 0.0188888888888889 open[2,2] + 0.0283333333333333 open[3,2]
   + 0.0433333333333333 open[4,2] - min >= 0
 R27: 0.02375 open[0,3] + 0.00791666666666667 open[1,3]
   + 0.0283333333333333 open[2,3] + 0.0425 open[3,3] + 0.065 open[4,3]
   - min >= 0
 R28: open[0,0] + open[0,1] + open[0,2] + open[0,3] = 1
 R29: open[1,0] + open[1,1] + open[1,2] + open[1,3] = 1
 R30: open[2,0] + open[2,1] + open[2,2] + open[2,3] = 1
 R31: open[3,0] + open[3,1] + open[3,2] + open[3,3] = 1
 R32: open[4,0] + open[4,1] + open[4,2] + open[4,3] = 1
Bounds
Binaries
 open[0,0] open[0,1] open[0,2] open[0,3] open[1,0] open[1,1] open[1,2]
 open[1,3] open[2,0] open[2,1] open[2,2] open[2,3] open[3,0] open[3,1]
 open[3,2] open[3,3] open[4,0] open[4,1] open[4,2] open[4,3]
End
