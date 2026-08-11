T = int(input())

def DFS(S):

    visited[S] = 1

    for w in nb_list[S]:
        if visited[w] == 0:
            DFS(w)

for tc in range(1, T+1):

    n, m = map(int, input().split())
    nb_list = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in range(m):
        s, e = list(map(int, input().split()))
        nb_list[s].append(e)

    S, O = list(map(int, input().split()))
    DFS(S)
    result = 0

    if visited[O] == 1:
        result = 1

    print(f'#{tc} {result}')