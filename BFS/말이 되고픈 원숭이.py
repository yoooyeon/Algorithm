# 백준 1600
from collections import deque
from pprint import pprint

K = int(input())
W, H = map(int, input().split())
board = []
for _ in range(H):
    board.append(list(map(int, input().split())))
knight_x = [2, 2, -2, -2, 1, -1, 1, -1]
knight_y = [1, -1, 1, -1, 2, 2, -2, -2]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[0 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]


def bfs(x, y, cnt):
    global K
    q = deque()
    q.append((x, y, cnt, K))
    while q:
        x, y, cnt, K = q.popleft()  # pop()이 아닌 popleft() 주의
        if x == H - 1 and y == W - 1:
            return cnt
        if K > 0:
            for k in range(8):
                nx = x + knight_x[k]
                ny = y + knight_y[k]
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][K - 1] and board[nx][ny] == 0:
                    visited[nx][ny][K - 1] = 1
                    q.append((nx, ny, cnt + 1, K - 1))

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][K] and board[nx][ny] == 0:
                visited[nx][ny][K] = 1
                q.append((nx, ny, cnt + 1, K))

    return -1


visited[0][0][K] = 1
print(bfs(0, 0, 0))
