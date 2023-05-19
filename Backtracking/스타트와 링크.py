# 백준 14889
import sys

n = int(input())
S = []
for _ in range(n):
    S.append(list(map(int, input().split())))

def get_score(marked):
    global ans
    start = 0
    link = 0
    for i in range(n):
        for j in range(i, n):
            if marked[i] and marked[j]:
                start += S[i][j] + S[j][i]
            if not marked[i] and not marked[j]:
                link += S[i][j] + S[j][i]

    ans = min(ans, abs(link - start))

def get_team(cnt, idx):
    if cnt == n // 2:
        get_score(marked)
        return

    if idx >= n:
        return

    marked[idx] = 1
    get_team(cnt + 1, idx + 1)
    marked[idx] = 0
    get_team(cnt, idx + 1)

ans = sys.maxsize
marked = [0 for _ in range(n)]
get_team(0, 0)
print(ans)
