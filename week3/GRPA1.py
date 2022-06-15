A = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]      
B = [1009, 1001, 1005, 1004, 1008, 1002, 1003, 1006, 1007]

def DishPrepareOrder(order_list):
    D = { }
    for i in order_list:
        if i not in D.keys():
            D[i] = 1
        else:
            D[i] += 1
    L = sorted(D.items(), key=lambda kv:kv[1], reverse=True)
    ans = sorted(L, key = lambda x: (-x[1], x[0]))
    res = [ ]
    for i in ans:
        res.append(i[0])
    return res
        
    
        
        
        
            
    
    