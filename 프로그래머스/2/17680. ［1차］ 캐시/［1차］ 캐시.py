from collections import deque

def solution(cacheSize, cities):
    
    answer = 0
    n = len(cities)
    queue = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for idx in range(n):
        
        if len(queue) == cacheSize:
            
            if cities[idx].lower() in queue:
                queue.remove(cities[idx].lower())
                queue.append(cities[idx].lower())
                answer += 1
                
            else:
                queue.popleft()
                queue.append(cities[idx].lower())
                answer += 5
        
        else:
            
            if cities[idx].lower() in queue:
                queue.remove(cities[idx].lower())
                queue.append(cities[idx].lower())
                answer += 1
                
            else:
                queue.append(cities[idx].lower())
                answer += 5
    
    return answer