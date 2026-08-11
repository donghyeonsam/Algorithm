import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def Dijkstra():

    pq = []
    heapq.heappush(pq, (0, 0, 0))
    cost_map[0][0] = 0
    while pq:
        cur_cost, x, y = heapq.heappop(pq)

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if 0 <= nx < N and 0 <= ny < N:

                if board[x][y] < board[nx][ny]:
                    new_cost = cur_cost + 1 + abs(board[x][y] - board[nx][ny])
                else:
                    new_cost = cur_cost + 1

                if cost_map[nx][ny] == -1:
                    cost_map[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
                elif cost_map[nx][ny] > new_cost:
                    cost_map[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cost_map = [[-1] * N for _ in range(N)]

    Dijkstra()

    result = cost_map[N-1][N-1]
    print(f'#{tc} {result}')