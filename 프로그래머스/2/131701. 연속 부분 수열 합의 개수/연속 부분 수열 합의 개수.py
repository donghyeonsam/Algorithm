def solution(elements):

    n = len(elements)
    result_lst = []
    num = 1
   
    while num != n+1:
        
        for idx in range(n):
            
            sum_lst = []
            
            if idx + num >= n:
                l = num - n + idx
                sum_lst = sum_lst + elements[idx:n] + elements[:l]

            else:
                sum_lst += elements[idx:idx+num]
                
            part_sum = sum(sum_lst)
            result_lst.append(part_sum)

        num += 1
        
    result_lst = set(result_lst)
    answer = len(result_lst)

    return answer