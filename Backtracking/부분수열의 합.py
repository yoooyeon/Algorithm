# 백준 1182
n, s = map(int, input().split())
li = list(map(int, input().split()))


def dfs(idx, cnt, target_cnt):
    global ans
    if cnt == target_cnt:
        sum_ = 0
        for i in range(n):
            if marked[i]:
                sum_ += li[i]
        if sum_ == s:
            ans += 1
        
        return

    if idx >= n:
        return

    marked[idx] = 1
    dfs(idx + 1, cnt + 1, target_cnt)
    marked[idx] = 0
    dfs(idx + 1, cnt, target_cnt)


ans = 0
marked = [0 for _ in range(n)]
for i in range(1, n + 1):
    dfs(0, 0, i)
print(ans)
