# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    completed = 0
    reported = [0 for _ in range(n)] # 배포 체크
    while completed < n:
        # 배포 완료 가능한 것 있는지 체크
        part_completed = 0 # 이번 배포 갯수
        for i in range(n):
            if progresses[i] >= 100:
                if not reported[i]:
                    part_completed += 1
                    reported[i] = 1
            else:
                break
        if part_completed > 0:
            completed += part_completed
            answer.append(part_completed)
        # 작업 진행
        for i in range(n):
            progresses[i] += speeds[i]
    return answer
