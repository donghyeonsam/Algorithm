def solution(n, left, right):
    
    answer = []
    
    left_row = left // n
    left_col = left % n
    right_row = right // n
    right_col = right % n
    
    if left_row == right_row:
        
        for idx in range(left_col, right_col+1):
            
            if left_row >= idx:
                answer.append(left_row+1)
            else:
                answer.append(idx+1)
    
    else:
        
        for idx in range(left_col, n):

            if left_row >= idx:
                answer.append(left_row+1)
            else:
                answer.append(idx+1)

        for row in range(left_row+1, right_row):
            lst = []

            for col in range(n):
                if row >= col:
                    lst.append(row+1)
                else:
                    lst.append(col+1)
            answer += lst

        for idx in range(right_col+1):

            if right_row >= idx:
                answer.append(right_row+1)
            else:
                answer.append(idx+1)

    return answer