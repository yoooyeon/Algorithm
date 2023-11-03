def solution(relation):
    R = len(relation)
    C = len(relation[0])
    orders = []

    def dfs(L, now, target, picked):
        if L == target:
            orders.append(picked.copy())
            return
        for i in range(now, C):
            if i not in picked:
                picked.append(i)
                dfs(L + 1, i, target, picked)
                picked.pop()

    for i in range(1, len(relation[0]) + 1):
        dfs(0, 0, i, [])

    def is_minimal(keys, order):
        for key in keys:
            if set(key).issubset(order):
                return False
        return True

    keys = []
    for order in orders:
        if not is_minimal(keys, order):
            continue
        tmp2 = []
        for row in relation:
            tmp = []
            for col_no in order:
                tmp.append(row[col_no])
            if tmp not in tmp2:
                tmp2.append(tmp)
        if len(tmp2) == R:
            keys.append(order)
    return len(keys)
