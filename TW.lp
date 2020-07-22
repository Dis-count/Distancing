\ Model TW_dis
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  open[0,0,0] + open[0,0,1] + open[0,1,0] + open[0,1,1] + open[0,2,0]
   + open[0,2,1] + open[0,3,0] + open[0,3,1] + open[0,4,0] + open[0,4,1]
   + open[0,5,0] + open[0,5,1] + open[1,0,0] + open[1,0,1] + open[1,1,0]
   + open[1,1,1] + open[1,2,0] + open[1,2,1] + open[1,3,0] + open[1,3,1]
   + open[1,4,0] + open[1,4,1] + open[1,5,0] + open[1,5,1] + open[2,0,0]
   + open[2,0,1] + open[2,1,0] + open[2,1,1] + open[2,2,0] + open[2,2,1]
   + open[2,3,0] + open[2,3,1] + open[2,4,0] + open[2,4,1] + open[2,5,0]
   + open[2,5,1] + open[3,0,0] + open[3,0,1] + open[3,1,0] + open[3,1,1]
   + open[3,2,0] + open[3,2,1] + open[3,3,0] + open[3,3,1] + open[3,4,0]
   + open[3,4,1] + open[3,5,0] + open[3,5,1] + open[4,0,0] + open[4,0,1]
   + open[4,1,0] + open[4,1,1] + open[4,2,0] + open[4,2,1] + open[4,3,0]
   + open[4,3,1] + open[4,4,0] + open[4,4,1] + open[4,5,0] + open[4,5,1]
   + open[5,0,0] + open[5,0,1] + open[5,1,0] + open[5,1,1] + open[5,2,0]
   + open[5,2,1] + open[5,3,0] + open[5,3,1] + open[5,4,0] + open[5,4,1]
   + open[5,5,0] + open[5,5,1]
Subject To
 R0: open[1,1,0] + open[1,1,1] + open[1,2,0] + open[1,2,1] + open[1,3,0]
   + open[1,3,1] + open[1,4,0] + open[1,4,1] + open[1,5,0] + open[1,5,1]
   = 1
 R1: open[2,1,0] + open[2,1,1] + open[2,2,0] + open[2,2,1] + open[2,3,0]
   + open[2,3,1] + open[2,4,0] + open[2,4,1] + open[2,5,0] + open[2,5,1]
   = 1
 R2: open[3,1,0] + open[3,1,1] + open[3,2,0] + open[3,2,1] + open[3,3,0]
   + open[3,3,1] + open[3,4,0] + open[3,4,1] + open[3,5,0] + open[3,5,1]
   = 1
 R3: open[4,1,0] + open[4,1,1] + open[4,2,0] + open[4,2,1] + open[4,3,0]
   + open[4,3,1] + open[4,4,0] + open[4,4,1] + open[4,5,0] + open[4,5,1]
   = 1
 R4: open[0,1,0] - open[1,0,0] - open[1,2,0] - open[1,3,0] - open[1,4,0]
   - open[1,5,0] + open[2,1,0] + open[3,1,0] + open[4,1,0] + open[5,1,0]
   = 0
 R5: open[0,1,1] - open[1,0,1] - open[1,2,1] - open[1,3,1] - open[1,4,1]
   - open[1,5,1] + open[2,1,1] + open[3,1,1] + open[4,1,1] + open[5,1,1]
   = 0
 R6: open[0,2,0] + open[1,2,0] - open[2,0,0] - open[2,1,0] - open[2,3,0]
   - open[2,4,0] - open[2,5,0] + open[3,2,0] + open[4,2,0] + open[5,2,0]
   = 0
 R7: open[0,2,1] + open[1,2,1] - open[2,0,1] - open[2,1,1] - open[2,3,1]
   - open[2,4,1] - open[2,5,1] + open[3,2,1] + open[4,2,1] + open[5,2,1]
   = 0
 R8: open[0,3,0] + open[1,3,0] + open[2,3,0] - open[3,0,0] - open[3,1,0]
   - open[3,2,0] - open[3,4,0] - open[3,5,0] + open[4,3,0] + open[5,3,0]
   = 0
 R9: open[0,3,1] + open[1,3,1] + open[2,3,1] - open[3,0,1] - open[3,1,1]
   - open[3,2,1] - open[3,4,1] - open[3,5,1] + open[4,3,1] + open[5,3,1]
   = 0
 R10: open[0,4,0] + open[1,4,0] + open[2,4,0] + open[3,4,0] - open[4,0,0]
   - open[4,1,0] - open[4,2,0] - open[4,3,0] - open[4,5,0] + open[5,4,0]
   = 0
 R11: open[0,4,1] + open[1,4,1] + open[2,4,1] + open[3,4,1] - open[4,0,1]
   - open[4,1,1] - open[4,2,1] - open[4,3,1] - open[4,5,1] + open[5,4,1]
   = 0
 R12: open[0,1,0] + open[0,2,0] + open[0,3,0] + open[0,4,0] + open[0,5,0]
   = 1
 R13: open[0,1,1] + open[0,2,1] + open[0,3,1] + open[0,4,1] + open[0,5,1]
   = 1
 R14: open[0,5,0] + open[1,5,0] + open[2,5,0] + open[3,5,0] + open[4,5,0]
   = 1
 R15: open[0,5,1] + open[1,5,1] + open[2,5,1] + open[3,5,1] + open[4,5,1]
   = 1
 R16: 10000 open[0,0,0] + interval[0] <= 10000
 R17: 10000 open[0,1,0] + start[0,0] - start[1,0] + interval[0] <= 10000
 R18: 10000 open[0,2,0] + start[0,0] - start[2,0] + interval[0] <= 10000
 R19: 10000 open[0,3,0] + start[0,0] - start[3,0] + interval[0] <= 10000
 R20: 10000 open[0,4,0] + start[0,0] - start[4,0] + interval[0] <= 10000
 R21: 10000 open[0,5,0] + start[0,0] - start[5,0] + interval[0] <= 10000
 R22: 10000 open[1,0,0] - start[0,0] + start[1,0] + interval[1] <= 9998
 R23: 10000 open[1,1,0] + interval[1] <= 9998
 R24: 10000 open[1,2,0] + start[1,0] - start[2,0] + interval[1] <= 9998
 R25: 10000 open[1,3,0] + start[1,0] - start[3,0] + interval[1] <= 9998
 R26: 10000 open[1,4,0] + start[1,0] - start[4,0] + interval[1] <= 9998
 R27: 10000 open[1,5,0] + start[1,0] - start[5,0] + interval[1] <= 9998
 R28: 10000 open[2,0,0] - start[0,0] + start[2,0] + interval[2] <= 9998
 R29: 10000 open[2,1,0] - start[1,0] + start[2,0] + interval[2] <= 9998
 R30: 10000 open[2,2,0] + interval[2] <= 9998
 R31: 10000 open[2,3,0] + start[2,0] - start[3,0] + interval[2] <= 9998
 R32: 10000 open[2,4,0] + start[2,0] - start[4,0] + interval[2] <= 9998
 R33: 10000 open[2,5,0] + start[2,0] - start[5,0] + interval[2] <= 9998
 R34: 10000 open[3,0,0] - start[0,0] + start[3,0] + interval[3] <= 9998
 R35: 10000 open[3,1,0] - start[1,0] + start[3,0] + interval[3] <= 9998
 R36: 10000 open[3,2,0] - start[2,0] + start[3,0] + interval[3] <= 9998
 R37: 10000 open[3,3,0] + interval[3] <= 9998
 R38: 10000 open[3,4,0] + start[3,0] - start[4,0] + interval[3] <= 9998
 R39: 10000 open[3,5,0] + start[3,0] - start[5,0] + interval[3] <= 9998
 R40: 10000 open[4,0,0] - start[0,0] + start[4,0] + interval[4] <= 9998
 R41: 10000 open[4,1,0] - start[1,0] + start[4,0] + interval[4] <= 9998
 R42: 10000 open[4,2,0] - start[2,0] + start[4,0] + interval[4] <= 9998
 R43: 10000 open[4,3,0] - start[3,0] + start[4,0] + interval[4] <= 9998
 R44: 10000 open[4,4,0] + interval[4] <= 9998
 R45: 10000 open[4,5,0] + start[4,0] - start[5,0] + interval[4] <= 9998
 R46: 10000 open[5,0,0] - start[0,0] + start[5,0] + interval[5] <= 10000
 R47: 10000 open[5,1,0] - start[1,0] + start[5,0] + interval[5] <= 10000
 R48: 10000 open[5,2,0] - start[2,0] + start[5,0] + interval[5] <= 10000
 R49: 10000 open[5,3,0] - start[3,0] + start[5,0] + interval[5] <= 10000
 R50: 10000 open[5,4,0] - start[4,0] + start[5,0] + interval[5] <= 10000
 R51: 10000 open[5,5,0] + interval[5] <= 10000
 R52: 10000 open[0,0,1] + interval[0] <= 10000
 R53: 10000 open[0,1,1] + start[0,1] - start[1,1] + interval[0] <= 10000
 R54: 10000 open[0,2,1] + start[0,1] - start[2,1] + interval[0] <= 10000
 R55: 10000 open[0,3,1] + start[0,1] - start[3,1] + interval[0] <= 10000
 R56: 10000 open[0,4,1] + start[0,1] - start[4,1] + interval[0] <= 10000
 R57: 10000 open[0,5,1] + start[0,1] - start[5,1] + interval[0] <= 10000
 R58: 10000 open[1,0,1] - start[0,1] + start[1,1] + interval[1] <= 9998
 R59: 10000 open[1,1,1] + interval[1] <= 9998
 R60: 10000 open[1,2,1] + start[1,1] - start[2,1] + interval[1] <= 9998
 R61: 10000 open[1,3,1] + start[1,1] - start[3,1] + interval[1] <= 9998
 R62: 10000 open[1,4,1] + start[1,1] - start[4,1] + interval[1] <= 9998
 R63: 10000 open[1,5,1] + start[1,1] - start[5,1] + interval[1] <= 9998
 R64: 10000 open[2,0,1] - start[0,1] + start[2,1] + interval[2] <= 9998
 R65: 10000 open[2,1,1] - start[1,1] + start[2,1] + interval[2] <= 9998
 R66: 10000 open[2,2,1] + interval[2] <= 9998
 R67: 10000 open[2,3,1] + start[2,1] - start[3,1] + interval[2] <= 9998
 R68: 10000 open[2,4,1] + start[2,1] - start[4,1] + interval[2] <= 9998
 R69: 10000 open[2,5,1] + start[2,1] - start[5,1] + interval[2] <= 9998
 R70: 10000 open[3,0,1] - start[0,1] + start[3,1] + interval[3] <= 9998
 R71: 10000 open[3,1,1] - start[1,1] + start[3,1] + interval[3] <= 9998
 R72: 10000 open[3,2,1] - start[2,1] + start[3,1] + interval[3] <= 9998
 R73: 10000 open[3,3,1] + interval[3] <= 9998
 R74: 10000 open[3,4,1] + start[3,1] - start[4,1] + interval[3] <= 9998
 R75: 10000 open[3,5,1] + start[3,1] - start[5,1] + interval[3] <= 9998
 R76: 10000 open[4,0,1] - start[0,1] + start[4,1] + interval[4] <= 9998
 R77: 10000 open[4,1,1] - start[1,1] + start[4,1] + interval[4] <= 9998
 R78: 10000 open[4,2,1] - start[2,1] + start[4,1] + interval[4] <= 9998
 R79: 10000 open[4,3,1] - start[3,1] + start[4,1] + interval[4] <= 9998
 R80: 10000 open[4,4,1] + interval[4] <= 9998
 R81: 10000 open[4,5,1] + start[4,1] - start[5,1] + interval[4] <= 9998
 R82: 10000 open[5,0,1] - start[0,1] + start[5,1] + interval[5] <= 10000
 R83: 10000 open[5,1,1] - start[1,1] + start[5,1] + interval[5] <= 10000
 R84: 10000 open[5,2,1] - start[2,1] + start[5,1] + interval[5] <= 10000
 R85: 10000 open[5,3,1] - start[3,1] + start[5,1] + interval[5] <= 10000
 R86: 10000 open[5,4,1] - start[4,1] + start[5,1] + interval[5] <= 10000
 R87: 10000 open[5,5,1] + interval[5] <= 10000
 R88: 8 open[1,1,0] + 8 open[1,2,0] + 8 open[1,3,0] + 8 open[1,4,0]
   + 8 open[1,5,0] - start[1,0] <= 0
 R89: 14 open[2,1,0] + 14 open[2,2,0] + 14 open[2,3,0] + 14 open[2,4,0]
   + 14 open[2,5,0] - start[2,0] <= 0
 R90: 10 open[3,1,0] + 10 open[3,2,0] + 10 open[3,3,0] + 10 open[3,4,0]
   + 10 open[3,5,0] - start[3,0] <= 0
 R91: 19 open[4,1,0] + 19 open[4,2,0] + 19 open[4,3,0] + 19 open[4,4,0]
   + 19 open[4,5,0] - start[4,0] <= 0
 R92: 8 open[1,1,1] + 8 open[1,2,1] + 8 open[1,3,1] + 8 open[1,4,1]
   + 8 open[1,5,1] - start[1,1] <= 0
 R93: 14 open[2,1,1] + 14 open[2,2,1] + 14 open[2,3,1] + 14 open[2,4,1]
   + 14 open[2,5,1] - start[2,1] <= 0
 R94: 10 open[3,1,1] + 10 open[3,2,1] + 10 open[3,3,1] + 10 open[3,4,1]
   + 10 open[3,5,1] - start[3,1] <= 0
 R95: 19 open[4,1,1] + 19 open[4,2,1] + 19 open[4,3,1] + 19 open[4,4,1]
   + 19 open[4,5,1] - start[4,1] <= 0
 R96: 11 open[1,1,0] + 11 open[1,2,0] + 11 open[1,3,0] + 11 open[1,4,0]
   + 11 open[1,5,0] - start[1,0] >= 0
 R97: 15 open[2,1,0] + 15 open[2,2,0] + 15 open[2,3,0] + 15 open[2,4,0]
   + 15 open[2,5,0] - start[2,0] >= 0
 R98: 16 open[3,1,0] + 16 open[3,2,0] + 16 open[3,3,0] + 16 open[3,4,0]
   + 16 open[3,5,0] - start[3,0] >= 0
 R99: 21 open[4,1,0] + 21 open[4,2,0] + 21 open[4,3,0] + 21 open[4,4,0]
   + 21 open[4,5,0] - start[4,0] >= 0
 R100: 11 open[1,1,1] + 11 open[1,2,1] + 11 open[1,3,1] + 11 open[1,4,1]
   + 11 open[1,5,1] - start[1,1] >= 0
 R101: 15 open[2,1,1] + 15 open[2,2,1] + 15 open[2,3,1] + 15 open[2,4,1]
   + 15 open[2,5,1] - start[2,1] >= 0
 R102: 16 open[3,1,1] + 16 open[3,2,1] + 16 open[3,3,1] + 16 open[3,4,1]
   + 16 open[3,5,1] - start[3,1] >= 0
 R103: 21 open[4,1,1] + 21 open[4,2,1] + 21 open[4,3,1] + 21 open[4,4,1]
   + 21 open[4,5,1] - start[4,1] >= 0
 R104: start[0,0] = 0
 R105: start[0,1] = 0
 R106: start[5,0] = 24
 R107: start[5,1] = 24
 R108: open[1,1,0] + open[1,2,0] + open[1,3,0] + open[1,4,0] + open[1,5,0]
   - 2 interval[1] <= 0
 R109: open[2,1,0] + open[2,2,0] + open[2,3,0] + open[2,4,0] + open[2,5,0]
   - 2 interval[2] <= 0
 R110: open[3,1,0] + open[3,2,0] + open[3,3,0] + open[3,4,0] + open[3,5,0]
   - 2 interval[3] <= 0
 R111: open[4,1,0] + open[4,2,0] + open[4,3,0] + open[4,4,0] + open[4,5,0]
   - 2 interval[4] <= 0
 R112: open[1,1,1] + open[1,2,1] + open[1,3,1] + open[1,4,1] + open[1,5,1]
   - 2 interval[1] <= 0
 R113: open[2,1,1] + open[2,2,1] + open[2,3,1] + open[2,4,1] + open[2,5,1]
   - 2 interval[2] <= 0
 R114: open[3,1,1] + open[3,2,1] + open[3,3,1] + open[3,4,1] + open[3,5,1]
   - 2 interval[3] <= 0
 R115: open[4,1,1] + open[4,2,1] + open[4,3,1] + open[4,4,1] + open[4,5,1]
   - 2 interval[4] <= 0
 R116: 35 open[1,1,0] + 35 open[1,2,0] + 35 open[1,3,0] + 35 open[1,4,0]
   + 35 open[1,5,0] <= 30
 R117: 35 open[1,1,1] + 35 open[1,2,1] + 35 open[1,3,1] + 35 open[1,4,1]
   + 35 open[1,5,1] <= 60
 R118: 20 open[2,1,0] + 20 open[2,2,0] + 20 open[2,3,0] + 20 open[2,4,0]
   + 20 open[2,5,0] <= 30
 R119: 20 open[2,1,1] + 20 open[2,2,1] + 20 open[2,3,1] + 20 open[2,4,1]
   + 20 open[2,5,1] <= 60
 R120: 44 open[3,1,0] + 44 open[3,2,0] + 44 open[3,3,0] + 44 open[3,4,0]
   + 44 open[3,5,0] <= 30
 R121: 44 open[3,1,1] + 44 open[3,2,1] + 44 open[3,3,1] + 44 open[3,4,1]
   + 44 open[3,5,1] <= 60
 R122: 10 open[4,1,0] + 10 open[4,2,0] + 10 open[4,3,0] + 10 open[4,4,0]
   + 10 open[4,5,0] <= 30
 R123: 10 open[4,1,1] + 10 open[4,2,1] + 10 open[4,3,1] + 10 open[4,4,1]
   + 10 open[4,5,1] <= 60
 R124: open[0,0,0] = 0
 R125: open[0,0,1] = 0
 R126: open[1,1,0] = 0
 R127: open[1,1,1] = 0
 R128: open[2,2,0] = 0
 R129: open[2,2,1] = 0
 R130: open[3,3,0] = 0
 R131: open[3,3,1] = 0
 R132: open[4,4,0] = 0
 R133: open[4,4,1] = 0
 R134: open[5,5,0] = 0
 R135: open[5,5,1] = 0
Bounds
Binaries
 open[0,0,0] open[0,0,1] open[0,1,0] open[0,1,1] open[0,2,0] open[0,2,1]
 open[0,3,0] open[0,3,1] open[0,4,0] open[0,4,1] open[0,5,0] open[0,5,1]
 open[1,0,0] open[1,0,1] open[1,1,0] open[1,1,1] open[1,2,0] open[1,2,1]
 open[1,3,0] open[1,3,1] open[1,4,0] open[1,4,1] open[1,5,0] open[1,5,1]
 open[2,0,0] open[2,0,1] open[2,1,0] open[2,1,1] open[2,2,0] open[2,2,1]
 open[2,3,0] open[2,3,1] open[2,4,0] open[2,4,1] open[2,5,0] open[2,5,1]
 open[3,0,0] open[3,0,1] open[3,1,0] open[3,1,1] open[3,2,0] open[3,2,1]
 open[3,3,0] open[3,3,1] open[3,4,0] open[3,4,1] open[3,5,0] open[3,5,1]
 open[4,0,0] open[4,0,1] open[4,1,0] open[4,1,1] open[4,2,0] open[4,2,1]
 open[4,3,0] open[4,3,1] open[4,4,0] open[4,4,1] open[4,5,0] open[4,5,1]
 open[5,0,0] open[5,0,1] open[5,1,0] open[5,1,1] open[5,2,0] open[5,2,1]
 open[5,3,0] open[5,3,1] open[5,4,0] open[5,4,1] open[5,5,0] open[5,5,1]
End
