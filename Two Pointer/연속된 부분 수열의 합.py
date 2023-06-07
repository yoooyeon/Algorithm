# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    answer = []
    s = 0
    e = 0
    sum_ = sequence[0]
    len_ = float('inf')
    while s <= e and e < len(sequence):

        if k == sum_:  # 목표값이라면
            if e - s < len_:
                answer = [s, e]
                len_ = e - s
            sum_ -= sequence[s]
            s += 1
            continue
            
        if sum_ < k: # 목표값보다 작으면
            e += 1
            if e < len(sequence):
                sum_ += sequence[e]
        else: # 목표값보다 크면
            # e는 인덱스를 증가시키고 sum_에서 더하는 반면 
            #s는 sum_에서 빼주고 인덱스를 증가시킨다
            
            sum_ -= sequence[s] 
            s += 1

    return answer


print(solution([1, 2, 3, 4, 5], 7))
