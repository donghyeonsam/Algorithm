def solution(distance, rocks, n):
    
    answer = 0
    rocks.append(distance)
    rocks.sort()
    m = len(rocks)
    low = 1
    high = distance
    
    while low <= high:
        
        mid = (low + high) // 2
        
        stones = 0
        prev = 0
        
        for idx in range(m):
            if stones > n:
                break
        
            if rocks[idx] - prev < mid:
                stones += 1
            else:
                prev = rocks[idx]
                
        if stones <= n:
            low = mid + 1
            answer = max(answer, mid)
        else:
            high = mid - 1
            
    return answer