'''
Consider a set of n points given in the form of list of tuples, where each tuple represents a point in a 2D space with first element of tuple as x-coordinate and second element as y-coordinate. 

Write a function minDistance(Points) that returns the distance between closest pair of points (pi, pj) in the set of points Points. 

--> n >= 2
--> No two points have same x co-ordinate.
--> No two points have same x co-ordinate.
--> Solution should run in O(nlogn) time.
'''

# Solution 

import math

# Returns eucledian disatnce between points p and q
def distance(p, q):
  return math.sqrt(math.pow(p[0] - q[0],2) + math.pow(p[1] - q[1],2))

def minDistanceRec(Px, Py):
  s = len(Px)
  # Given number of points cannot be less than 2.
  # If only 2 or 3 points are left return the minimum distance accordingly.
  if (s == 2):
    return distance(Px[0],Px[1])
  elif (s == 3):
    return min(distance(Px[0],Px[1]), distance(Px[1],Px[2]), distance(Px[2],Px[0]))

  # For more than 3 points divide the poitns by point around median of x coordinates
  m = s//2
  Qx = Px[:m]
  Rx = Px[m:]
  xR = Rx[0][0]    # minimum x value in Rx
  
  # Construct Qy and Ry in O(n) rather from Py
  Qy=[]
  Ry=[]
  for p in Py:
    if(p[0] < xR):
      Qy.append(p)
    else:
      Ry.append(p)

  # Extract Sy using delta
  delta = min(minDistanceRec(Qx, Qy), minDistanceRec(Rx, Ry))
  Sy = []
  for p in Py:
    if abs(p[0]-xR) <= delta:
      Sy.append(p)
    
  #print(xR,delta,Sy)
  sizeS = len(Sy)
  if sizeS > 1:
      minS = distance(Sy[0], Sy[1])
      for i in range(1, sizeS-1):
          for j in range(i, min(i+15, sizeS)-1):
              minS = min(minS, distance(Sy[i], Sy[j+1]))
      return min(delta, minS)
  else:
      return delta

def minDistance(Points):
  Px = sorted(Points)
  Py = Points
  Py.sort(key=lambda x: x[-1])
  #print(Px,Py)
  return round(minDistanceRec(Px, Py), 2)


'''
Input
	[(46, 67), (52, 49), (7, 1), (10, 35), (31, 19), (57, 3), (64, 23), (75, 71), (29, 34), (39, 61), (26, 30), (16, 11), (61, 43), (51, 0), (60, 20), (1, 60), (34, 28), (8, 68)]
Output
	5.0

Input
	[(2, 15), (40, 5), (20, 1), (21, 14), (1,4), (3, 11)]
Output
	4.12
'''

# Solution 2

import math, sys
import numpy as np
def distance(a,b):
    return np.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2))

def closest_pair(Px,Py):

    if len(Px) < 4:
        return closest_pair_burteforce(Px)

    Q = Px[:len(Px)//2]
    R = Px[len(Px)//2:]

    Qx = sorted(Q,key = lambda p: p[0])
    Qy = sorted(Q,key = lambda p: p[1])
    Rx = sorted(R,key = lambda p: p[0])
    Ry = sorted(R,key = lambda p: p[1])


    dl, p1, q1 = closest_pair(Qx,Qy)
    dr, p2, q2 = closest_pair(Rx,Ry)


    d = min(dl,dr)
    dc, p3, q3 = closest_split_pair(Px,Py,d)

    mind = min(dl,dr,dc)
    if mind == dl:
      return dl, p1, q1
    elif mind == dr:
      return dr, p2, q2
    else:
      return dc, p3, q3


def closest_pair_burteforce(Px):
    mind = float("inf")
    cpairs = None
    for i in range(len(Px)):
        for j in range(i+1,len(Px)):
            dis = distance(Px[i],Px[j])
            if dis < mind:
                mind = dis
                cpairs = (Px[i],Px[j])
    return (mind,cpairs[0],cpairs[1])


def closest_split_pair(Px,Py,d):
    xbar = Px[len(Px)//2][0]
    Sy = []
    for point in Py:
        if xbar - d <= point[0] <= xbar + d:
            Sy.append(point)

    best = d
    best_pair = (Px[0][0], Px[0][1])


    for i in range(len(Sy)):
        for j in range(1,min(8,len(Sy)-i)):
            if distance(Sy[i],Sy[i+j]) < best:
                best = distance(Sy[i],Sy[i+j])
                best_pair = (Sy[i], Sy[i+j])



    return best, best_pair[0], best_pair[1]



def minDistance(Points):
    Px = sorted(Points,key = lambda p: p[0])
    Py = sorted(Points,key = lambda p: p[1])
    d, p, q = closest_pair(Px,Py)
    return round(d,2)
