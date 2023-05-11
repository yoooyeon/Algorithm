# 백준 16173
N = int(input())
data = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)

dx = [1, 0]
dy = [0, 1]

def dfs(x, y, d): # (행, 열, 이동 가능 거리)
    global result
    if result == "HaruHaru": # 한번이라도 종료 지점에 도달햇다면 종료
        return
    if x == N - 1 and y == N - 1:
        result = "HaruHaru"
        return
    flag = True # 움직일 수 있는지 체크용
    for i in range(2):
        if d <= 0:
            break
        nx = x + dx[i] * d
        ny = y + dy[i] * d
        if 0 <= nx < N and 0 <= ny < N:
            flag = False
            dfs(nx, ny, data[nx][ny])
    if flag:
        result = "Hing"
        return


result = ""
dfs(0, 0, data[0][0])
print(result)
