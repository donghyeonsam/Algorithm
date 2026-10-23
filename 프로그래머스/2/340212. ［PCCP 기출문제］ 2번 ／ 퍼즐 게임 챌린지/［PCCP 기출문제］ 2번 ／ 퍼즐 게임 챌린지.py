def solution(diffs, times, limit):

    answer = 0
    low = 1
    high = max(diffs)
    min_level = 0xfffffffff
    
    while low <= high:
        
        mid = (low + high) // 2
        
        tot_times = 0
        
        if mid >= diffs[0]:
            tot_times += times[0]
        else:
            tot_times += times[0] * (diffs[0] - mid + 1)

        for idx in range(1, len(diffs)):
            if mid >= diffs[idx]:
                tot_times += times[idx]
            else:
                tot_times += times[idx] + (times[idx] + times[idx-1]) * (diffs[idx] - mid)                     
        if tot_times > limit:
            low = mid + 1
        else:
            high = mid - 1
            min_level = min(min_level, mid)
    
    answer = min_level
                                 
    return answer