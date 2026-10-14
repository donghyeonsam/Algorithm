def solution(s):
    
    answer = 0
    l = len(s)
    stack = [s[0]]
    
    if l % 2 != 0:
        return 0

    for idx in range(1, l):
        stack_len = len(stack)
        
        if stack_len == 0:
            stack.append(s[idx])
            continue
        
        if s[idx] == stack[stack_len-1]:
            stack.pop(stack_len-1)
        else:
            stack.append(s[idx])
        
    if len(stack) == 0:
        answer = 1
     
    return answer