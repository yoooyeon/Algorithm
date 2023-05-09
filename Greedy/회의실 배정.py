n = int(input())
se_list = []
for i in range(n):
    s, e = map(int, input().split())
    se_list.append([s, e])
se_list.sort(key=lambda x: (x[1], x[0]))

ans = 0
p = 0
for s, e in se_list:
    if s >= p:
        ans += 1
        p = e
print(ans)
