import heapq

def solution(n, roads, sources, destination):
    
    def dijkstra(start_node):
        
        pq = [(0, start_node)]
        dists = [0xffffffffff] * (n+1)
        dists[start_node] = 0
        result = []
        
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
            
        for location in sources:
            if dists[location] == 0xffffffffff:
                result.append(-1)
            else:
                result.append(dists[location])
        
        return result

        
    graph = [[] for _ in range(n+1)]

    for start, end in roads:
        graph[start].append((1, end))
        graph[end].append((1, start))
        
    answer = dijkstra(destination)
    
    return answer