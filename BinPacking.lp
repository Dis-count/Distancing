\ Model Bin
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  min
Subject To
 R0: 10 open[0,0] <= 65
 R1: 10 open[0,1] <= 51
 R2: 10 open[0,2] <= 20
 R3: 10 open[0,3] <= 50
 R4: 45 open[1,0] <= 65
 R5: 45 open[1,1] <= 51
 R6: 45 open[1,2] <= 20
 R7: 45 open[1,3] <= 50
 R8: 40 open[2,0] <= 65
 R9: 40 open[2,1] <= 51
 R10: 40 open[2,2] <= 20
 R11: 40 open[2,3] <= 50
 R12: 16 open[3,0] <= 65
 R13: 16 open[3,1] <= 51
 R14: 16 open[3,2] <= 20
 R15: 16 open[3,3] <= 50
 R16: 39 open[4,0] <= 65
 R17: 39 open[4,1] <= 51
 R18: 39 open[4,2] <= 20
 R19: 39 open[4,3] <= 50
 R20: 32 open[5,0] <= 65
 R21: 32 open[5,1] <= 51
 R22: 32 open[5,2] <= 20
 R23: 32 open[5,3] <= 50
 R24: 11 open[6,0] <= 65
 R25: 11 open[6,1] <= 51
 R26: 11 open[6,2] <= 20
 R27: 11 open[6,3] <= 50
 R28: 36 open[7,0] <= 65
 R29: 36 open[7,1] <= 51
 R30: 36 open[7,2] <= 20
 R31: 36 open[7,3] <= 50
 R32: 27 open[8,0] <= 65
 R33: 27 open[8,1] <= 51
 R34: 27 open[8,2] <= 20
 R35: 27 open[8,3] <= 50
 R36: 33 open[9,0] <= 65
 R37: 33 open[9,1] <= 51
 R38: 33 open[9,2] <= 20
 R39: 33 open[9,3] <= 50
 R40: 20 open[10,0] <= 65
 R41: 20 open[10,1] <= 51
 R42: 20 open[10,2] <= 20
 R43: 20 open[10,3] <= 50
 R44: 21 open[11,0] <= 65
 R45: 21 open[11,1] <= 51
 R46: 21 open[11,2] <= 20
 R47: 21 open[11,3] <= 50
 R48: 3 open[0,0] + open[1,0] + 3 open[2,0] + 2 open[3,0] + 2 open[4,0]
   + 2 open[5,0] + 3 open[6,0] + open[7,0] + open[8,0] + open[9,0]
   + 3 open[10,0] + 3 open[11,0] <= 24
 R49: 3 open[0,1] + open[1,1] + 3 open[2,1] + 2 open[3,1] + 2 open[4,1]
   + 2 open[5,1] + 3 open[6,1] + open[7,1] + open[8,1] + open[9,1]
   + 3 open[10,1] + 3 open[11,1] <= 24
 R50: 3 open[0,2] + open[1,2] + 3 open[2,2] + 2 open[3,2] + 2 open[4,2]
   + 2 open[5,2] + 3 open[6,2] + open[7,2] + open[8,2] + open[9,2]
   + 3 open[10,2] + 3 open[11,2] <= 24
 R51: 3 open[0,3] + open[1,3] + 3 open[2,3] + 2 open[3,3] + 2 open[4,3]
   + 2 open[5,3] + 3 open[6,3] + open[7,3] + open[8,3] + open[9,3]
   + 3 open[10,3] + 3 open[11,3] <= 24
 R52: 0.0192307692307692 open[0,0] + 0.0288461538461538 open[1,0]
   + 0.0769230769230769 open[2,0] + 0.0205128205128205 open[3,0]
   + 0.05 open[4,0] + 0.041025641025641 open[5,0]
   + 0.0211538461538462 open[6,0] + 0.0230769230769231 open[7,0]
   + 0.0173076923076923 open[8,0] + 0.0211538461538462 open[9,0]
   + 0.0384615384615385 open[10,0] + 0.0403846153846154 open[11,0] - min
   >= 0
 R53: 0.0245098039215686 open[0,1] + 0.0367647058823529 open[1,1]
   + 0.0980392156862745 open[2,1] + 0.0261437908496732 open[3,1]
   + 0.0637254901960784 open[4,1] + 0.0522875816993464 open[5,1]
   + 0.0269607843137255 open[6,1] + 0.0294117647058824 open[7,1]
   + 0.0220588235294118 open[8,1] + 0.0269607843137255 open[9,1]
   + 0.0490196078431373 open[10,1] + 0.0514705882352941 open[11,1] - min
   >= 0
 R54: 0.0625 open[0,2] + 0.09375 open[1,2] + 0.25 open[2,2]
   + 0.0666666666666667 open[3,2] + 0.1625 open[4,2]
   + 0.1333333333333333 open[5,2] + 0.06875 open[6,2] + 0.075 open[7,2]
   + 0.05625 open[8,2] + 0.06875 open[9,2] + 0.125 open[10,2]
   + 0.13125 open[11,2] - min >= 0
 R55: 0.025 open[0,3] + 0.0375 open[1,3] + 0.1 open[2,3]
   + 0.0266666666666667 open[3,3] + 0.065 open[4,3]
   + 0.0533333333333333 open[5,3] + 0.0275 open[6,3] + 0.03 open[7,3]
   + 0.0225 open[8,3] + 0.0275 open[9,3] + 0.05 open[10,3]
   + 0.0525 open[11,3] - min >= 0
 R56: open[0,0] + open[0,1] + open[0,2] + open[0,3] = 1
 R57: open[1,0] + open[1,1] + open[1,2] + open[1,3] = 1
 R58: open[2,0] + open[2,1] + open[2,2] + open[2,3] = 1
 R59: open[3,0] + open[3,1] + open[3,2] + open[3,3] = 1
 R60: open[4,0] + open[4,1] + open[4,2] + open[4,3] = 1
 R61: open[5,0] + open[5,1] + open[5,2] + open[5,3] = 1
 R62: open[6,0] + open[6,1] + open[6,2] + open[6,3] = 1
 R63: open[7,0] + open[7,1] + open[7,2] + open[7,3] = 1
 R64: open[8,0] + open[8,1] + open[8,2] + open[8,3] = 1
 R65: open[9,0] + open[9,1] + open[9,2] + open[9,3] = 1
 R66: open[10,0] + open[10,1] + open[10,2] + open[10,3] = 1
 R67: open[11,0] + open[11,1] + open[11,2] + open[11,3] = 1
Bounds
Binaries
 open[0,0] open[0,1] open[0,2] open[0,3] open[1,0] open[1,1] open[1,2]
 open[1,3] open[2,0] open[2,1] open[2,2] open[2,3] open[3,0] open[3,1]
 open[3,2] open[3,3] open[4,0] open[4,1] open[4,2] open[4,3] open[5,0]
 open[5,1] open[5,2] open[5,3] open[6,0] open[6,1] open[6,2] open[6,3]
 open[7,0] open[7,1] open[7,2] open[7,3] open[8,0] open[8,1] open[8,2]
 open[8,3] open[9,0] open[9,1] open[9,2] open[9,3] open[10,0] open[10,1]
 open[10,2] open[10,3] open[11,0] open[11,1] open[11,2] open[11,3]
End
