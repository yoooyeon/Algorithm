from heapq import heappop, heappush


def solution(k, n, reqs):
    answer = float('inf')
    MAX = n - k + 1
    memo = [[0 for _ in range(MAX + 1)] for _ in range(k)]  # 행: 상담 유형

    def get_time(type_no, ct_cnt):  # 상담 유형, 상담 인원에 따른 시간 계산 & 메모에 저장
        q = [0 for _ in range(ct_cnt)]
        wait_time = 0
        for start, time, type in reqs:
            if type == type_no:
                available = heappop(q)

                if available <= start:  # 대기 없이 가능
                    heappush(q, start + time)
                else:
                    wait_time += available - start
                    heappush(q, available + time)

        return wait_time

    def calcuate(arr):  # 메모를 참고해 계산 후 정답을 갱신
        nonlocal answer
        tmp = 0
        for i in range(k):  # 유형 실 번호는 i+1
            tmp += memo[i][arr[i]]
        answer = min(answer, tmp)

    def dfs(total, div, path):  # 순열로 상담원 인원 배치
        if div == 1:
            arr = path + [total]
            calcuate(arr.copy())
            return

        for i in range(1, total - div + 2):
            dfs(total - i, div - 1, path + [i])

    for i in range(k):
        for j in range(1, MAX + 1):
            memo[i][j] = get_time(i + 1, j)  # 상담 유형, 담당 인원
    dfs(n, k, [])
    return answer


# print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))
print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1],
                      [70, 100, 2]]))
