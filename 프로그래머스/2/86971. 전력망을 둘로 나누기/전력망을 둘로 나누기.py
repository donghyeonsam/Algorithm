def solution(n, wires):
    
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
    
    answer = n
    
    for idx in range(n-1):
        
        parents = list(range(n+1))
        
        for j, (u, v) in enumerate(wires):
            if j == idx:
                continue
            union(u, v)
        
        for i in range(n):
            find_set(i)
    
        parents = parents[1:]
        a = max(parents.count(x) for x in set(parents))
        answer = min(answer, abs(n - 2 * a))
        
    return answer