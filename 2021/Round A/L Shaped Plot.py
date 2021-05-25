# Google Kick Start : Problem 2
# L Shape Plot

import numpy as np
def count(x, y):
  return max((min(x//2, y)+min(x,y//2)-2),0)

def solve():
  R, C = map(int, input().split())
  G = []
  for _ in range(R):
    G.append(list(map(int, input().split())))
  G = np.array(G)
  dim = G.shape
  l = np.zeros(dim)
  t = np.zeros(dim)
  r = np.zeros(dim)
  b = np.zeros(dim)

  for i in range(dim[0]):
    lt = 0
    rt = 0
    for j in range(dim[1]):
      if G[i][j] == 0:
        l[i][j] = 0
        lt = 0
      else:
        lt += 1
        l[i][j] = lt

      if G[i][C-1-j] == 0:
        r[i][C-1-j] = 0
        rt = 0
      else:
        rt += 1
        r[i][C-1-j] = rt
      
  for j in range(dim[1]):
    tt = 0
    bt = 0
    for i in range(dim[0]):
      if G[i][j] == 0:
        t[i][j] = 0
        tt = 0
      else:
        tt += 1
        t[i][j] = tt

      if G[R-1-i][j] == 0:
        b[R-1-i][j] = 0
        bt = 0
      else:
        bt += 1
        b[R-1-i][j] = bt
  tl = 0
  tr = 0
  bl = 0
  br = 0
  for i in range(dim[0]):
    for j in range(dim[1]):
      tl += count(l[i][j],t[i][j])
      tr += count(r[i][j],t[i][j])
      bl += count(l[i][j],b[i][j])
      br += count(r[i][j],b[i][j])

  return tl+tr+bl+br
  
for i in range(int(input())):
  print("Case #{}: {}".format(i+1, solve()))
