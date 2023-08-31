def solution(stones, k):
    left = 1
    right = 200000000 # stone의 최댓값
    # 이진탐색
    while left <= right:
        mid = (left + right) // 2 
        cnt = 0
        for i in stones:
            if i < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

