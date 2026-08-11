from collections import deque

def R_BFS(num):

    global result
    used = [False] * (N + 1)
    q = deque()
    q.append(num)
    while q:
        tmp = q.popleft()
        for idx in range(len(reverse_graph[tmp])):
            next = reverse_graph[tmp][idx]
            if not used[next]:
                used[next] = True
                q.append(next)

    cnt = 0
    for k in range(1, N + 1):
        if used[k]:
            cnt += 1

    return cnt

def BFS(num):

    global result
    used = [False] * (N+1)
    q = deque()
    q.append(num)
    while q:
        tmp = q.popleft()
        for idx in range(len(graph[tmp])):
            next = graph[tmp][idx]
            if not used[next]:
                used[next] = True
                q.append(next)

    cnt = 0
    for k in range(1, N+1):
        if used[k]:
            cnt += 1

    return cnt

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    reverse_graph = [[] for _ in range(N+1)]
    result= 0

    for k in range(M):
        graph[arr[k][0]].append(arr[k][1])
        reverse_graph[arr[k][1]].append(arr[k][0])

    for num in range(1, N+1):
        if BFS(num) + R_BFS(num) == N-1:
            result += 1

    print(f'#{tc} {result}')


