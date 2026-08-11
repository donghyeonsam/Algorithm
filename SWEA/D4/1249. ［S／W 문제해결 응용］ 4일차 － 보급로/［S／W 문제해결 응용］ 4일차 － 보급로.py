import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find_route():

    dist = [[-1] * N for _ in range(N)]
    pq = []
    dist[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        cur_dist, x, y = heapq.heappop(pq)

        if dist[x][y] != -1 and cur_dist > dist[x][y]:
            continue

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = cur_dist + board[nx][ny]
                if dist[nx][ny] == -1 or dist[nx][ny] > new_dist:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    return dist[N-1][N-1]

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]

    result = find_route()

    print(f'#{tc} {result}')