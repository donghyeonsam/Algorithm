dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def line(x, y, dirt):

    changed = []
    connected = False
    for k in range(1, N):
        nx, ny = x + dx[dirt] * k, y + dy[dirt] * k
        if not (0 <= nx < N and 0 <= ny < N):
            break
        if board[nx][ny] != 0:
            return [], 0
        changed.append((nx, ny))
        if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
            connected = True
            break
    if not connected:
        return [], 0

    for ix, iy in changed:
        board[ix][iy] = 2

    return changed, 1

def DFS(p_num, complete):

    global result, tot_complete

    if complete + (len(prosessor) - p_num) < tot_complete:
        return

    if p_num == len(prosessor):
        cnt = 0
        for row in range(N):
            for col in range(N):
                if board[row][col] == 2:
                    cnt += 1
        if complete > tot_complete:
            tot_complete = complete
            result = cnt
        elif complete == tot_complete:
            result = min(result, cnt)
        return

    x, y = prosessor[p_num]

    for dirt in range(4):
        changed, c_cnt = line(x, y, dirt)
        DFS(p_num+1, complete + c_cnt)

        for idx in range(len(changed)):
            board[changed[idx][0]][changed[idx][1]] = 0
    DFS(p_num+1, complete)

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    prosessor = []
    result = 0xffffffffff
    tot_complete = 0

    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                if row == 0 or row == N - 1 or col == 0 or col == N - 1:
                    continue
                prosessor.append((row, col))

    DFS(0, 0)

    print(f'#{tc} {result}')