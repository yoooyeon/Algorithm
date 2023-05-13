# 백준 1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

n, m = map(int, input().split())
query = []
group = [i for i in range(n + 1)]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        group[y] = x
    else:
        group[x] = y


def find(x):
    if x == group[x]:
        return x
    group[x] = find(group[x])
    return group[x]


for _ in range(m):
    a, b, c = map(int, input().split())
    query.append([a, b, c])
    if a == 0:  # 그룹 짓기
        union(b, c)
    else:  # 같은 그룹인지 확인
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")

