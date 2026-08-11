import heapq
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
def find_route():
 
    pq = []
    dist = [[-1] * N for _ in range(N)]
    heapq.heappush(pq, (0, 0, 0))
    dist[0][0] = 0
    while pq:
        cost, x, y = heapq.heappop(pq)
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + road[nx][ny]
                if dist[nx][ny] == -1 or dist[nx][ny] > new_cost:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
 
    return dist[N-1][N-1]
 
 
T = int(input())
 
for tc in range(1, T+1):
 
    N = int(input())
    road = [list(map(int, input().strip())) for _ in range(N)]
 
    print(f'#{tc} {find_route()}')