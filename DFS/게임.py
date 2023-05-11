# 백준 1103
# dfs + dp 문제


import sys
N, M = map(int, sys.stdin.readline().split())
data = []
for i in range(N):
    tmp = sys.stdin.readline()
    data.append(tmp[:-1])
visited = [[False for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]


def dfs(x, y, dist):
    global maxDist
    maxDist = max(maxDist, dist)
    move = int(data[x][y])
    ajlist = [[x + move, y], [x - move, y], [x, y + move], [x, y - move]]
    for nx, ny in ajlist:
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] != 'H' and dist + 1 > dp[nx][ny]: # 범위 안벗어나는지, 구멍 아닌지, 최소 이동거리인지
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dp[nx][ny] = dist + 1
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False

            else:
                print(-1)
                exit()

maxDist = -1
dfs(0, 0, 1)
print(maxDist)
