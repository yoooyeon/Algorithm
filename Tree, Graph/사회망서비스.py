# 백준 2533
# dfs + dp
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def dfs(cur):
    global visited, dp
    visited[cur] = 1
    for p in tree[cur]:
        if visited[p]: continue
        dfs(p)
        dp[cur][0] += dp[p][1]  # 내가 얼리어답터가 아닌 경우 자식들은 모두 얼리어답터를 충족해야함
        dp[cur][1] += min(dp[p])  # 내가 얼리어답터인경우 자식은 비용이 적은것으로 택한다


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [[0, 1] for i in range(n + 1)]
visited = [0 for _ in range(n + 1)]
dfs(1)
print(min(dp[1]))
