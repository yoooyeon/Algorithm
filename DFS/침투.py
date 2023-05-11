# 백준 13565
import sys

sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
data = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
res = ""
for _ in range(N):
    data.append(list(map(int, list(input()))))
visited = [[0 for _ in range(M)] for _ in range(N)]


def dfs(x, y):
    global res
    if x == N - 1:
        res = "YES"
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and data[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny)


for i in range(M):
    x, y = 0, i
    if visited[0][i] == 0 and data[0][i] == 0:
        visited[0][i] = 1
        dfs(0, i)
if res == "":
    print("NO")
else:
    print(res)
