import heapq

def solution(board):
    
    def dijkstra():
        
        pq = []
        dists = [[[0xfffffff] * 4 for _ in range(N)] for _ in range(N)]
        for idx in range(4):
            dists[0][0][idx] = 0
            heapq.heappush(pq, (0, 0, 0, idx))
        
        while pq:
            
            cost, x, y, d = heapq.heappop(pq)
            
            if dists[x][y][d] < cost:
                continue
                
            for idx in range(4):
                
                nx, ny = x + dx[idx], y + dy[idx]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                    
                    if d % 2 == idx % 2:
                        new_cost = cost + 100
                        if dists[nx][ny][idx] <= new_cost:
                            continue
                        dists[nx][ny][idx] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny, idx))
                            
                    elif d % 2 != idx % 2:
                        new_cost = cost + 600
                        if dists[nx][ny][idx] <= new_cost:
                            continue
                        dists[nx][ny][idx] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny, idx))
                    
        return min(dists[N-1][N-1])
    
    N = len(board)
    dx = [1, 0 ,-1, 0]
    dy = [0, 1, 0, -1]
    
    answer = dijkstra()
    
    return answer