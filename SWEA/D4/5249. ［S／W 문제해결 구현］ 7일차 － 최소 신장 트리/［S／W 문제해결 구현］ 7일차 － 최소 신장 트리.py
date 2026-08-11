import heapq
 
def prim(s):
 
    min_weight = 0
    MST = [False] * (V+1)
    pq = []
    heapq.heappush(pq, (0, s))
 
    while pq:
        w, u = heapq.heappop(pq)
 
        if MST[u]:
            continue
 
        MST[u] = True
        min_weight += w
 
        for next_w, next_u in graph[u]:
            if MST[next_u]:
                continue
            heapq.heappush(pq, (next_w, next_u))
 
    return min_weight
 
T = int(input())
 
for tc in range(1, T+1):
 
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] * (V+1) for _ in range(V+1)]
 
    for start, end, weight in edges:
        graph[start].append((weight, end))
        graph[end].append((weight, start))
 
    result = prim(0)
 
    print(f'#{tc} {result}')