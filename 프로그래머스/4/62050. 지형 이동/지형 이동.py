import heapq

def solution(land, height):
    
    answer = 0
    n = len(land)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def prim(start_x, start_y):
        
        min_weight = 0
        pq = [(0, start_x, start_y)]
        MST = [[0] * n for _ in range(n)]
    
        while pq:
            weight, x, y = heapq.heappop(pq)
            
            if MST[x][y]:
                continue
            
            MST[x][y] = 1
            min_weight += weight
            
            for idx in range(4):
                
                next_x, next_y = x + dx[idx], y + dy[idx]
                
                if 0 <= next_x < n and 0 <= next_y < n:
                    
                    next_weight = abs(land[x][y] - land[next_x][next_y])
                    if next_weight <= height:
                        next_weight = 0
                
                    heapq.heappush(pq, (next_weight, next_x, next_y))
                    
        return min_weight
                                      
    answer = prim(0, 0)
    
    return answer