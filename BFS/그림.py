# 백준 1926
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]


def bfs(x, y, no):
    q = deque()
    q.append((x, y, no))
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 1
    while q:
        x, y, no = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = 1
                board[nx][ny] = no
                cnt += 1
                q.append((nx, ny, no))

    return cnt
no = 2
ans=[]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            ans.append(bfs(i, j, no))
            no += 1
print(len(ans))
print(max(ans))

