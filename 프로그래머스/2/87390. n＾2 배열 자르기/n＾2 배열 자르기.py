def solution(n, left, right):
    
    answer = []
    
    for idx in range(left, right+1):
        r = idx // n;
        c = idx % n;
        
        if r >= c:
            answer.append(r+1);
        else:
            answer.append(c+1);
    return answer