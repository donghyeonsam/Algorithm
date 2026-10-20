n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 슬라이딩 윈도우 방식
sum_num = sum(arr[:k])
answer = sum_num

for idx in range(k, n):

    sum_num = sum_num - arr[idx-k] + arr[idx]
    answer = max(answer, sum_num)

print(answer)