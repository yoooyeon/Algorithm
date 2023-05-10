def dfs(n):
    global mark
    mark[n - 1] = 1

    if dic[n]:
        for x in dic[n]:
            if not mark[x - 1]:
                dfs(x)


N, M = map(int, input().split())
dic = {}
mark = [0 for _ in range(N)]
ans = 0
for i in range(N):
    dic[i + 1] = []
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
print(dic)
for i in range(N):
    if not mark[i]:
        # mark[i + 1] = 1
        ans += 1
        dfs(i + 1)
print(ans)
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
