'''
Closest pair of points

1) Several objects on screen 

2) Basic step: find closest pair of objects 

3) n objects — naive algorithm is n^2
	
	-> For each pair of objects, compute their distance 
	-> Report minimum distance across all pairs 

4) There is a clever algorithm that takes time O(nlogn) using divide and conquer

5) Given n points (p1, p2, p3,..., pn)  find the closest pair 

	-> Assume no two points have same  or  coordinate
	-> Split the points into two halves by vertical line 
	-> Recursively compute closest pair in each half 
	-> Compare shortest distance in each half to shortest distance across the dividing line 

6) Recurrence: 2T(n/2) + n

7) Overall: O(nlogn)
'''

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



pts =  [(2, 15), (40, 5), (20, 1), (21, 14), (1,4), (3, 11)]
mul = 0
if (len(pts) > 100): mul = 0
result = minDistance(pts)
for i in range(mul):
  minDistance(pts)
print(result)



