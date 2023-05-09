n = list(map(int, input()))
n.sort()
res = n[0]
for i in range(1, len(n)):
    if n[i] + res > n[i] * res:
        res = n[i] + res
    else:
        res = n[i] * res
print(res)

# 곱하기 혹은 더하기 해서 가장 큰 수
