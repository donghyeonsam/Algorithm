def solution(n, computers):
    
    def find_set(x):
        
        if x == parents[x]:
            return x
    
        parents[x] = find_set(parents[x])
        return parents[x]
    
    def union(x, y):
        
        rx = find_set(x)
        ry = find_set(y)
        
        if rx == ry:
            return
        
        if rx > ry:
            parents[ry] = rx
        else:
            parents[rx] = ry
    
    answer = 0
    parents = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            if i == j:
                continue
                
            elif i != j and computers[i][j]:
                union(i, j)
    
    parents = set([find_set(i) for i in parents])
    answer = len(parents)
    
    return answer