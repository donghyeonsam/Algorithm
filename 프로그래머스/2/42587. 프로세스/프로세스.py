def solution(priorities, location):
    
    answer = 0
    queue = []
    n = len(priorities)
    check_lst = [False] * n

    while len(queue) < n:
        
        for idx in range(n):
            if check_lst[idx] == False and priorities[idx] >= max(priorities[i] for i in range(n) if not check_lst[i]):
                check_lst[idx] = True
                if idx == location:
                    queue.append(1)
                else:
                    queue.append(0)
            else:
                continue        
    
    for idx in range(n):
        if queue[idx]:
            answer = idx + 1
    
    return answer