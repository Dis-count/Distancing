\ Model Bin
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  max_t
Subject To
 R0: 13 open[0,0] <= 34
 R1: 13 open[0,1] <= 43
 R2: 20 open[1,0] <= 34
 R3: 20 open[1,1] <= 43
 R4: 14 open[2,0] <= 34
 R5: 14 open[2,1] <= 43
 R6: 23 open[3,0] <= 34
 R7: 23 open[3,1] <= 43
 R8: 3 open[0,0] + open[1,0] + 2 open[2,0] + open[3,0] <= 24
 R9: 3 open[0,1] + open[1,1] + 2 open[2,1] + open[3,1] <= 24
 R10: 0.0477941176470588 open[0,0] + 0.0245098039215686 open[1,0]
   + 0.0343137254901961 open[2,0] + 0.0281862745098039 open[3,0] - max_t
   <= 0
 R11: 0.0377906976744186 open[0,1] + 0.0193798449612403 open[1,1]
   + 0.0271317829457364 open[2,1] + 0.0222868217054264 open[3,1] - max_t
   <= 0
 R12: open[0,0] + open[0,1] = 1
 R13: open[1,0] + open[1,1] = 1
 R14: open[2,0] + open[2,1] = 1
 R15: open[3,0] + open[3,1] = 1
Bounds
Binaries
 open[0,0] open[0,1] open[1,0] open[1,1] open[2,0] open[2,1] open[3,0]
 open[3,1]
End
