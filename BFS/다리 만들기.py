from collections import deque
import sys

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]


# 각 섬에 번호 붙이기 2 ~ 
def group_bfs(x, y, no):
    global visited, board
    q = deque()
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = 1
                board[nx][ny] = no
                q.append((nx, ny))


# 한 섬에서 다른 섬으로 가는 최단 거리 구하기
# 같은 섬의 좌표를 방문처리 하고 q에 넣어주는 것이 핵심
def bridge_bfs(now_no):
    global board
    q = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    answer = sys.maxsize

    for i in range(n):
        for j in range(n):
            if board[i][j] == now_no:
                visited[i][j] = 1
                q.append((i, j))
                
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            
            nx, ny = x + dx[k], y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] != now_no:
                
                if board[nx][ny] > 0: # 다른 섬
                    answer = min(answer, visited[x][y])
                    return answer
                else: # 바다
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return answer


no = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == 1:
            visited[i][j] = 1
            no += 1
            board[i][j] = no
            group_bfs(i, j, no)

answer = sys.maxsize
for i in range(2, no):
    answer = min(answer, bridge_bfs(i))

print(answer - 1)
