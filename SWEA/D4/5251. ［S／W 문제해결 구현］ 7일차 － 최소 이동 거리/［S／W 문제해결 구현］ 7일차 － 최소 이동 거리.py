import heapq

def Dijkstra():

    global cost_map

    pq = []
    for idx in range(len(graph[0])):
        heapq.heappush(pq, (graph[0][idx][1], graph[0][idx][0]))
    cost_map[0] = 0
    while pq:
        cur_cost, cur_idx = heapq.heappop(pq)

        for k in range(len(graph[cur_idx])):
            next_idx = graph[cur_idx][k][0]
            new_cost = cur_cost + graph[cur_idx][k][1]
            if cost_map[next_idx] == -1 or cost_map[next_idx] > new_cost:
                cost_map[next_idx] = new_cost
                heapq.heappush(pq, (new_cost, next_idx))

T = int(input())

for tc in range(1, T+1):

    N, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] for _ in range(N+1)]
    cost_map = [-1] * (N+1)

    for idx in range(E):
        graph[lst[idx][0]].append((lst[idx][1], lst[idx][2]))

    Dijkstra()

    result = cost_map[N]

    print(f'#{tc} {result}')