N = int(input())
M = int(input())
li = list(map(int, input().split()))
li.sort()
s, e = 0, N - 1
ans = 0
while s < e:
    sum_ = li[s] + li[e]
    if sum_ == M:
        ans += 1
        e -= 1
        s += 1
    if sum_ > M:
        e -= 1
    if sum_ < M:
        s += 1
print(ans)
