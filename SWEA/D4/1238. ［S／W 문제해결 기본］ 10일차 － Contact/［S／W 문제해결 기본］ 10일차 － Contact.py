from collections import deque

def BFS(s):

    used = [False] * 101
    q = deque()
    used[s] = True
    q.append((s, 0))
    max_degree = 0
    result = 0

    while q:

        tmp, degree = q.popleft()

        if max_degree < degree:
            max_degree = degree
            result = tmp
        elif max_degree <= degree and result < tmp:
            result = tmp

        for k in range(len(graph[tmp])):
            next = graph[tmp][k]
            if not used[next]:
                used[next] = True
                q.append((next, degree+1))

    return result

T = 10

for tc in range(1, T+1):

    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]

    for idx in range(0, N, 2):
        num = arr[idx]
        graph[num].append(arr[idx+1])

    print(f'#{tc} {BFS(S)}')