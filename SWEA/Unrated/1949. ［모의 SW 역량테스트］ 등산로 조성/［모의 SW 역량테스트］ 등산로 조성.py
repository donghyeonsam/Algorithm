def DFS(row, col, root, k_cnt):

    global result
    global visited

    visited[row][col] = 1
    if result <= root:
        result = root
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx = row + dx
        ny = col + dy
        if 0 <= nx < n and 0 <= ny < n and mnt[nx][ny] < mnt[row][col] and visited[nx][ny] == 0:
            DFS(nx, ny, root+1, k_cnt)
        elif k_cnt == 1 and 0 <= nx < n and 0 <= ny < n and mnt[nx][ny] - k < mnt[row][col] and mnt[nx][ny] >= mnt[row][col] and visited[nx][ny] == 0:
            original = mnt[nx][ny]
            mnt[nx][ny] = mnt[row][col] - 1
            DFS(nx, ny, root+1, k_cnt-1)
            mnt[nx][ny] = original
    visited[row][col] = 0

T = int(input())

for tc in range(1, T+1):

    n, k = list(map(int, input().split()))
    mnt = [list(map(int, input().split())) for _ in range(n)]
    max_m = 0
    result = 0
    visited = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if mnt[row][col] > max_m:
                max_m = mnt[row][col]
    for row in range(n):
        for col in range(n):
            if mnt[row][col] == max_m:
                DFS(row, col, 1, 1)

    print(f'#{tc} {result}')