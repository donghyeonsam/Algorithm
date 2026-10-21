def solution(n, costs):

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
    cnt = 0
    parents = [i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])
    
    for u, v, w in costs:
        
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            answer += w
            
            if cnt == n-1:
                break
            
    return answer
