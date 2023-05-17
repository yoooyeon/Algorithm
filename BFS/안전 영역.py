from collections import deque
from copy import deepcopy

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


def bfs(x, y, board):
    global tmp_visited
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not tmp_visited[nx][ny] and board[nx][ny] > 0:
                tmp_visited[nx][ny] = 1
                q.append((nx, ny))


max_height = max(map(max, board))
ans = []
visited = [[0 for _ in range(n)] for _ in range(n)]
for k in range(max_height, 0, -1): # 모든 높이 체크
    tmp_board = deepcopy(board)
    tmp_visited = deepcopy(visited)
    # 높이 제한에 따라 안전하지 않은 지점은 0으로 세팅
    for i in range(n):
        for j in range(n):
            if tmp_board[i][j] < k:
                tmp_board[i][j] = 0
                
    cnt = 0 # 안전영역 갯수
    
    for i in range(n): # 안전영역 갯수 체크
        for j in range(n):
            if tmp_board[i][j] > 0 and not tmp_visited[i][j]:
                cnt += 1
                tmp_visited[i][j] = 1
                bfs(i, j, tmp_board)
    ans.append(cnt)
# print(ans)
print(max(ans))
