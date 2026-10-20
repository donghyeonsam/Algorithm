n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer= -10000000000000

for row in range(n-k+1):
    cur = 0

    for i in range(row, row+k):
        for j in range(k):
            cur += arr[i][j]
    
    answer = max(answer, cur)

    for col in range(n-k):
        cur += sum([arr[row+idx][col+k] for idx in range(k)]) - sum([arr[row+idx][col] for idx in range(k)])
        answer = max(answer, cur)

print(answer)