def inspection(cur, type, cost):

    global plan

    if type == 'A':
        new_cost = cost + A * plan[cur]
        temp = plan[cur]
        plan[cur] = 0
        purchase(cur+1, new_cost)
        plan[cur] = temp
    elif type == 'B':
        new_cost = cost + B
        temp = plan[cur]
        plan[cur] = 0
        purchase(cur+1, new_cost)
        plan[cur] = temp
    elif type == 'C':
        new_cost = cost + C
        temp = plan[cur:cur+3]
        plan[cur:cur+3] = [0, 0, 0]
        purchase(cur+3, new_cost)
        plan[cur:cur+3] = temp
    else:
        new_cost = cost + D
        temp = plan[:]
        plan[:] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        purchase(13, new_cost)
        plan[:] = temp


def purchase(s, cost):

    global result

    if cost > result:
        return

    cnt = 0
    for k in range(13):
        if plan[k] == 0:
            cnt += 1
    if cnt == 13:
        result = min(result, cost)
        return result

    for i in range(s, 13):
        if plan[i] != 0:
            inspection(i, 'A', cost)
            inspection(i, 'B', cost)
            inspection(i, 'C', cost)
            inspection(i, 'D', cost)



T = int(input())

for tc in range(1, T+1):

    A, B, C, D = map(int, input().split())
    plan = [0]
    plan += list(map(int, input().split()))
    result = 0xfffffffffffff
    start = 0

    for idx in range(1, 13):
        if plan[idx] != 0:
            start = idx
            break

    purchase(start, 0)

    print(f'#{tc} {result}')