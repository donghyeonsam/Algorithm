def solution(n, times):
    
    low = 0
    high = max(times) * n
    answer = high
    
    while low <= high:
        
        mid = (low + high) // 2        
        complete = 0
        
        for supervisor in times:
            
            complete += mid // supervisor
            
        if complete < n:        
            low = mid + 1
            continue
            
        else:
            answer = mid
            high = mid - 1
            continue
    
    return answer