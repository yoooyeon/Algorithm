# 백준 1949
# dfs + dp

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    global visited
    visited[cur] = 1
    for x in tree[cur]:
        if not visited[x]:
            dfs(x)
            dp[cur][0] += max(dp[x][0], dp[x][1])  # 방문x - 이전 노드 방문 하거나 안하거나 상관 없음
            dp[cur][1] += dp[x][0]  # 방문 - 이전 노드 방문 안함
            # print(dp)


n = int(input())
cost = [0] + list(map(int, input().split()))
tree = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [0 for _ in range(n + 1)]
# print(tree)
dp = [[0, cost[i]] for i in range(n + 1)]
dfs(1)
# print(dp)
print(max(dp[1][0], dp[1][1]))
