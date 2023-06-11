# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles): # m: 열, n: 행
    MOD = 1000000007
    dp = [[1] * m for _ in range(n)] # 1로 세팅
    
    for x, y in puddles:
        dp[y-1][x-1] = 0
        
    # 1행 체크
    for i in range(m): # 웅덩이 다음은 갈 수 없음
        if dp[0][i] == 0:
            for j in range(i+1, m):
                dp[0][j] = 0
            break
    # 1열 체크
    for i in range(n): # 웅덩이 다음은 갈 수 없음
        if dp[i][0] == 0:
            for j in range(i+1, n):
                dp[j][0] = 0
            break
            
    # 오른쪽 아래로만 움직일 수 있기 때문에 이중 포문을 사용하면 된다.
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != 0: # 웅덩이가 아니면
                dp[i][j] = (dp[i-1][j] % MOD) + (dp[i][j-1] % MOD)

    return dp[-1][-1] % MOD

