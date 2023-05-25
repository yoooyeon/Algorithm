# 백준 1967
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
tree = {}
for i in range(n):
    tree[i + 1] = []
for _ in range(n - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))


def dfs(a, d):
    if a == 0:
        return
    for n, dist in tree[a]:
        if visited[n] == -1:
            visited[n] = d + dist
            dfs(n, d + dist)
    return


# max_dist = max(max_dist, d)


visited = [-1 for _ in range(n + 1)]
max_dist = 0
max_node = 0
visited[1] = 0
dfs(1, 0)
for i in range(len(visited)):
    if max_dist < visited[i]:
        max_dist = visited[i]
        max_node = i
max_dist = 0
visited = [-1 for _ in range(n + 1)]
visited[max_node] = 0
dfs(max_node, 0)
print(max(visited))
