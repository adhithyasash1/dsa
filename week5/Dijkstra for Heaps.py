def dijkstra(WMat,s):
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat)*rows+1
    (visited,distance) = ({},{})
    for v in range(rows):
        (visited[v],distance[v]) = (False,infinity)
    distance[s] = 0
    for u in range(rows):
        nextd = min([distance[v] for v in range(rows)
                     if not visited[v]])
        nextvlist = [v for v in range(rows)
                     if (not visited[v]) and
                     distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for v in range(cols):
            if WMat[nextv,v,0] == 1 and (not visited[v]):
                distance[v] = min(distance[v],distance[nextv]
                                  +WMat[nextv,v,1])
    return(distance)

