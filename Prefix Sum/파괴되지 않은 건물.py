# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skills):
    
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp_arr = [[0] * (m + 1) for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skills:
        
        if type == 1:
            tmp_type = -1
        else:
            tmp_type = 1

        tmp_arr[r1][c1] += degree * tmp_type
        tmp_arr[r1][c2 + 1] -= degree * tmp_type
        tmp_arr[r2 + 1][c1] -= degree * tmp_type
        tmp_arr[r2 + 1][c2 + 1] += degree * tmp_type
        
    # 왼쪽에서 오른쪽으로 누적
    for x in range(n):
        for y in range(1, m):
            tmp_arr[x][y] += tmp_arr[x][y - 1]
    # 위에서 아래로 누적
    for i in range(m):
        for j in range(1, n):
            tmp_arr[j][i] += tmp_arr[j - 1][i]

    # 누적합 더하기
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp_arr[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

