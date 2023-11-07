import math

n, m = map(int, input().split())
li = [[0, 0]]  # 우주신 위치 1 ~ n
li2 = []  # 연결된 우주신
parent = [i for i in range(n + 1)]
channel = []


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if a > b:
        parent[a] = b
        return True
    else:
        parent[b] = a
        return True


for _ in range(n):
    li.append(list(map(int, input().split())))
    
for _ in range(m):
    a, b = map(int, input().split())
    li2.append([a, b])
    union(a, b)
    channel.append(a)
    channel.append(b)
    
distance = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
graph = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        if i < j:
            break
        x1, y1 = li[i]
        x2, y2 = li[j]
        graph.append([math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), i, j])
graph.sort()

ans = 0

for d, a, b in graph:
    if union(a, b):
        ans += d

print('{:.2f}'.format(ans))

