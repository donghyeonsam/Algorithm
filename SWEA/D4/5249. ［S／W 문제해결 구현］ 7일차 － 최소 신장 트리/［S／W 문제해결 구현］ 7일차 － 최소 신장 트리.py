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
 
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry
 
T = int(input())
 
for tc in range(1, T+1):
 
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    cnt = 0
    result = 0
 
    parents = [i for i in range(V+1)]
 
    edges.sort(key=lambda x: x[2])
 
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += w
 
            if cnt == V:
                break
 
    print(f'#{tc} {result}')