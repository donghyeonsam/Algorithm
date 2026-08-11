from copy import deepcopy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def drop(board):

    for col in range(W):
        last_x =  H - 1
        for row in range(H-1, -1, -1):
            if board[row][col] != 0:
                board[last_x][col] = board[row][col]
                if last_x != row:
                    board[row][col] = 0
                last_x -= 1

    return board

def chain_crash(x, y, tmp, board):

    for idx in range(4):
        for k in range(1, tmp+1):
            nx, ny = x + dx[idx] * k, y + dy[idx] * k
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                elif board[nx][ny] > 1:
                    new_tmp = board[nx][ny] - 1
                    board[nx][ny] = 0
                    chain_crash(nx, ny, new_tmp, board)

    return board

def crash(idx, board):

    for row in range(H):
        if board[row][idx] != 0:
            tmp = board[row][idx] - 1
            if tmp == 0:
                board[row][idx] = 0
                return board
            else:
                board[row][idx] = 0
                board = chain_crash(row, idx, tmp, board)
                return drop(board)

    return board

def play(depth, org_bricks):

    global min_remain

    if depth == N:
        cnt = 0
        for row in range(H):
            for col in range(W):
                if org_bricks[row][col] != 0:
                    cnt += 1
        min_remain = min(min_remain, cnt)
        return min_remain

    for idx in range(W):
        board = deepcopy(org_bricks)
        board = crash(idx, board)
        play(depth + 1, board)

T = int(input())

for tc in range(1, T+1):

    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_remain = 0xffffffffffff

    play(0, bricks)

    print(f'#{tc} {min_remain}')
