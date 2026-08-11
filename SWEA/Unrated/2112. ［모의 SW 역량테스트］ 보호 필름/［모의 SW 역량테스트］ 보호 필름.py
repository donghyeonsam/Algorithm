from itertools import product, combinations

def solution():

    for r in range(D+1):
        for rows in combinations(range(D), r):
            for values in product([0, 1], repeat=r):
                temp = []
                for row in rows:
                    temp.append(film[row][:])

                for i in range(r):
                    row = rows[i]
                    val = values[i]
                    for col in range(W):
                        film[row][col] = val

                if inspection(film):
                    return r

                for t in range(r):
                    film[rows[t]] = temp[t]

def inspection(new_film):

    col = 0

    while col < W:

        last = new_film[0][col]
        cnt = 1
        passed = False
        for row in range(1, D):
            if last == new_film[row][col]:
                cnt += 1
            else:
                cnt = 1
            last = new_film[row][col]
            if cnt >= K:
                passed =True
                break

        if not passed:
            return False

        col += 1

    return True


T = int(input())

for tc in range(1, T+1):

    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    result = 0

    result = solution()
    print(f'#{tc} {result}')
