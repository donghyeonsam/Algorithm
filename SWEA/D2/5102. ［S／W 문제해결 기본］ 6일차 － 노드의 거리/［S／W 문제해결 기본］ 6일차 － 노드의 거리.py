from collections import deque
 
def BFS(s):
 
    visited = [False] * (V+1)
    q = deque()
    visited[S] = True
    q.append((S, 0))
    while q:
        cur, cnt = q.popleft()
 
        if cur == G:
            return cnt
             
        for next in graph[cur]:
            if visited[next]:
                continue
            visited[next] = True
            new_cnt = cnt + 1
            q.append((next, new_cnt))
             
    return 0
 
T = int(input())
 
for tc in range(1, T+1):
 
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V+1)]
 
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
 
    result = BFS(S)
 
    print(f'#{tc} {result}')