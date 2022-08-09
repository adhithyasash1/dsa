lines = int(input())
curvature = float(input())
i, ans = 0, [ ]
mid = lines // 2
eqn = (curvature*(i-mid)**2 + mid)
    
for i in range(lines):
    if curvature > 0:
      eqn = (curvature)*(i-mid)**2 + mid
      ans.append(eqn) 
    elif curvature < 0:
      eqn = (curvature)*(-i+mid)**2 + mid
      ans.append(eqn) 

if curvature > 0:
  val = ans[len(ans)//2]
  new_list = [x-val for x in ans]

elif curvature < 0:
  val = ans[0]
  new_list = [x-val for x in ans] 

for i in range(len(ans)):
    curr = int(new_list[i])
    print(' '*curr + '*')

    
    
