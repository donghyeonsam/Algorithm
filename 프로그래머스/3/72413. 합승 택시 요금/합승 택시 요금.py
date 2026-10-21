import heapq

def solution(n, s, a, b, fares):
    
    def dijkstra_s(goal):
        
        pq = [(0, s)]
        dists = [0xffffffff] * (n+1)
        dists[s] = 0
        
        while pq:
            
            cost, node = heapq.heappop(pq)
            
            if dists[node] < cost:
                continue
                
            for next_cost, next_node in graph[node]:
                new_cost = cost + next_cost
                
                if dists[next_node] <= new_cost:
                    continue
                
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
                
        return dists[goal]
    
    def dijkstra_a(goal):
        
        pq = [(0, a)]
        dists = [0xffffffff] * (n+1)
        dists[a] = 0
        
        while pq:
            
            cost, node = heapq.heappop(pq)
            
            if dists[node] < cost:
                continue
                
            for next_cost, next_node in graph[node]:
                new_cost = cost + next_cost
                
                if dists[next_node] <= new_cost:
                    continue
                
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
                
        return dists[goal]
    
    def dijkstra_b(goal):
        
        pq = [(0, b)]
        dists = [0xffffffff] * (n+1)
        dists[b] = 0
        
        while pq:
            
            cost, node = heapq.heappop(pq)
            
            if dists[node] < cost:
                continue
                
            for next_cost, next_node in graph[node]:
                new_cost = cost + next_cost
                
                if dists[next_node] <= new_cost:
                    continue
                
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
                
        return dists[goal]
    
    graph = [[] for _ in range(n+1)]
    
    for start, end, cost in fares:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
        
    answer = 0xfffffffffffff
    
    for k in range(1, n+1):
        
        answer = min(answer, dijkstra_s(k) + dijkstra_a(k) + dijkstra_b(k))
    
    return answer